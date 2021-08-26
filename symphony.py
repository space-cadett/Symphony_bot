import youtube_dl

import constants


class Symphony:
    def __init__(self):
        ydlOpts = {
            'format': 'bestaudio',
            'quiet': True}
        self.__ytdl = youtube_dl.YoutubeDL(ydlOpts)

        self.__queue = []

    def processQueue(self, url: str) -> list:
        videoInfo = self.__ytdl.extract_info(url, download=False)

        if '_type' in videoInfo:
            for entry in videoInfo['entries']:
                self.__processVideo(entry)
        else:
            self.__processVideo(videoInfo)

        shallowCopy = self.__queue.copy()
        self.__queue.clear()
        return shallowCopy

    def __processVideo(self, videoDict: dict) -> None:
        # Gets OPUS audio streams for discord.py
        audioOpusFormat = []

        for audioFormat in videoDict['formats']:
            try:
                # YT Streams
                if audioFormat['acodec'] == 'opus':
                    audioOpusFormat.append(audioFormat)
            except KeyError:
                # Soundcloud Streams
                if audioFormat['ext'] == 'opus':
                    audioOpusFormat.append(audioFormat)

        audioOpusFormat = sorted(
            audioOpusFormat, key=lambda k: k['abr'], reverse=True)

        title = videoDict['title']
        description = videoDict['description']
        channelName = videoDict['uploader']
        pageURL = videoDict['webpage_url']
        streamURL = audioOpusFormat[0]['url']
        durationInSec = videoDict['duration']
        thumbnailURL = videoDict['thumbnail']

        videoInfo = {
            'title': title,
            'description': description,
            'channelName': channelName,
            'pageURL': pageURL,
            'streamURL': streamURL,
            'durationInSec': durationInSec,
            'thumbnailURL': thumbnailURL
        }

        self.__queue.append(videoInfo)


if __name__ == "__main__":
    symphony = Symphony()
    queue = symphony.processQueue(constants.TEST_YT_URL)
    # queue = symphony.processQueue(constants.TEST_SC_URL)
    print(queue)
