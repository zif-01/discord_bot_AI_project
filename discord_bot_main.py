import discord
import os
from discord.ext import commands
import time
from youtube_dl import YoutubeDL
import nest_asyncio 
nest_asyncio.apply()
from musicnn.tagger import top_tags

YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

client = commands.Bot(command_prefix='-', intents=discord.Intents.all())


@client.command()
async def play(ctx, *, arg):
    vc = await ctx.message.author.voice.channel.connect()
    for file in os.listdir():
        if file.endswith('.mp3'):
            os.remove('song.mp3')
    with YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.download([arg])
        for file in os.listdir():
            if file.endswith('.mp3'):
                os.rename(file, 'song.mp3')
        info = ydl.extract_info(arg, download=False)

    url = info['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=url, **FFMPEG_OPTIONS))

    @client.command()
    async def save():
        from musicnn.tagger import top_tags
        a = []
        a = top_tags('song.mp3', model='MTT_musicnn', topN=10)
        with open(f"{info['song_title']}.txt", "w") as f:
            f.write(str(url))
            for s in a:
                f.write(str(s) + "\n")


@client.command()
async def playlist(ctx, *, arg):
    vc = await ctx.message.author.voice.channel.connect()
    for file in os.listdir():
        if file.endswith('.txt'):
            name = os.path.basename(file)
            f1 = open(name, 'r')
            lines = f1.readlines()
            for line in lines:
                if line == arg:
                    url = f1.readline(0)
                    with YoutubeDL(YDL_OPTIONS) as ydl:
                        info = ydl.extract_info(url, download=False)
                        tm = info['duration']
                        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=url, **FFMPEG_OPTIONS))
                        time.sleep(tm)


client.run("my token :)")
