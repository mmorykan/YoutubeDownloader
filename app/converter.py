import os, sys
from subprocess import Popen, PIPE


class Converter:

    def __init__(self, ):
        self.ffmpeg_location = this_script_dir = os.path.dirname(os.path.realpath(__file__))
        if not getattr(sys, 'frozen', False):
            platform = 'windows' if os.name == 'nt' else 'mac'
            self.ffmpeg_location = os.path.join(os.path.dirname(this_script_dir), 'ffmpeg_' + platform, 'bin')

    def convert(self, filenames, format_):
        for filename in filenames:
            args = [os.path.join(self.ffmpeg_location, 'ffmpeg'), '-i', filename, filename.rsplit('.', 1)[0] + '.' + format_]
            print(args)
            proc = Popen(args)
            proc.wait()
