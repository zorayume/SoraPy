import discord

from discordpy_bot.bot import MyClient
from discordpy_bot.config import DISCORD_TOKEN

def main() -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(DISCORD_TOKEN)

# Run main func
main()