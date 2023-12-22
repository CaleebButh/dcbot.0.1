import discord
from discord.ext import commands
import random
from itertools import cycle

class Norn(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Norn.py is ready!")

    @commands.command(help = "Enter a name and find out if they're naughty or nice!")
    async def norn(self, ctx, *, question):
        naughty_nice = ([" is Naughty! :(", " is Nice! :)", " is nice! :)", " is Naughty! :("]) 
        if question == "jace":
            await ctx.send("Jace is naughty.")
        else:
            norn_ans = random.choice(naughty_nice)
        await ctx.send(question + norn_ans)

    @norn.error
    async def norn_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Add a name please.")
            
async def setup(client):
    await client.add_cog(Norn(client))