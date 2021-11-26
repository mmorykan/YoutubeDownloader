from __future__ import unicode_literals
from yt_dlp import YoutubeDL
# from pydub import AudioSegment, utils
from download_logger import Logger
import os, sys


class YoutubeDownloader():
    """
    This class contains a single YoutubeDL instance from yt-dlp that downloads audio from videos, 
    gets info from them, and trims the audio file after download
    """

    def __init__(self):
        # If the app running in a bundled state, we must use absolute paths to find the ffmpeg binaries
        this_script_dir = os.path.dirname(os.path.realpath(__file__))
        ext, plat = ('.exe', 'windows') if os.name == 'nt' else ('', 'mac')
        if getattr(sys, 'frozen', False):
            # utils.get_prober_name = lambda: os.path.join(this_script_dir, 'ffprobe' + ext)
            # AudioSegment.converter = os.path.join(this_script_dir, 'ffmpeg' + ext)
            ffmpeg_location = this_script_dir
        else:
            # utils.get_prober_name = lambda: os.path.join(os.path.dirname(this_script_dir), 'ffmpeg_'+plat, 'bin', 'ffprobe' + ext)
            # AudioSegment.converter = os.path.join(os.path.dirname(this_script_dir), 'ffmpeg_'+plat, 'bin', 'ffmpeg' + ext)
            ffmpeg_location = os.path.join(os.path.dirname(this_script_dir), 'ffmpeg_'+plat, 'bin')

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
        because youtube_dl has no convenient option for this yet.
        """

        # Sets the format and download path in the YoutubeDL object
        self.youtube_downloader.params['outtmpl'] = data['full_path']
        self.youtube_downloader.format_selector = self.youtube_downloader.build_format_selector(data['format'])
        self.youtube_downloader.outtmpl_dict = self.youtube_downloader.parse_outtmpl()

        self.add_metadata(data)

        # Must run youtube-dl --rm-cache-dir on command line when 403 error or YoutubeDL().cache.remove() in python
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

    # def trim_audio(self, data):
    #     """
    #     Trims the audio from a just downloaded file if a start time or end time as been specified.
    #     All times have been converted to milliseconds to work with pydub for audio slicing.
    #     Saves the newly trimmed file with the specified metadata.
    #     """
    #     start, end = data['start_time'], data['end_time']
    #     try: 
    #         audio = AudioSegment.from_file(data['full_path'])
    #     except Exception as e:
    #         with open(os.path.expanduser('~')+'/error.txt', 'a') as f:
    #             f.write(f'{data["full_path"]}{AudioSegment.converter} line 61: {e}')
    #     try:
    #         if start and end:
    #             audio = audio[self.__convert_time(start):self.__convert_time(end)]
    #         elif start:
    #             audio = audio[self.__convert_time(start):]
    #         elif end:
    #             audio = audio[:self.__convert_time(end)]
    #     except Exception as e:
    #         with open(os.path.expanduser('~')+'/error.txt', 'a') as f:
    #             f.write(f'error line 75: {e}')
    #     try:
    #         audio.export(data['full_path'], tags={'title': data['title'], 'artist': data['artist'], 'genre': data['genre']})
    #     except Exception as e:
    #         with open(os.path.expanduser('~')+'/error.txt', 'a') as f:
    #             f.write('line 81 '+str(e))

    def add_metadata(self, data):

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

    # def __convert_time(self, time):
    #     """
    #     converts time object to milliseconds
    #     """
        
    #     return (time.tm_min * 60 + time.tm_sec) * 1000

