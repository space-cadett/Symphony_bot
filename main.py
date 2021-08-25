import discord
from discord.ext import commands

import constants

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print("I am here!")


@client.command()
async def hello(ctx):
    await ctx.send("Hi")

client.run(constants.TOKEN)
