import discord
from discord.ext import commands
import random
import asyncio
import os
from itertools import cycle

class Eightball(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Eightball.py is ready!")

    @commands.command(aliases = ["8Ball", "8ball","eightball", "magicball"], help = "Ask the Magic 8Ball a question.")
    async def magic_eightball(self,ctx, *, question):
        try:
            with open("responses.txt", "r") as f:
                random_responses = f.readlines()
                response = random.choice(random_responses).strip() 
            await ctx.send(response)
        except FileNotFoundError:
            await ctx.send("Could not find the responses file.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
async def setup(client):
    await client.add_cog(Eightball(client))