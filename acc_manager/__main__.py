import os
import logging

from acc_manager.discord_main import DiscordBot
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    OWNER_ID = int(os.getenv("OWNER_ID"))

    logging.basicConfig(
        level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
    )

    bot = DiscordBot(prefix="!", ext_dir="cogs")

    bot.run()


if __name__ == "__main__":
    main()
