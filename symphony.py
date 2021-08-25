import youtube_dl

import constants


class Symphony:
    def __init__(self):
        ydlOpts = {'format': 'bestaudio/best'}
        self.ytdl = youtube_dl.YoutubeDL(ydlOpts)

    def audioStreamByURL(self, url: str) -> str:
        # Returns audio stream url
        videoInfo = self.ytdl.extract_info(url, download=False)
        streamURL = videoInfo['formats'][0]['urls']
        return streamURL


if __name__ == "__main__":
    symphony = Symphony()
    info = symphony.audioStreamByURL(constants.TEST_YT_URL)
    print(info)
