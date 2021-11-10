from __future__ import unicode_literals
import youtube_dl
from pydub import AudioSegment


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

        self.__trim_audio(data)

    @staticmethod
    def get_info(url):
        with youtube_dl.YoutubeDL({'nocheckcertificate': True}) as ydl:
            meta = ydl.extract_info(url, download=False)
            print(meta)
        return {
            'formats': {format['ext'] for format in meta['formats']}, 
            'title': meta['title'], 
            'duration': meta['duration'] 
            }

    def __trim_audio(self, data):
        start, end = data['start_time'], data['end_time']
        audio = AudioSegment.from_file(self.ydl_opts['outtmpl'], self.ydl_opts['format'])
        if start and end:
            print('slicing both')
            start_time = (start.tm_min * 60 + start.tm_sec) * 1000
            end_time = (end.tm_min * 60 + end.tm_sec) * 1000
            audio = audio[start_time:end_time]
        elif start:
            print('slicing start')
            start_time = (start.tm_min * 60 + start.tm_sec) * 1000
            audio = audio[start_time:]
        elif end:
            print('slicinge end')
            end_time = (end.tm_min * 60 + end.tm_sec) * 1000
            audio = audio[:end_time]
        audio.export(self.ydl_opts['outtmpl'], tags={'title': data['title'], 'artist': data['artist'], 'genre': data['genre']})
        # audio.export('test.m4a', tags={'title': data['title'], 'artist': data['artist'], 'genre': data['genre']})
