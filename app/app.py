import sys, os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon
from darktheme.widget_template import DarkPalette
import resources  # Must be imported for resource files such as icons

from dialogs.converter_main_dialog import Ui_MainWindow
from progress_bar import ProgessBar
from file_exists import FileExists
from downloader import YoutubeDownloader
from url_needed import URLNeeded
from info import Info
from invalid_time import InvalidTime
import validators
import time


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.format = 'm4a'  # self.format = 'bestaudio/best'
        self.progress = ProgessBar()
        self.file_exists = FileExists()
        self.url_needed = URLNeeded()
        self.info = Info()
        self.invalid_time = InvalidTime()
        self.settings = QSettings()
        self.InfoButton.setStyleSheet('background-color: white')
        self.InfoButton.setIcon(QIcon(':/icons/info.jpg'))
        self.InfoButton.setIconSize(self.InfoButton.size())
        self.restore_settings()
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.DownloadButton.clicked.connect(self.download)
        self.ListFormatButton.clicked.connect(self.list_formats)
        self.FolderButton.clicked.connect(self.choose_path)
        self.FormatList.clicked.connect(self.choose_format)
        self.InfoButton.clicked.connect(self.info.exec)

    def choose_path(self, x):
        directory = QFileDialog.getExistingDirectory(self, self.tr("Select Directory"), os.path.expanduser('~'),
                                       QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if directory:
            self.FolderText.setText(directory)
            self.save_settings(directory)

    def choose_format(self, index):
        self.format = index.data()

    def download(self):
        if not self.__is_valid_url():
            return
        url = 'https://youtu.be/8-y-8cyt-3U' # Remove this line
        path = self.FolderText.text()
        start_time = self.StartTimeText.text()
        end_time = self.EndTimeText.text()
        filename = self.FilenameText.text().split('.')[0]  # Split in case user inputs file format on end
        data = YoutubeDownloader.get_info(url)
        
        # Default the filename
        if not filename:
            filename = data['title']

        # Default the path
        if not path:
            path = os.path.expanduser('~')

        # Check end time
        if end_time:
            end_time = self.__is_valid_time(end_time, data['duration'])
            if not end_time:
                return

        # Check start time
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
                        'format': self.format,
                        }
        if os.path.exists(full_path):
            self.file_exists.set_message(filename + '.' + self.format)
            self.file_exists.exec()
            if self.file_exists.overwrite_file:
                os.remove(full_path)  # Need this because youtube-dl won't overwrite existing files with same name
                self.progress.start_download(download_info)
        else:
            self.progress.start_download(download_info)
        
    def list_formats(self):
        if not self.__is_valid_url():
            return
        url = 'https://youtu.be/8-y-8cyt-3U' # Remove this line
        data = YoutubeDownloader.get_info(url)
        self.FormatList.addItems(data['formats'])

    def __is_valid_url(self):
        url = self.UrlText.text()
        if not validators.url(url):
            self.url_needed.exec()
            return False
        return True
    
    def __is_valid_time(self, trim_time, duration):
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

    def save_settings(self, directory):
        self.settings.setValue("directory", directory)

    def restore_settings(self):
        directory = self.settings.value("directory")
        self.FolderText.setText(directory)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(DarkPalette())

    win = Window()
    win.setWindowTitle("Youtube Downloader")
    win.show()
    sys.exit(app.exec())
