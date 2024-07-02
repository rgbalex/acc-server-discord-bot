import threading
from flask import Flask, request
import logging, json, os

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
)

app = Flask(__name__)
data = None
status = "running"

try:
    config = json.load(open("config.json"))
except FileNotFoundError:
    config = {"file_path": "", "reboot_command": ""}
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    raise FileNotFoundError("Please fill out the config.json file")


@app.route("/", methods=["GET"])
def home():
    global status
    return {"status": status}


@app.route("/event", methods=["POST"])
def handle_webhook():
    global data
    global status
    data = request.get_json()
    logging.info("Webhook received")
    logging.info(data)

    if status != "running":
        return "Server is currently rebooting. Please wait for it to finish."

    threading.Thread(target=handle_webhook).start()
    return "Webhook received successfully"


def handle_webhook():
    global data
    global status
    logging.info("Writing file...")
    with open("./event.json", "w") as f:
        f.write(str(data))
    logging.info("File written")

    logging.info("Rebooting server...")
    status = "rebooting"
    os.system(f"{config['reboot_command']}")
    status = "running"
    logging.info("Service rebooted.")

    logging.info("Copying to server directory...")
    return_value = os.system(f"sudo cp ./event.json {config['file_path']}")
    if return_value != 0:
        logging.error("Error copying file to server directory")
        status = "copy error"
        return "Error copying file to server directory"
    logging.info("Copied to server directory")
    return "Success"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
