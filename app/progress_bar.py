from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QThread
from dialogs.progress_bar_dialog import Ui_ProgressBarDialog
from downloader_thread import DownloadProgressThread


class ProgessBar(QDialog, Ui_ProgressBarDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Downloading...')
        self.ProgressBar.setMaximum(1000)

        self.progress_updater = DownloadProgressThread()
        self.thread = QThread()
        self.filename = ''

        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.progress_updater.progress.connect(self.update_progress_bar)
        self.progress_updater.done.connect(self.finished)
        self.progress_updater.done.connect(self.thread.quit)
        self.progress_updater.moveToThread(self.thread)
        self.thread.started.connect(self.progress_updater.download)
        self.SuccessButton.clicked.connect(self.close)        

    def start_download(self, data):
        self.reset()
        self.progress_updater.song_data = data  # Just a pass through
        self.filename = data['filename'] + '.' + data['format']
        self.show()
        self.thread.start()

    def update_progress_bar(self, percentage, eta, speed, size):
        self.ProgressLabel.setText(self.filename + '\t' + 'ETA: ' + eta + ', ' + speed + ', ' + size)
        self.ProgressBar.setValue(int(percentage*10))
        self.ProgressBar.setFormat("{:.02f}%".format(percentage))

    def finished(self):
        self.SuccessButton.setEnabled(True)

    def reset(self):
        self.ProgressLabel.setText('')
        self.ProgressBar.setValue(0)
        self.ProgressBar.setFormat("{:.02f}%".format(0))
        self.SuccessButton.setEnabled(False)
