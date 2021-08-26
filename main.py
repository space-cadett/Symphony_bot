import discord
from discord.ext import commands

from symphony import Symphony
import constants

client = commands.Bot(command_prefix=">")

symphony = Symphony()


@client.event
async def on_ready():
    print("I am here!")


@client.command()
async def play(ctx, args):
    videoInfo = symphony.processQueue(args)
    await ctx.send(str(videoInfo))

client.run(constants.TOKEN)
