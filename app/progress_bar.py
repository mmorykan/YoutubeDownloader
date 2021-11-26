from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QThread
from dialogs.progress_bar_dialog import Ui_ProgressBarDialog
from downloader_thread import DownloadProgressThread


class ProgessBar(QDialog, Ui_ProgressBarDialog):
    """
    Dialog that appears when a download is in progress. 
    This dialog starts a QThread to constantly update a progress bar during a download.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Downloading...')
        self.ProgressBar.setMaximum(1000)

        self.progress_updater = DownloadProgressThread()
        self.thread = QThread()
        self.filename = ''

        self.connect_signals_slots()

    def connect_signals_slots(self):
        # Connect progress signal pyqtSignal to update progress function
        self.progress_updater.progress.connect(self.update_progress_bar)  
        self.progress_updater.done.connect(self.finished)  # Signal QThread when to quit
        self.progress_updater.moveToThread(self.thread)  # Move progress update class to the QThread
        self.thread.started.connect(self.progress_updater.download)  # Thread starts downloading upon start
        self.SuccessButton.clicked.connect(self.close)        

    def start_download(self, data):
        """
        Gives progress updater class the user input song data.
        Starts QThread to start downloading.
        """
        
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
        self.thread.quit()
        self.thread.wait()  # Waits for the thread to terminate after being quit

    def reset(self):
        self.ProgressLabel.setText('')
        self.ProgressBar.setValue(0)
        self.ProgressBar.setFormat("{:.02f}%".format(0))
        self.SuccessButton.setEnabled(False)
