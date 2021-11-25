import sys, os

# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon
from darktheme.widget_template import DarkPalette
import resources  # Must be imported for resource files such as icons

from dialogs.converter_main_dialog import Ui_MainWindow
from progress_bar import ProgessBar
from file_exists import FileExists
from url_needed import URLNeeded
from info import Info
from invalid_time import InvalidTime
import validators
import time


class Window(QMainWindow, Ui_MainWindow):
    """
    This is the main window for the GUI. It controls execution of all other dialogs as well.
    This class handles all the validation of input from the user.
    There is one instance of all other dialogs in this class.
    Also, this class saves the previously chosen folder in QSettings for convenience the next time the app is run.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.format = 'm4a'  # bestaudio/best' downloads best quality audio/video
        self.progress = ProgessBar()
        self.file_exists = FileExists()
        self.url_needed = URLNeeded()
        self.info = Info()
        self.invalid_time = InvalidTime()
        self.settings = QSettings()
        self.setup_info_button()
        self.restore_settings()
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.DownloadButton.clicked.connect(self.download)
        self.ListFormatButton.clicked.connect(self.list_formats)
        self.FolderButton.clicked.connect(self.choose_path)
        self.FormatList.clicked.connect(self.choose_format)
        self.InfoButton.clicked.connect(self.info.exec)

    def setup_info_button(self):
        self.InfoButton.setStyleSheet('background-color: white')
        self.InfoButton.setIcon(QIcon(':/icons/info.jpg'))
        self.InfoButton.setIconSize(self.InfoButton.size())

    def choose_path(self, _):
        directory = QFileDialog.getExistingDirectory(self, self.tr("Select Directory"), os.path.expanduser('~'),
                                       QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if directory:
            self.FolderText.setText(directory)
            self.save_settings(directory)

    def choose_format(self, index):
        self.format = index.data()

    def download(self):
        url = self.UrlText.text()
        if not self.__is_valid_url(url):
            return
        path = self.FolderText.text()
        start_time = self.StartTimeText.text()
        end_time = self.EndTimeText.text()
        filename = self.FilenameText.text().split('.')[0]  # Split in case user inputs file format on end
        data = self.__get_info(url)
        
        # Default the filename if not entered
        if not filename:
            filename = data['title']

        # Default the path if not entered
        if not path:
            path = os.path.expanduser('~')

        # Format end time if entered
        if end_time:
            end_time = self.__is_valid_time(end_time, data['duration'])
            if not end_time:
                return

        # Format start time if entered
        if start_time:
            start_time = self.__is_valid_time(start_time, (end_time.tm_min * 60 + end_time.tm_sec) if end_time else data['duration'])
            if not start_time:
                return

        full_path = os.path.join(path, filename + '.' + self.format)
        download_info = {'url': url,
                        'title': self.TitleText.text(),
                        'artist': self.ArtistText.text(),
                        'genre': self.GenreText.text(),
                        'start_time': start_time,
                        'end_time': end_time,
                        'full_path': full_path,
                        'filename': filename,
                        'format': self.format}
        if os.path.exists(full_path):  # Ask to overwrite file if it already exists
            self.file_exists.set_message(filename + '.' + self.format)
            self.file_exists.exec()
            if self.file_exists.overwrite_file:
                os.remove(full_path)  # Need this because youtube-dl won't overwrite existing files with same name
                self.progress.start_download(download_info)
        else:
            self.progress.start_download(download_info)
        
        # Clear all fields except folder field
        for field in (self.UrlText, self.TitleText, self.ArtistText, self.GenreText, self.FilenameText, self.StartTimeText, self.EndTimeText):
            field.clear()
        
    def list_formats(self):
        url = self.UrlText.text()
        if not self.__is_valid_url(url):
            return
        data = self.__get_info(url)
        self.FormatList.addItems(data['formats'])

    def __is_valid_url(self, url):
        # If a url is not valid, execute dialog and return False
        if not validators.url(url):
            self.url_needed.exec()
            return False
        return True
    
    def __is_valid_time(self, trim_time, duration):
        # All time is compared in seconds
        try:
            formatted = time.strptime(trim_time, '%M:%S')
        except ValueError:
            self.invalid_time.exec()
            return False

        if duration:
            if (formatted.tm_min * 60 + formatted.tm_sec) < duration:
                return formatted
            else:
                self.invalid_time.exec()
                return False
        else:
            return formatted

    def __get_info(self, url):
        return self.progress.progress_updater.downloader.get_info(url)

    def save_settings(self, directory):
        # Save the chosen directory in QSettings for convenience the next time the app is run
        self.settings.setValue("directory", directory)

    def restore_settings(self):
        # Load the previously chosen folder on startup
        directory = self.settings.value("directory", os.path.expanduser('~'))
        self.FolderText.setText(directory)


if __name__ == "__main__":
    # Create app and set dark theme
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(DarkPalette())

    # Create window and show it
    win = Window()
    win.setWindowTitle("Youtube Downloader")
    win.show()
    sys.exit(app.exec())
