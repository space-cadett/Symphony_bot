import discord
from discord import player
from discord.ext import commands
from discord.ext.commands import bot


from symphony import Symphony
import constants

symphony = Symphony()

client = discord.Client()

#client = commands.Bot(command_prefix="$")


@client.command()
async def play(ctx, args):
    videoInfo = symphony.processQueue(args)
    await ctx.send(str(videoInfo))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Hello!')


client.run(constants.TOKEN)
