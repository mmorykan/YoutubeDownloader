from __future__ import unicode_literals
import youtube_dl
from mutagen.easymp4 import EasyMP4


class MyLogger(object):
    def debug(self, msg):
        print('debug', msg)

    def warning(self, msg):
        print('warning', msg)

    def error(self, msg):
        print('error', msg)


class YoutubeDownloader():

    def __init__(self):
        self.ydl_opts = {
            'extractaudio': True,
            'noplaylist': True,
            'addmetadata': True,
            'logger': MyLogger(),
            'nocheckcertificate': True,
            'cachedir': False,
        }

    # Must run youtube-dl --rm-cache-dir when 403 error
    def download(self, data):

        self.ydl_opts['format'] = data['format']
        self.ydl_opts['outtmpl'] = data['full_path']

        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([data['url']])

        self.__add_metadata(data)

    @staticmethod
    def list_formats_and_title(url):
        with youtube_dl.YoutubeDL({'nocheckcertificate': True}) as ydl:
            meta = ydl.extract_info(url, download=False)
            
        return {format['ext'] for format in meta['formats']}, meta['title']

    def __add_metadata(self, data):
        metatag = EasyMP4(self.ydl_opts['outtmpl'])
        for name in ('title', 'artist', 'genre'):
            if data[name]:
                metatag[name] = data[name]
        metatag.save()