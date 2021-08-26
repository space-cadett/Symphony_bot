import discord

from symphony import Symphony
import constants


symphony = Symphony()

# client = discord.Client()

<<<<<<< HEAD

@client.command()
async def play(ctx, args):
    videoInfo = symphony.processQueue(args)
    await ctx.send(str(videoInfo))
=======
client = commands.Bot(command_prefix='$', case_insensitive=True)
>>>>>>> 7c0818593279054b35534f6dd13c03a898ab0b07


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
