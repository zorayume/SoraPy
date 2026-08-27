import discord
from sorapy_bot.bot import SoraPy
from sorapy_bot.config import DISCORD_TOKEN
from colorama import Fore, Back, Style

def main():
    client = SoraPy()
    try: 
        client.run(DISCORD_TOKEN)
    except discord.errors.LoginFailure:
        print(Fore.RED + Back.BLACK + "[ERROR - TOKEN INCORRECT] Your token may be not configured correctly or wrong token. Generate and copy from the developer portal" + Style.RESET_ALL)
        return
    except Exception as e:
        print(Fore.RED + Back.BLACK + f"[ERROR] Something has gone wrong. Here's your error: {e}")
        return

# Run
if __name__ == "__main__":
    main()