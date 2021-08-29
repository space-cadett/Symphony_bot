from discord.ext import commands
from discord.ext.commands.core import Command

from symphony import Symphony
import utils
import constants

symphony = Symphony()
client = commands.Bot(command_prefix='$', case_insensitive=True)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(name='hi')
async def hi(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')


@client.command(name='join')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command(name='leave')
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.command(name='play', description='Play audio from YouTube URL')
async def play(ctx, args):
    videoInfo = symphony.processQueue(args)[0]
    embeddedMsg = utils.addedToQueueEmbed(videoInfo, ctx.author.avatar_url)
    await ctx.send(embed=embeddedMsg)


@client.command(name='queue', description='Show current queue')
async def queue(ctx):
    # TODO print queue
    pass


@client.command(name='status', description='Print bot status')
async def status(ctx):
    # TODO print bot name, latency, uptime, etc
    pass


client.run(constants.TOKEN)
