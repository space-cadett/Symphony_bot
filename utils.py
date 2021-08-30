import datetime

import discord


def addedToQueueEmbed(videoInfo: dict, authorPicURL: str):
    embed = discord.Embed(
        title=videoInfo['title'],
        url=videoInfo['pageURL'],
        color=0x252525)

    embed.set_author(name='Added to Queue', icon_url=authorPicURL)
    embed.set_thumbnail(url=videoInfo['thumbnailURL'])

    embed.add_field(
        name='Channel', value=videoInfo['channelName'], inline=True)
    embed.add_field(
        name='Song Duration',
        value=__formatTime(videoInfo['durationInSec']), inline=True)

    return embed


def spotifySongName():
    # TODO Return list of song names from spotify link
    pass


def __formatTime(timeInSeconds: int) -> str:
    timeStr = str(datetime.timedelta(seconds=timeInSeconds))
    time = timeStr.split(':')

    if time[0] == '0':
        return ':'.join(time[1:])
    else:
        return ':'.join(time)
