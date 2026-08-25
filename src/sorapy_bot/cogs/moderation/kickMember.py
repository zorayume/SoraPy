import discord
from discord.ext import commands

class KickMember(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)

    async def kick(self, ctx, member = None, reason = None):
        if member.startswith("<@") and member.endswith("<"):
            member_id = member.replace("<@", "").replace("<@!", "").replace(">", "")
        elif member.isdigit():
            member_id = member
        else:
            kickEmbedInfo = discord.Embed(title=f"{ctx.prefix}kick <MEMBER>")

        try:
            member_id = int(member_id)
            target = ctx.guild.get_member(member_id)

            if target == None:
                await ctx.send("Member is not found")
                return
            if target.top_role >= ctx.guild.me.top_role:
                await ctx.send("The role for the user is higher than me. Place me higher than them.")
                return
            if target.id == ctx.author.id:
                await ctx.send("You cannot kick yourself")
                return

            if reason == None:
                reason = "User has violate the rule"

            # await ctx.guild.kick(target, reason=reason)
            embed = discord.Embed(description=f"{target} was kicked", color=discord.Color.green())

        except discord.Forbidden:
            await ctx.send(f"Cannot kick the person. Please check back the permission")
            
async def setup(client):
    await client.add_cog(KickMember(client))