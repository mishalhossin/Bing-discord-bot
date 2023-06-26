# Bing Chatbot for Discord

This is a chatbot implemented in Discord using the Bing API for natural language processing. The chatbot interacts with users in text channels, providing automated responses based on user prompts.

## Features

- Responds to user messages with generated responses from the Bing API.
- Supports both active channels and direct messages (DMs).
- Toggles the inclusion of specific channels or DMs as active for chat interactions.
- Provides an interactive help command to view available commands.

## Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/mishalhossin/Bing-discord-bot
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Configure the environment variables:

   - Create a `.env` file based on the `.env.example` file.
   - Set the `DISCORD_TOKEN` environment variable in the `.env` file with your Discord bot token.

4. Run the bot:

   ```shell
   python main.py
   ```

## Usage

- After inviting the bot to your Discord server using the provided invite link, you can interact with the bot in text channels or by sending direct messages to it.
- The bot will respond to your messages with generated responses based on the Bing's natural language processing capabilities.
- You can use the `/togglechannel` command to include or exclude specific channels from the active channel list. This determines whether the bot will respond to messages in those channels.
- You can use the `/toggledm` command to toggle the ability to interact with the bot through direct messages.
- For a list of all available commands, you can use the `/help` command.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
