import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            latency = round(self.latency * 1000)
            await message.channel.send(f'pong! {latency}ms')

def main() -> None:
    load_dotenv() # Loads the env first
    discord_token = os.environ.get('TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(discord_token)

# Run main func
main()