from PyQt5.QtCore import QThread, pyqtSignal
from downloader import YoutubeDownloader


class DownloadProgressThread(QThread):

    # These must be class variables outside the constructor
    progress = pyqtSignal(float, str, str, str)
    done = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.song_data = {}
        self.downloader = YoutubeDownloader()
        self.downloader.ydl_opts['progress_hooks'] = [self.progress_bar]  # Send callback function to youtube-dl for progress reports during download
        
    def download(self):
        self.downloader.download(self.song_data)

    def progress_bar(self, song):
        if song['status'] != 'finished':
            self.progress.emit(float(song['_percent_str'][:-1]), song['_eta_str'], song['_speed_str'], song['_total_bytes_str'])
        else:
            self.done.emit()
