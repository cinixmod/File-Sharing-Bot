import os
import logging
import asyncio
from bot import Client

# Read environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Initialize the client directly
client = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    async with client:
        try:
            await client.start()
            logging.info("Bot started successfully!")
            await client.idle()  # Keep the bot running
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
