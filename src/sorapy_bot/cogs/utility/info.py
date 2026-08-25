import discord
from discord.ext import commands
import time

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx):
        if ctx.guild is None:
            return await ctx.send("This command can be only used in servers")

        start = time.time()
        
        guild = ctx.guild

        server_name = guild.name
        server_id = guild.id
        member_count = guild.member_count
        server_owner = guild.owner
        server_created_at = guild.created_at.strftime("%B %d, %Y")

        embed = discord.Embed(title=f"{server_name}", color=discord.Color.green())
        embed.add_field(name="Server ID", value=server_id, inline=True)
        embed.add_field(name="Member Count", value=member_count, inline=True)
        embed.add_field(name="Server Owner", value=server_owner, inline=True)
        embed.add_field(name="Created At", value=server_created_at, inline=True)

        time.sleep(1)
        end = time.time()

        embed.set_footer(text=f"Speed: {end - start}")

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Info(client))