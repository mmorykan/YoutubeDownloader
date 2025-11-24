import os
import sys
import subprocess

from sim.updater import update
from updater_thread import UpdateProgressThread

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from dialogs.progress_bar_dialog import Ui_ProgressBarDialog

class ApplicationUpdater(QDialog, Ui_ProgressBarDialog):
    """
    This class is used to check GitHub for the most recent release of this application and begin updating.
    This class should only be instantiated at startup of the application. It will use a separate thread to download
    the most recent release. Once downloaded, this process will be terminated and overwritten with the new version,
    then restarted.
    """

    GITHUB_USER = "mmorykan"
    GITHUB_REPO = "YoutubeDownloader"

    window_closed = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Updating Application...')
        self.ProgressBar.setValue(0)
        self.ProgressBar.setMaximum(100)
        self.progress_updater = None
        self.setWindowIcon(QIcon(f':/icons/{"windows" if os.name == "nt" else "mac"}_app.jpg'))
        self.debug_mode = int(not getattr(sys, 'frozen', False))

    def get_exe_paths(self):
        paths = {
            'temp': 'update_temp.exe',
            'current': 'Youtube_Downloader.exe',
            'updater': 'App_Updater.exe',
        }
        if self.debug_mode:
            prefix = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
            paths['temp'] = os.path.join(prefix, "dist", paths['temp'])
            paths['current'] = os.path.join(prefix, "dist", paths['current'])
            paths['updater'] = os.path.join("py", prefix, "updater", "updater.py")

        return paths

    def check_for_updates(self):
        paths = self.get_exe_paths()
        temp_path = paths['temp']

        url = f"https://api.github.com/repos/{ApplicationUpdater.GITHUB_USER}/{ApplicationUpdater.GITHUB_REPO}/releases/latest"
        self.progress_updater = UpdateProgressThread(url, temp_path)

        self.progress_updater.moveToThread(self.progress_updater)  # Move progress update class to the QThread
        self.progress_updater.started.connect(self.progress_updater.download)  # Thread starts downloading upon start
        # Connect progress signal pyqtSignal to update progress function
        self.progress_updater.progress.connect(self.update_progress_bar)
        self.progress_updater.finished.connect(self.finished)  # Signal QThread when to quit

        self.SuccessButton.clicked.connect(self.close)

        self.progress_updater.start()

    def update_progress_bar(self, percentage):
        self.ProgressLabel.setText("Updating Application... The application will restart automatically after installation")
        self.ProgressBar.setValue(int(percentage))
        if percentage > 95:
            self.setWindowTitle(f'Installing...')

    def finished(self, no_update):
        if no_update:
            print("Skipping the update")
            self.close()
            return

        print("download finished")
        self.SuccessButton.setEnabled(True)
        self.setWindowTitle('Update Complete')

        # Launch updater.exe to replace running EXE
        paths = self.get_exe_paths()
        current_exe = paths['current'] # sys.argv[0] in production
        temp_path = paths['temp']

        if self.debug_mode:
            update(current_exe, temp_path, int(self.debug_mode))
        else:
            subprocess.Popen([paths['updater'], current_exe, temp_path, str(self.debug_mode)])

            print("Updating... restarting.")
            sys.exit(0)

    def closeEvent(self, event):
        if self.progress_updater and self.progress_updater.isRunning():
            self.progress_updater.quit()

        self.window_closed.emit(int(self.winId()))
        event.accept()

def main():
    updater = ApplicationUpdater()
    updater.check_for_updates()

    print("App running normally...")
    input("Press enter to quit...")

if __name__ == "__main__":
    main()
