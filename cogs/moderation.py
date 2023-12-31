import discord
from discord.ext import commands
import random
from itertools import cycle

class Moderation(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is ready!")

    @commands.command(help = "Clears a number of previous messages specified by you.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,count: int):
        await ctx.channel.purge(limit=count)
        await ctx.send(f"{count} messages have been purged.")

    @commands.command(help = "bans member of your choosing")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.ban(member)

        conf_embed=discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Banned:",value=f"{member.mention} has been banned from the server by {ctx.author.mention}.")
        conf_embed.add_field(name="Reason:", value=modreason, inline=False)

        await ctx.send(embed=conf_embed)

    @commands.command(help="unbans member")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)

        conf_embed=discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Unbanned:",value=f"@{userId} has been unbanned from the server by {ctx.author.mention}.")

        await ctx.send(embed=conf_embed)

    @clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing number of messages you wish to clear.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Shouldnt have to ask this... Who are we banning? (tag someone)")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who are we unbanning man, tag them.")

async def setup(client):
    await client.add_cog(Moderation(client))