import discord
import constants
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event 
async def on_ready():
    print("I am here!")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

client.run(constants.TOKEN)
