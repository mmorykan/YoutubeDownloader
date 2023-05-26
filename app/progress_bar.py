import os
from PyQt5.QtWidgets import QDialog
from dialogs.progress_bar_dialog import Ui_ProgressBarDialog
from downloader_thread import DownloadProgressThread


class ProgessBar(QDialog, Ui_ProgressBarDialog):
    """
    Dialog that appears when a download is in progress. 
    This dialog starts a QThread to constantly update a progress bar during a download.
    """

    def __init__(self, on_finished, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Downloading...')
        self.ProgressBar.setMaximum(1000)
        self.data = {}
        self.on_finished = on_finished
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

    def start_download(self, data):  # Change this (make onclose event)
        """
        Gives progress updater class the user input song data.
        Starts QThread to start downloading.
        """

        self.reset()
        self.data = self.progress_updater.song_data = data  # Just a pass through
        self.filename = data['filename'] + '.' + data['format']
        self.show()
        self.progress_updater.start()

    def update_progress_bar(self, percentage, eta, speed, size):
        self.ProgressLabel.setText((self.filename if len(self.filename) < 40 else self.filename[:40] + '... ') + '\t' + 'ETA: ' + eta + ', ' + speed + ', ' + size)
        self.ProgressBar.setValue(int(percentage*10))
        self.ProgressBar.setFormat("{:.02f}%".format(percentage))
        if percentage > 95:
            self.setWindowTitle('Converting...')

    def finished(self):
        self.progress_updater.add_to_player()
        self.SuccessButton.setEnabled(True)
        self.setWindowTitle('Download Complete')
        self.on_finished(self)

    def adding_to_player(self, window_title):
        self.setWindowTitle(window_title)

    def reset(self):
        self.ProgressLabel.setText('')
        self.ProgressBar.setValue(0)
        self.ProgressBar.setFormat("{:.02f}%".format(0))
        self.SuccessButton.setEnabled(False)
        self.setWindowTitle('Downloading...')

    def closeEvent(self, event):  # Need to downloader/ffmpeg thread from here
        self.progress_updater.disconnect()
        if self.progress_updater.isRunning():
            self.progress_updater.quit()
            file_ = os.path.join(self.data['path'], self.filename)
            if os.path.exists(file_):
                os.remove(file_)

        event.accept()
