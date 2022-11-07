# simple-faqbot

## Quick Start

### Discord 

Follow the instructions for creating a bot: https://discordpy.readthedocs.io/en/stable/discord.html

When in the Bots tab of Applications, make sure to turn on the slider for all privileged Gateway Intents to test the bot.

### Edit `.env` file with your bot token

```bash
cp .env.template .env
````

### Launch with Docker 

```bash
docker-compose up -d
````


### Help

For a list of available commands send `.help` as a message in Discord or Telegram.


### Prefix

`command_prefix`: instead of the default `.` can modify to `/`, `$`, `#`, `!` or whatever you prefer.

### Status

`discord.Game()`: default is `with decentralized tools`.

## Contributing

The spaghetti code for this bot is held together by hope and a lot of bubble gum. It would be ideal for someone with actual software development skills can improve upon this and make it better. Thus, any improvements to this package is highly appreciated.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-stuff`)
3. Commit your changes (`git commit -am "Add new stuff improvements"`)
4. Push to branch (`git push origin feature/new-stuff`)
5. Open a pull request




