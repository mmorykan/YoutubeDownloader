import os
from PyQt5.QtWidgets import QDialog
from dialogs.progress_bar_dialog import Ui_ProgressBarDialog
from downloader_thread import DownloadProgressThread
from PyQt5.QtCore import pyqtSignal, QMutex


class ProgessBar(QDialog, Ui_ProgressBarDialog):
    """
    Dialog that appears when a download is in progress. 
    This dialog starts a QThread to constantly update a progress bar during a download.
    """

    download_finished = pyqtSignal()
    window_closed = pyqtSignal(int)
    player_lock = QMutex()
    delete_window = QMutex()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Downloading...')
        self.ProgressBar.setMaximum(1000)
        self.data = {}
        self.progress_updater = DownloadProgressThread()
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.progress_updater.moveToThread(self.progress_updater)  # Move progress update class to the QThread
        self.progress_updater.started.connect(self.progress_updater.download)  # Thread starts downloading upon start
        # Connect progress signal pyqtSignal to update progress function
        self.progress_updater.progress.connect(self.update_progress_bar) 
        self.progress_updater.adding_to_player.connect(self.adding_to_player) 
        self.progress_updater.finished.connect(self.finished)  # Signal QThread when to quit

        self.SuccessButton.clicked.connect(self.close)        

    def start_download(self, data):
        """
        Gives progress updater class the user input song data.
        Starts QThread to start downloading.
        """
        self.data = self.progress_updater.song_data = data  # Just a pass through
        self.filename = data['filename'] + '.' + data['format']
        self.setWindowTitle(f'Downloading {self.filename}...')
        self.show()
        self.progress_updater.start()

    def update_progress_bar(self, percentage, display):
        self.ProgressLabel.setText(display)
        self.ProgressBar.setValue(int(percentage*10))
        self.ProgressBar.setFormat("{:.02f}%".format(percentage))
        if percentage > 95:
            self.setWindowTitle(f'Converting {self.filename}...')

    def finished(self):
        self.progress_updater.add_to_player()
        self.SuccessButton.setEnabled(True)
        self.setWindowTitle(f'Downloaded {self.filename}')
        self.player_lock.lock()
        self.download_finished.emit()  # Updates GUI
        self.player_lock.unlock()

    def adding_to_player(self, window_title):
        self.setWindowTitle(window_title)

    def closeEvent(self, event):  # Need to downloader/ffmpeg thread from here
        self.progress_updater.disconnect()
        if self.progress_updater.isRunning():
            self.progress_updater.quit()
            file_ = os.path.join(self.data['path'], self.filename)
            if os.path.exists(file_):
                os.remove(file_)

        self.delete_window.lock()
        self.window_closed.emit(int(self.winId()))
        self.delete_window.unlock()
        event.accept()
