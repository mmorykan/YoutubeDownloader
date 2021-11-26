from __future__ import unicode_literals
from yt_dlp import YoutubeDL
from download_logger import Logger
import os, sys


class YoutubeDownloader():
    """
    This class contains a single YoutubeDL instance from yt-dlp that downloads audio from videos, 
    gets info from them, and trims the audio file after download
    """

    def __init__(self):
        # If the app running in a bundled state, we may need absolute paths to find the ffmpeg binaries
        this_script_dir = os.path.dirname(os.path.realpath(__file__))
        platform = 'windows' if os.name == 'nt' else 'mac'
        if getattr(sys, 'frozen', False):
            ffmpeg_location = this_script_dir
        else:
            ffmpeg_location = os.path.join(os.path.dirname(this_script_dir), 'ffmpeg_' + platform, 'bin')

        self.youtube_downloader = YoutubeDL({
                                            # 'ffmpeg_location': ffmpeg_location,
                                            'extractaudio': True,
                                            'noplaylist': True,
                                            'nocheckcertificate': True,
                                            'cachedir': False,
                                            'logger': Logger(),
                                            'postprocessors': [{
                                                'key': 'FFmpegExtractAudio',
                                                }],
                                            'overwrites': True
                                            })

    def download(self, data):
        """
        Downloads the youtube audio given the format and output path.
        Removes the youtube_dl cache upon every download to not get a 403 forbidden error 
        because cachedir may not work yet.
        """

        # Sets the format and download path in the YoutubeDL object
        self.youtube_downloader.params['outtmpl'] = data['full_path']
        self.youtube_downloader.outtmpl_dict = self.youtube_downloader.parse_outtmpl()  # Check yt-dlp __init__ for YoutubeDL.py
        self.youtube_downloader.format_selector = self.youtube_downloader.build_format_selector(data['format'])  # Check yt-dlp __init__ for YoutubeDL.py
        self.add_metadata(data)

        # Must run yt-dlp --rm-cache-dir on command line when 403 error or YoutubeDL().cache.remove() in python
        self.youtube_downloader.cache.remove()
        self.youtube_downloader.download([data['url']])

    def get_info(self, url):
        """
        Returns a set of the formats of the url, as well as the title and duration of the video 
        """

        meta = self.youtube_downloader.extract_info(url, download=False)
        return {
            'formats': {format['ext'] for format in meta['formats']} - {'webm'}, 
            'title': meta['title'], 
            'duration': meta['duration'] 
            }

    def add_metadata(self, data):
        """
        Determines the post processor arguments for the youtube downloader.
        Trims the audio of the video and adds metadata to the file.
        """

        postprocessor_args = []
        start, end = data['start_time'], data['end_time']
        if start and end:
            postprocessor_args = ['-ss', start, '-to', end]
        elif start:
            postprocessor_args = ['-ss', start]
        elif end:
            postprocessor_args = ['-ss', '00:00', '-to', end]

        for metadata in ('title', 'artist', 'genre'):
            if data[metadata]:
                postprocessor_args += ['-metadata', f'{metadata}={data[metadata]}']

        self.youtube_downloader.params['postprocessor_args'] = postprocessor_args

    def add_progress_hook(self, hook):
        """
        Adds a callback function hook to the downloader so user can receive progress updates
        """

        self.youtube_downloader.add_progress_hook(hook)
