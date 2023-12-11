import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import asyncio

client = commands.Bot(command_prefix= "!", intents = discord.Intents.all())

bot_status = cycle(["Type !helpme for list of commands."])

@tasks.loop(seconds= 5)
async def change_status():
    await client.change_presence(activity = discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print("success: Bot is connected to Discord")
    change_status.start()

#@client.command(help= "Returns the bots latency.")
#async def ping(ctx):
 #   bot_latency = round(client.latency * 1000)
  #  await ctx.send(f"Pong! {bot_latency} ms.")

@client.command(aliases = ["8Ball", "8ball","eightball", "magicball"], help = "Ask the Magic 8Ball a question.")
async def magic_eightball(ctx, *, question):
    with open("C:/Users/saman/Desktop/dcbot/responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)

    await ctx.send(response)

@client.command(help = "Rolls a D20")
async def dice_roll(ctx):
    dice_nums = (["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20",])
    dice_result = random.choice(dice_nums)
    await ctx.send(f"You rolled: {dice_result}!")

@client.command(help = "Enter a name and find out if they're naughty or nice!")
async def norn(ctx, *, question):
    naughty_nice = ([" is Naughty! :(", " is Nice! :)", " is nice! :)", " is Naughty! :("]) 
    if question == "jace":
        await ctx.send("Jace is naughty.")
    else:
        norn_ans = random.choice(naughty_nice)
        await ctx.send(question + norn_ans)

@client.command(help ="Shows a list of available commands.")
async def helpme(ctx):
    command_list = [(command.name, command.help) for command in ctx.bot.commands]
    formatted_commands = "\n".join([f"{name}: {description}" for name, description in command_list])
    await ctx.send(f"Here are all available commands: \n ```\n{formatted_commands}\n```")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")

async def main():
    async with client:
        await load()
        await client.start("MTE3NDkzMzUzMDA0MDU5ODYyOQ.Gbv1Xa.1o6wCcmyrquikSOUPsIHhP4Bqj-vvKeEQuPxbY")

asyncio.run(main())