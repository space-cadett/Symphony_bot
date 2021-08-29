import discord
from discord.ext import commands

from symphony import Symphony
import constants


symphony = Symphony()

# client = discord.Client()

client = commands.Bot(command_prefix='$', case_insensitive=True)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(name='hi')
async def hi(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')


@client.command(name='play', description='Play audio from YouTube URL')
async def play(ctx, args):
    videoInfo = symphony.processQueue(args)
    await ctx.send(str(videoInfo))


client.run(constants.TOKEN)
