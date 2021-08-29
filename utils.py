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
    hours = timeInSeconds // 3600
    minutes = (timeInSeconds % 3600) // 60
    seconds = timeInSeconds % 60

    if hours == 0:
        return f'{minutes}:{seconds}'
    else:
        return f'{hours}:{minutes}:{seconds}'
