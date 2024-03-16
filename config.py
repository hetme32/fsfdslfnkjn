import os

try:
    app_id = int(os.environ.get("app_id", "523894"))
except Exception as app_id:
    print(f"⚠️ App ID Invalid {app_id}")
try:
    api_hash = os.environ.get("api_hash", "e15ad5314295f")
except Exception as api_hash:
    print(f"⚠️ Api Hash Invalid {api_hash}")
try:
    bot_token = os.environ.get("bot_token", "683894700450:AAGtmIuSJgmjbkbi3vs")
except Exception as bot_token:
    print(f"⚠️ Bot Token Invalid {bot_token}")
try:
    custom_caption = os.environ.get("custom_caption", "<b>{file_name}</b>\n\n<b>JOIN 💎 : @M2LINKS</b>")
except Exception as custom_caption:
    print(f"⚠️ Custom Caption Invalid {custom_caption}")