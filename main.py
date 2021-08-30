import sys
import time

from discord.ext import commands
from discord import FFmpegOpusAudio

from symphony import Symphony
import utils
import constants

symphony = Symphony()
client = commands.Bot(command_prefix='$', case_insensitive=True)
startTime = time.time()

FFMpegOptions = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command(name='hi', aliases=['hello'])
async def hi(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')


@client.command(name='join')
async def join(ctx):
    authorChannel = ctx.author.voice
    if authorChannel is not None:
        await authorChannel.channel.connect()
    else:
        await ctx.send('You are not connected to a voice channel')


@client.command(name='leave')
async def leave(ctx):
    currentChannel = ctx.voice_client
    if currentChannel is not None:
        await currentChannel.disconnect()


@client.command(name='play', description='Play audio from YouTube URL')
async def play(ctx, args):
    currentChannel = ctx.voice_client

    if currentChannel is not None:
        videoInfo = symphony.processQueue(args)[0]
        embeddedMsg = utils.addedToQueueEmbed(videoInfo, ctx.author.avatar_url)
        await ctx.send(embed=embeddedMsg)

        currentChannel.play(
            FFmpegOpusAudio(videoInfo['streamURL'], **FFMpegOptions))
    else:
        await join(ctx)
        if ctx.voice_client is None:
            return
        else:
            await play(ctx, args)


@client.command(name='queue', description='Show current queue')
async def queue(ctx):
    # TODO print queue
    pass


@client.command(name='status', aliases=['echo', 'test'],
                description='Print bot status')
async def status(ctx):
    # TODO print bot name, latency, uptime, etc
    pass


@client.command(name='shutdown')
async def shutdown(ctx):
    # Check if admins, sys.exit()
    pass


try:
    client.run(constants.TOKEN)
except KeyboardInterrupt:
    sys.exit()
