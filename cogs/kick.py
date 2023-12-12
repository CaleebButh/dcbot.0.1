import discord
from discord.ext import commands
import random
from itertools import cycle

class Kick(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Kick.py is ready!")

    
    @commands.command("kicks a member specified by you")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, modreason):
        if modreason is None:
            modreason = "No reason provided"
        try:
            await ctx.guild.kick(member, reason=modreason)

            conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
            conf_embed.add_field(name="Kicked:", value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.", inline=False)
            conf_embed.add_field(name="Reason:", value=modreason, inline=False)

            await ctx.send(embed=conf_embed)
        except discord.Forbidden:
            await ctx.send("I do not have permission to kick this member.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(client):
    await client.add_cog(Kick(client))