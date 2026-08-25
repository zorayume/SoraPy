import discord
from pathlib import Path
from discord.ext import commands


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
        print("Bot is Logged on as", self.user)
        print("Commands:", [command.name for command in self.commands])

    async def setup_hook(self):
        cogs_path = Path(__file__).parent / "cogs"

        for file in cogs_path.rglob("*.py"): # recursively search the cogs folder and its subfolder
            if file.name == "__init__.py":
                continue

            relative = file.relative_to(cogs_path) # strips the location to only cogs folder location

            # An example utility/info.py => utility/info
            module = relative.with_suffix("") # remove the suffix (extension)

            extensions = "discordpy_bot.cogs." + ".".join(module.parts)

            try:
                await self.load_extension(extensions)
                print(f"Loaded: {extensions}")

            except Exception as e:
                print(f"Failed to load {extensions}")
                print(f"{type(e).__name__}: {e}")
