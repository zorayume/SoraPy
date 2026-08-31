import discord
from discord.ext import commands

class BanMember(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member=discord.Member, * , reason: str = "Rule breaker"):
        
        if member.startswith("<@") and member.endswith(">"):
            member_id = member.replace("<@", "").replace("<@!", "").replace(">", "")
        elif member.isdigit():
            member_id = member
        else:
            banEmbedInfo = discord.Embed(title=f"{ctx.prefix}ban <MEMBER>", description=f"Ban is used to get rid of member out of server")
            banEmbedInfo.add_field(name="MEMBER - id or mentions", value="`!ban <@12345678>` or `!ban 12345678`", inline=True)

            await ctx.send("Invalid member, please use either ID or mention.", embed=banEmbedInfo)
            return

        try:
            member_id = int(member_id)

            target = ctx.guild.get_member(member_id)

            if target.top_role >= ctx.guild.me.top_role:
                await ctx.send("The user's role is higher than mine, please place me on top of that role")
                return

            if target.id == ctx.author.id:
                await ctx.send("You cannot ban yourself")
                return
            
            if reason == None:
                reason = "Rules Breaker"

            # await ctx.guild.ban(target, reason=reason)
            embed = discord.Embed(description=f"Successfully banned {target} with reason: `{reason}`", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send(f"Cannot ban member. You need a permission of ban for me")

    @ban.error
    async def moderation_error(self, ctx, error):
        match error:
            case commands.MissingPermissions():
                await ctx.send("You need the permission of `BanMembers`.")
            case commands.BotMissingPermissions():
                await ctx.send("Cannot ban member. You need a permission of ban for me")
            case commands.MissingRequiredArgument():
                await ctx.send("!ban <MEMBER> <REASON>")
            case commands.MemberNotFound():
                await ctx.send("Member not found")
            

async def setup(client):
    await client.add_cog(BanMember(client))