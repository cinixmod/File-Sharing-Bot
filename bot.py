import os
import logging
import asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from pyrogram.errors import FloodWait

# Setup logging
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Read environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "madflixbotz")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))

try:
    ADMINS = [6848088376]
    for x in os.environ.get("ADMINS", "6848088376").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")

# Initialize the bot
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def start_bot():
    async with bot:
        try:
            await bot.start()
            logging.info("Bot started successfully!")
            # You can add your main bot logic here
            await bot.idle()  # Keep the bot running
        except FloodWait as e:
            logging.warning(f"Flood wait for {e.x} seconds. Retrying...")
            await asyncio.sleep(e.x)  # Wait for the specified time
            await start_bot()  # Retry starting the bot
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(start_bot())
