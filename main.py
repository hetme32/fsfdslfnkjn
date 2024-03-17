from pyrogram import Client, filters
import asyncio
from config import *

AutoCaptionBot = Client(
    "AutoCaptionBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

start_message = """
<b>Hello {} 👋,</b>\n
<b>I am an AutoCaption Bot</b>"""

@AutoCaptionBot.on_message(filters.private & filters.command(["start"]))
async def start_command(_, update):
    await update.reply_text(start_message.format(update.from_user.mention), disable_web_page_preview=True)


@AutoCaptionBot.on_callback_query(filters.regex("start"))
async def start_callback(_, update):
    await update.message.edit_text(start_message.format(update.from_user.mention), disable_web_page_preview=True)


@AutoCaptionBot.on_message(filters.channel)
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

AutoCaptionBot.run()
