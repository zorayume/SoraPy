from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.client.latency * 1000)
        await ctx.send(f"Pong! {latency}ms")

async def setup(client):
    await client.add_cog(Ping(client))