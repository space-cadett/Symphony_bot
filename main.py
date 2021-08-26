import discord

from symphony import Symphony
import constants


symphony = Symphony()

client = discord.Client()


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
