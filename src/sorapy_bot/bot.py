import discord
from pathlib import Path
from discord.ext import commands, tasks
from colorama import Fore, Back, Style

class SoraPy(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content=True
        intents.members=True

        super().__init__(
            command_prefix="!",
            intents=intents,
        )

    async def on_ready(self):
        command_list = ", ".join([command.name for command in self.commands])

        print(Fore.GREEN + f"[INFO] Bot is Logged on as {self.user}" + Style.RESET_ALL)
        print(Fore.GREEN + f"[INFO] Loaded {command_list}", Style.RESET_ALL)

        if not self.update_status.is_running():
            self.update_status.start()

    @tasks.loop(minutes=3)
    async def update_status(self):
        member_count = sum(guild.member_count or 0 for guild in self.guilds)
        guild_count = len(self.guilds)
        status = [
            discord.Activity(type=discord.ActivityType.listening, name="A widely sea song"),
            discord.Activity(type=discord.ActivityType.watching, name=f"For {member_count} Members"),
            discord.Activity(type=discord.ActivityType.watching, name=f"For {guild_count} Servers")
        ]

        activity = status[self.update_status.current_loop % len(status)] 
        await self.change_presence(activity=activity)


    async def setup_hook(self):
        cogs_path = Path(__file__).parent / "cogs"

        for file in cogs_path.rglob("*.py"): # recursively search the cogs folder and its subfolder
            if file.name == "__init__.py":
                continue

            relative = file.relative_to(cogs_path) # strips the location to only cogs folder location

            # An example utility/info.py => utility/info
            module = relative.with_suffix("") # remove the suffix (extension)

            extensions = "sorapy_bot.cogs." + ".".join(module.parts)

            try:
                await self.load_extension(extensions)
                print(Fore.GREEN + f"[LOGS] Loaded {extensions}")

            except Exception as e:
                print(Fore.RED + Back.BLACK + f"Failed to load {extensions}")
                print(Fore.RED + Back.BLACK + f"{type(e).__name__}: {e}")
