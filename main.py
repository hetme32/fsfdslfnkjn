from pyrogram import Client, filters
import asyncio
from config import *

app = Client(
    "app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

start_message = """
<b>Hello {} 👋,</b>\n
<b>I am an AutoCaption Bot</b>"""

help_message = """
<b>Commands :</b>\n
<b>set_caption : set customised Caption.</b>\n
<b>You can use :</b> <code>{file_name}</code>\n
<b>You can also use <a href=''>HTML Markdown tags</a></b>
"""

@app.on_message(filters.private & filters.command(["start"]))
async def start_command(_, update):
    await update.reply_text(start_message.format(update.from_user.mention), disable_web_page_preview=True)

@app.on_message(filters.private & filters.command(["help"]))
async def start_command(_, update):
    await update.reply_text(help_message, disable_web_page_preview=True)

@app.on_message(filters.private & filters.command(["add_capt","add","add_caption","set_caption"]))
async def add_caption_command(_, update):
    await update.reply_text("<b>Send me the new custom caption</b>")

@app.on_message(filters.private & ~filters.command(["start", "add_capt"]))
async def set_custom_caption(_, update):
    global CUSTOM_CAPTION
    CUSTOM_CAPTION = update.text
    await update.reply_text("<b>Custom caption set successfully!</b>")

@app.on_message(filters.channel)
async def edit_caption(_, update):
    media_obj, _ = get_file_details(update)
    try:
        await update.edit_caption(caption=CUSTOM_CAPTION.format(file_name=media_obj.file_name))
    except asyncio.exceptions.TimeoutError as TimeoutError:
        await asyncio.sleep(TimeoutError)
        await update.edit_caption(caption=CUSTOM_CAPTION.format(file_name=media_obj.file_name))


def get_file_details(update):
    if update.media:
        for message_type in (
                "photo",
                "animation",
                "audio",
                "document",
                "video",
                "video_note",
                "voice",
                # "contact",
                # "dice",
                # "poll",
                # "location",
                # "venue",
                # "sticker"
        ):
            obj = getattr(update, message_type)
            if obj:
                return obj, obj.file_id

print("Bot Started..")

app.run()
