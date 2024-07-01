from flask import Flask, request
import logging, json, os

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
)

app = Flask(__name__)

try:
    config = json.load(open("config.json"))
except FileNotFoundError:
    config = {"file_path": "", "reboot_command": ""}
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    raise FileNotFoundError("Please fill out the config.json file")

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/event", methods=["POST"])
def handle_webhook():
    data = request.get_json()
    logging.info("Webhook received")
    logging.info(data)
    logging.info("Copying to server directory...")

    with open(config["file_path"], "w") as f:
        f.write(str(data))

    logging.info("Copied to server directory")
    logging.info("Rebooting server...")

    os.system(f"{config['reboot_command']}")

    logging.info("Service rebooted.")

    return "Webhook received successfully"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
