from __future__ import unicode_literals
from posixpath import abspath
from yt_dlp import YoutubeDL, FFmpegExtractAudioPP, FFmpegVideoConvertorPP
from download_logger import Logger
import os, sys
from subprocess import Popen


class YoutubeDownloader:
    """
    This class contains a single YoutubeDL instance from yt-dlp that downloads audio/video from a youtube url. 
    Also adds metadata to the downloaded file and trims it.
    """
    
    def __init__(self):
        # If the app running in a bundled state, we may need absolute paths to find the ffmpeg binaries
        self.ffmpeg_location = this_script_dir = os.path.dirname(os.path.realpath(__file__))
        if not getattr(sys, 'frozen', False):
            platform = 'windows' if os.name == 'nt' else 'mac'
            self.ffmpeg_location = os.path.join(os.path.dirname(this_script_dir), 'ffmpeg_' + platform, 'bin')

        self.ext = 'webm'
        self.rejected_formats = {'mka'}
        self.video_formats, self.audio_formats = (set(FFmpegVideoConvertorPP.SUPPORTED_EXTS) - self.rejected_formats, set(FFmpegExtractAudioPP.SUPPORTED_EXTS))
        self.audio_only, self.audio_and_video = (('bestaudio/best', FFmpegExtractAudioPP), ('best', FFmpegVideoConvertorPP))
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
        Downloads the youtube audio and possibly video given the format, output path, and postprocessor arguments.
        Modifies the original file downloaded before postprocessing if the user wants it.
        Removes the youtube_dl cache upon every download to not get a 403 forbidden error 
        because cachedir option may not work yet.
        """

        keep_original_video = data['keep_video'] or data['trim_video']
        self.youtube_downloader.params['keepvideo'] = keep_original_video
        self.youtube_downloader.params['outtmpl'] = os.path.join(data['path'], data['filename'] + '.%(ext)s')
        self.youtube_downloader.outtmpl_dict = self.youtube_downloader.parse_outtmpl()  # Check yt-dlp __init__ for YoutubeDL.py 
        metadata_args = self.get_metadata_args(data['metadata'])
        self.youtube_downloader.params['postprocessor_args'] = self.get_trim_video_args(data['start_time'], data['end_time']) + metadata_args

        format_, post_processor_class = self.get_format_and_postprocessor(data['format'], data['audio_and_video'])

        self.youtube_downloader.format_selector = self.youtube_downloader.build_format_selector(format_)
        self.youtube_downloader.add_post_processor(post_processor_class(self.youtube_downloader, data['format']))

        self.youtube_downloader.cache.remove()
        self.youtube_downloader.download([data['url']])            

        if keep_original_video:
            self.modify_original(self.youtube_downloader.params['postprocessor_args'] if data['trim_video'] else metadata_args, data['path'], data['filename'], data['format'])

    def get_format_and_postprocessor(self, chosen_format, audio_and_video):
        """
        Returns the downloaded format of the video along with the audio or video post processor.
        """

        if chosen_format in self.video_formats and chosen_format in self.audio_formats:
            format_, post_processor_class = self.audio_and_video if audio_and_video else self.audio_only
        else:
            format_, post_processor_class = self.audio_and_video if chosen_format in self.video_formats else self.audio_only

        return format_, post_processor_class

        
    def get_info(self, url):
        """
        Returns a set of the title and duration of the video.
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
        Add trimming times to a list for postprocessing.
        """

        trim_args = []
        if start and end:
            trim_args = ['-ss', start, '-to', end]
        elif start:
            trim_args = ['-ss', start]
        elif end:
            trim_args = ['-ss', '00:00:00', '-to', end]

        return trim_args

    def modify_original(self, postprocessor_args, path, filename, format_):
        """
        If the user wants to keep the originally downloaded file before post processing,
        we can apply all post processing to the original file as well.
        """

        if format_ == self.ext:
            current_file = os.path.join(path, filename + '.' + self.ext)
            renamed_file = current_file.replace('.', '_original.')
            os.rename(current_file, renamed_file)
            
            self.run_ffmpeg(renamed_file, current_file, self.youtube_downloader.params['postprocessor_args'])

            filename = renamed_file.rsplit('.', 1)[0]

        current_file = os.path.join(path, filename + '.' + self.ext)
        output_file = current_file.replace('.', '_edited.')  # Temp file to be written to and replaced
        
        self.run_ffmpeg(current_file, output_file, postprocessor_args)

        os.replace(output_file, current_file)

    def run_ffmpeg(self, current_file, output_file, postprocessor_args):

        proc = Popen([os.path.join(self.ffmpeg_location, 'ffmpeg'), '-i', current_file] + \
                        postprocessor_args + \
                        ['-c', 'copy', output_file])
        proc.wait()

    def progress(self, song):
        """
        Progress hook upon downloading. Only used for getting the file extension of best quality video.
        """

        if song['status'] == 'finished':
            self.ext = song['info_dict']['ext']

    def get_supported_formats(self):
        """
        Returns a list of all supported formats without duplicates, and then a set of the duplicates.
        Have to use a list for all formats in order to preserve order when displayed in the GUI.
        """

        formats = FFmpegExtractAudioPP.SUPPORTED_EXTS + FFmpegVideoConvertorPP.SUPPORTED_EXTS
        return ([format_ for pos, format_ in enumerate(formats) if not (format_ in self.rejected_formats or format_ in formats[:pos])], 
                self.video_formats.intersection(self.audio_formats))
