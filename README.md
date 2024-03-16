# AutoCaptionBot

AutoCaptionBot is a Telegram bot created using Pyrogram that automatically adds captions to media files posted in channels.

## Features

- Automatically adds captions to photos, videos, animations, documents, audios, and other supported media types.
- Customizable caption format.
- Start command to greet users.

## Requirements

- Python 3.7 or higher
- Pyrogram library
- Telegram API credentials (app ID, API hash, bot token)

## Installation

1. Clone the repository:

2. Install the required dependencies:

3. Set up your Telegram API credentials:

    - Create a Telegram application at [Telegram Apps](https://my.telegram.org/apps).
    - Obtain the app ID and API hash.
    - Create a bot on Telegram and obtain the bot token.

4. Set up environment variables for your credentials:

    ```
    export app_id="YOUR_APP_ID"
    export api_hash="YOUR_API_HASH"
    export bot_token="YOUR_BOT_TOKEN"
    ```

5. Customize the caption format in the `custom_caption` variable in the `main.py` file if needed.

6. Run the bot:


## Usage

- Start the bot by sending the `/start` command in a private chat with the bot.
- Add the bot to your Telegram channel and grant it permission to edit messages.
- Post media files in the channel, and the bot will automatically add captions to them.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

