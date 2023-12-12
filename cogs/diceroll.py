import discord
from discord.ext import commands
import random
from itertools import cycle

class Dice_roll(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("DiceRoll.py is ready!")

    @commands.command(help = "Rolls a D20")
    async def dice_roll(self,ctx):
        dice_nums = (["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20",])
        dice_result = random.choice(dice_nums)
        await ctx.send(f"You rolled: {dice_result}!")
async def setup(client):
    await client.add_cog(Dice_roll(client))