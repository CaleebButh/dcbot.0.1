import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import asyncio
import yt_dlp

client = commands.Bot(command_prefix= "!", intents = discord.Intents.all())

bot_status = cycle(["Type !helpme for list of commands."])

# ytdl_format_options = {
#     'format': 'bestaudio/best',
#     'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
#     'restrictfilenames': True,
#     'noplaylist': True,
#     'nocheckcertificate': True,
#     'ignoreerrors': False,
#     'logtostderr': False,
#     'quiet': True,
#     'no_warnings': True,
#     'default_search': 'auto',
#     'source_address': '0.0.0.0'
# }

# ffmpeg_options = {
#     'options': '-vn'
# }

# ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

# class YTDLSource(discord.PCMVolumeTransformer):
#     def __init__(self, source, *, data, volume=0.5):
#         super().__init__(source, volume)
#         self.data = data
#         self.title = data.get('title')
#         self.url = data.get('url')

#     @classmethod
#     async def from_url(cls, url, *, loop=None, stream=False):
#         loop = loop or asyncio.get_event_loop()
#         data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

#         if 'entries' in data:
#             # Take first item from a playlist
#             data = data['entries'][0]

#         filename = data['url'] if stream else ytdl.prepare_filename(data)
#         return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

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
async def HEY(ctx):
    await ctx.send("HO!")

@client.command(name='join', help='Joins a voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel.")
        return

    channel = ctx.message.author.voice.channel

    if ctx.voice_client is not None:
        await ctx.voice_client.move_to(channel)
    else:
        await channel.connect()

    await ctx.send(f"Joined {channel}")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('!play'):
#         await play_music(message)

# async def play_music(message):
#     if not message.author.voice:
#         await message.channel.send("You are not connected to a voice channel.")
#         return

#     voice_channel = message.author.voice.channel
#     if voice_channel is not None:
#         song = message.content[len('!play '):].strip()
#         if message.guild.voice_client is None:
#             await voice_channel.connect()
#         else:
#             await message.guild.voice_client.move_to(voice_channel)

#         # Play the song
#         async with message.channel.typing():
#             player = await YTDLSource.from_url(song, loop=client.loop, stream=True)
#             message.guild.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

#         await message.channel.send(f'🎶 Now playing: **{player.title}**')

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
        await client.start("MTE3NDkzMzUzMDA0MDU5ODYyOQ.GPPwvi.bkS5Ry_K3GcImDzgmAMzJFl8JLc-HKKDUdSgQk")

asyncio.run(main())

