import discord
from discord.ext import commands
import random
import asyncio
import os
from itertools import cycle

class Eightball(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Eightball.py is ready!")

    @commands.command(aliases = ["8Ball", "8ball","eightball", "magicball"], help = "Ask the Magic 8Ball a question.")
    async def magic_eightball(ctx, *, question):
        with open("C:/Users/saman/Desktop/dcbot/responses.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)
        await ctx.send(response)
async def setup(bot):
    await bot.add_cog(Eightball(bot))