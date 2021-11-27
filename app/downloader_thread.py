from PyQt5.QtCore import QThread, pyqtSignal
from downloader import YoutubeDownloader


class DownloadProgressThread(QThread):
    """
    A class that represents a QThread that constantly updates the progress bar upon download.
    This class contains one instance of YoutubeDownloader and adds its own progress method as the progess hook
    Also, we use pyqtSignals to be able to emit data back to the main thread so that the main thread can update the GUI.
    """

    # These must be class variables outside the constructor
    progress = pyqtSignal(float, str, str, str)
    done = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.song_data = {}
        self.downloader = YoutubeDownloader()
        self.downloader.youtube_downloader.add_progress_hook(self.progress_bar)
        
    def download(self):
        self.downloader.download(self.song_data)

    def progress_bar(self, song):
        if song['status'] != 'finished':
            total = song.get('_total_bytes_estimate_str', song.get('_total_bytes_str', ''))
            self.progress.emit(float(song['_percent_str'][:-1]), song['_eta_str'], song['_speed_str'], total)
        else:
            self.done.emit()
