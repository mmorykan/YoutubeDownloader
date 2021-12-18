from __future__ import unicode_literals
from yt_dlp import YoutubeDL, FFmpegExtractAudioPP, FFmpegVideoConvertorPP, postprocessor
from download_logger import Logger
import os, sys
from subprocess import Popen


class YoutubeDownloader:
    """
    This class contains a single YoutubeDL instance from yt-dlp that downloads audio from videos, 
    gets info from them, and trims the audio file after download
    """
    
    def __init__(self):
        # If the app running in a bundled state, we may need absolute paths to find the ffmpeg binaries
        self.ffmpeg_location = this_script_dir = os.path.dirname(os.path.realpath(__file__))
        if not getattr(sys, 'frozen', False):
            platform = 'windows' if os.name == 'nt' else 'mac'
            self.ffmpeg_location = os.path.join(os.path.dirname(this_script_dir), 'ffmpeg_' + platform, 'bin')

        self.ext = 'webm'
        self.video_formats = set(FFmpegVideoConvertorPP.SUPPORTED_EXTS) - {'mka'}
        self.youtube_downloader = YoutubeDL({
                                            'ffmpeg_location': self.ffmpeg_location,  # Need path to ffmpeg
                                            'noplaylist': True,
                                            'nocheckcertificate': True,
                                            'cachedir': False,
                                            'logger': Logger(),
                                            'overwrites': True,
                                            'progress_hooks': [self.progress]
                                            })

    def download(self, data):
        """
        Downloads the youtube audio given the format and output path.
        Removes the youtube_dl cache upon every download to not get a 403 forbidden error 
        because cachedir option may not work yet.
        """

        self.youtube_downloader.params['keepvideo'] = data['keep_video'] or data['trim_video']
        self.youtube_downloader.params['outtmpl'] = os.path.join(data['path'], data['filename'] + '.%(ext)s')
        self.youtube_downloader.outtmpl_dict = self.youtube_downloader.parse_outtmpl()  # Check yt-dlp __init__ for YoutubeDL.py 
        metadata_args = self.get_metadata_args(data['metadata'])
        self.youtube_downloader.params['postprocessor_args'] = self.get_trim_video_args(data['start_time'], data['end_time']) + metadata_args

        # Need better code here
        if data['audio_and_video']:
            format_ = 'best'
            preferred_format = data['format'] if data['format'] in self.video_formats else 'mp4'
            post_processor = FFmpegVideoConvertorPP(self.youtube_downloader, preferedformat=preferred_format)
        else:
            format_ = 'bestaudio/best'
            post_processor = FFmpegExtractAudioPP(self.youtube_downloader, preferredcodec=data['format'])

        self.youtube_downloader.format_selector = self.youtube_downloader.build_format_selector(format_)
        self.youtube_downloader.add_post_processor(post_processor)

        self.youtube_downloader.cache.remove()
        self.youtube_downloader.download([data['url']])

        if data['keep_video'] or data['trim_video']:
            if data['trim_video']:
                args = self.youtube_downloader.params['postprocessor_args']
            elif data['keep_video']:
                args = metadata_args
            self.modify_original(args, data['path'], data['filename'])
        
    def get_info(self, url):
        """
        Returns a set of the formats of the url, as well as the title and duration of the video 
        """

        meta = self.youtube_downloader.extract_info(url, download=False)
        return {
            'title': meta['title'], 
            'duration': meta['duration'] 
            }

    def get_metadata_args(self, metadata):
        """
        Add metadata arguments to a list for postprocessing.
        """

        metadata_args = []
        for metadata_type in ('title', 'artist', 'genre'):
            if metadata[metadata_type]:
                metadata_args += ['-metadata', f'{metadata_type}={metadata[metadata_type]}']

        return metadata_args

    def get_trim_video_args(self, start, end):
        """
        Add trimming times to a list for postprocessing
        """

        trim_args = []
        if start and end:
            trim_args = ['-ss', start, '-to', end]
        elif start:
            trim_args = ['-ss', start]
        elif end:
            trim_args = ['-ss', '00:00:00', '-to', end]

        return trim_args

    def modify_original(self, postprocessor_args, path, filename):
        """
        If the user wants to keep the originally downloaded file before post processing because it is in better format,
        we apply all post processing to the original file as well.
        """

        current_file = os.path.join(path, filename + '.' + self.ext)
        output_file = os.path.join(path, filename + '_edited.' + self.ext)  # Temp file to be written to and renamed
        proc = Popen([os.path.join(self.ffmpeg_location, 'ffmpeg'), '-i', current_file] + \
                        postprocessor_args + \
                        ['-c', 'copy', output_file])
        proc.wait()
        os.replace(output_file, current_file)

    def progress(self, song):
        """
        Progress hook upon downloading. Only used for getting the file extension of best quality video
        """

        if song['status'] == 'finished':
            self.ext = song['info_dict']['ext']

    @staticmethod
    def get_supported_formats():
        # Cannot use sets here because order will change when displayed in the GUI
        formats = FFmpegExtractAudioPP.SUPPORTED_EXTS + FFmpegVideoConvertorPP.SUPPORTED_EXTS
        return [format_ for pos, format_ in enumerate(formats) if format_ not in formats[:pos]]
