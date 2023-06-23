import os
import time
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

app = Client(
    "VideoDownloaderBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Handler function to download video
@Client.on_message(filters.command("download") & filters.private)
async def download_video(bot: Client, message: Message):
    text = message.text.split(" ")[1]
    # Use youtube-dl to download the video
    os.system(f"youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' -o 'video.mp4' {text}")
    # Upload the video to Telegram
    await message.reply_video(video="video.mp4")
    # Delete the temporary video file
    os.remove("video.mp4")

# Start the bot
app.run()
