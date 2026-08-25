from discordpy_bot.bot import SoraPy
from discordpy_bot.config import DISCORD_TOKEN

def main():
    client = SoraPy()
    client.run(DISCORD_TOKEN)

# Run
if __name__ == "__main__":
    main()