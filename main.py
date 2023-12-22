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

@client.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        try:
            await channel.connect()
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("You aren't in a voice channel. Please join one to use this command.")

@client.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("I left the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel.")


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
        await client.start("")

asyncio.run(main())

