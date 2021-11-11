from __future__ import unicode_literals
from youtube_dl import YoutubeDL
from pydub import AudioSegment
from download_logger import Logger


class YoutubeDownloader():
    """
    This class contains a single YoutubeDL instance that downloads audio from videos, 
    gets info from them, and trims the audio file after download
    """

    def __init__(self):
        self.youtube_downloader = YoutubeDL({
                                            'extractaudio': True,
                                            'noplaylist': True,
                                            'nocheckcertificate': True,
                                            'cachedir': False,
                                            'logger': Logger(),
                                            })

    def download(self, data):
        """
        Downloads the youtube audio given the format and output path.
        Removes the youtube_dl cache upon every download to not get a 403 forbidden error 
        because youtube_dl has no convenient option for this yet.
        """

        # Sets the format and download path in the YoutubeDL object
        self.youtube_downloader.params['format'] = data['format']
        self.youtube_downloader.params['outtmpl'] = data['full_path']

        # Must run youtube-dl --rm-cache-dir on command line when 403 error or YoutubeDL().cache.remove() in python
        self.youtube_downloader.cache.remove()
        self.youtube_downloader.download([data['url']])

    def get_info(self, url):
        """
        Returns a set of the formats of the url, as well as the title and duration of the video 
        """

        meta = self.youtube_downloader.extract_info(url, download=False)
        return {
            'formats': {format['ext'] for format in meta['formats']}, 
            'title': meta['title'], 
            'duration': meta['duration'] 
            }

    def trim_audio(self, data):
        """
        Trims the audio from a just downloaded file if a start time or end time as been specified.
        All times have been converted to milliseconds to work with pydub for audio slicing.
        Saves the newly trimmed file with the specified metadata.
        """

        start, end = data['start_time'], data['end_time']
        audio = AudioSegment.from_file(data['full_path'], data['format'])
        if start and end:
            start_time = (start.tm_min * 60 + start.tm_sec) * 1000
            end_time = (end.tm_min * 60 + end.tm_sec) * 1000
            audio = audio[start_time:end_time]
        elif start:
            start_time = (start.tm_min * 60 + start.tm_sec) * 1000
            audio = audio[start_time:]
        elif end:
            end_time = (end.tm_min * 60 + end.tm_sec) * 1000
            audio = audio[:end_time]
        audio.export(data['full_path'], tags={'title': data['title'], 'artist': data['artist'], 'genre': data['genre']})
 
    def add_progress_hook(self, hook):
        """
        Adds a callback function hook to the downloader so user can receive progress updates
        """

        self.youtube_downloader.add_progress_hook(hook)
