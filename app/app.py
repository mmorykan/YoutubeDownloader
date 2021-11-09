import sys, os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QIcon
from darktheme.widget_template import DarkPalette
import resources

from converter_main_dialog import Ui_MainWindow
from downloader import YoutubeDownloader
from progress_bar_dialog import ProgessBarDialog
from file_exists_dialog import FileExists
from url_needed import URLNeeded
from info import Info
import validators


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.format = 'm4a'  # self.format = 'bestaudio/best'
        self.progress = ProgessBarDialog()
        self.file_exists = FileExists()
        self.url_needed = URLNeeded()
        self.info = Info()
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
        
        _, title = YoutubeDownloader.list_formats_and_title(url)
        filename = self.FilenameText.text().split('.')[0]
        if not filename:
            filename = title

        path = self.FolderText.text()
        if not path:
            path = os.path.expanduser('~')
        
        full_path = os.path.join(path, filename + '.' + self.format)
        if os.path.exists(full_path):
            self.file_exists.set_message(filename + '.' + self.format)
            self.file_exists.exec()
            if self.file_exists.overwrite_file:
                os.remove(full_path)  # Need this because youtube-dl won't overwrite existing files with same name
                self.progress.start_download({'url': url,
                                              'title': self.TitleText.text(),
                                              'artist': self.ArtistText.text(),
                                              'genre': self.GenreText.text(),
                                              'start_time': self.StartTimeText.text(),
                                              'end_time': self.EndTimeText.text(),
                                              'full_path': full_path,
                                              'filename': filename,
                                              'format': self.format})
        
    def list_formats(self):
        if not self.__is_valid_url():
            return
        url = 'https://youtu.be/8-y-8cyt-3U' # Remove this line
        formats, _ = YoutubeDownloader.list_formats_and_title(url)
        self.FormatList.addItems(formats)

    def __is_valid_url(self):
        url = self.UrlText.text()
        if not validators.url(url):
            self.url_needed.exec()
            return False
        return True

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
