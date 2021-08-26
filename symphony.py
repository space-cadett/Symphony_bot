import youtube_dl

import constants


class Symphony:
    def __init__(self):
        ydlOpts = {
            'format': '251/250/249/bestaudio',
            'quiet': True}
        self.ytdl = youtube_dl.YoutubeDL(ydlOpts)

        self.queue = []

    def processQueue(self, url):
        videoInfo = self.ytdl.extract_info(url, download=False)

        if '_type' in videoInfo:
            for entry in videoInfo['entries']:
                self.__processVideo(entry)
        else:
            self.__processVideo(videoInfo)

        return self.queue

    def __processVideo(self, videoDict: dict) -> None:
        # Gets OPUS audio streams for discord.py
        audioOpusFormat = []

        for audioFormat in videoDict['formats']:
            if audioFormat['acodec'] == 'opus':
                audioOpusFormat.append(audioFormat)

        audioOpusFormat = sorted(
            audioOpusFormat, key=lambda k: k['format_id'], reverse=True)

        title = videoDict['title']
        pageURL = videoDict['webpage_url']
        streamURL = audioOpusFormat[0]['url']
        durationInSec = videoDict['duration']
        thumbnailURL = videoDict['thumbnail']

        videoInfo = {
            'title': title,
            'pageURL': pageURL,
            'streamURL': streamURL,
            'durationInSec': durationInSec,
            'thumbnailURL': thumbnailURL
        }

        self.queue.append(videoInfo)


if __name__ == "__main__":
    symphony = Symphony()
    ytVid = symphony.processQueue(constants.TEST_YT_URL)
    print(ytVid)
