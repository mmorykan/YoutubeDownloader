import sys, os

# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtCore import QSettings, Qt
from PyQt5.QtGui import QIcon

from darktheme.widget_template import DarkPalette
from downloader import YoutubeDownloader
import resources  # Must be imported for resource files such as icons

from dialogs.converter_main_dialog import Ui_MainWindow
from progress_bar import ProgessBar
from file_exists import FileExists
from url_needed import URLNeeded
from info import Info
from invalid_time import InvalidTime
from application_doesnt_exist import ApplicationDoesntExist
from converter import Converter
from player_connector import PlayerConnector
from players.iTunesPlayer import iTunesPlayer
from datetime import datetime
import validators

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
        self.file_exists = FileExists()
        self.url_needed = URLNeeded()
        self.info = Info()
        self.invalid_time = InvalidTime()
        self.application_doesnt_exist = ApplicationDoesntExist()
        self.settings = QSettings("Mark Project", "Youtube Downloader")
        self.converter = Converter()
        self.icon = QIcon(f':/icons/{"windows" if os.name == "nt" else "mac"}_app.jpg')
        self.downloads = {}
        self.format = ''
        self.conversion_format = ''
        self.audio_boxes = (self.KeepOriginalAudioBox, self.TrimOriginalAudioBox)
        self.video_boxes = (self.KeepOriginalVideoBox, self.TrimOriginalVideoBox)
        self.player_boxes = {
            self.AddToITunesBox: iTunesPlayer,
        }
        self.player = None
        self.connect_signals_slots()
        self.setup_info_button()
        self.set_icons()
        self.resize_format_list()
        self.restore_settings()

    def connect_signals_slots(self):
        self.DownloadButton.clicked.connect(self.download)
        self.ConvertButton.clicked.connect(self.convert)
        self.FolderButton.clicked.connect(self.choose_path)
        self.ChooseFilesButton.clicked.connect(self.choose_files)
        self.FormatBox.currentTextChanged.connect(self.choose_conversion_format)
        self.FormatList.clicked.connect(self.choose_format)
        self.InfoButton.clicked.connect(self.info.exec)
        self.ClearPlaylistsButton.clicked.connect(lambda: self.clear_metadata_selection(self.PlaylistListWidget))
        self.ClearArtistsButton.clicked.connect(lambda: self.clear_metadata_selection(self.ArtistListWidget))
        self.ClearGenresButton.clicked.connect(lambda: self.clear_metadata_selection(self.GenreListWidget))
        self.ClearAlbumsButton.clicked.connect(lambda: self.clear_metadata_selection(self.AlbumListWidget))
        for player_box in self.player_boxes:
            player_box.clicked.connect(self.connect_player)

    def setup_info_button(self):
        self.InfoButton.setStyleSheet('background-color: white')
        self.InfoButton.setIcon(QIcon(':/icons/info.jpg'))
        self.InfoButton.resize(self.InfoButton.size().width(), self.DownloadButton.size().height())
        self.InfoButton.setIconSize(self.InfoButton.size())

    def set_icons(self):
        for dialog in (self, self.file_exists, self.url_needed, self.info, self.invalid_time, self.application_doesnt_exist):
            dialog.setWindowIcon(self.icon)

    def resize_format_list(self):
        formats = YoutubeDownloader.get_supported_formats()
        self.FormatBox.addItems(formats)
        self.FormatBox.setStyleSheet('combobox-popup: 0')
        self.FormatList.addItems(formats)
        # Extend the width of the list by the width (height) of the scrollbar. The height is 8 rows
        self.FormatList.setFixedSize(self.FormatList.size().width() + self.FormatList.verticalScrollBar().size().height(), self.FormatList.sizeHintForRow(0) * 5)

    def choose_path(self, _):
        directory = QFileDialog.getExistingDirectory(self, self.tr("Select Directory"), self.FolderText.text(),
                                       QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if directory:
            self.FolderText.setText(directory)

    def choose_files(self, _):
        self.FilesList.clear()
        filter_ = ' *.'.join(YoutubeDownloader.get_supported_formats()[1:])
        files, _ = QFileDialog.getOpenFileNames(self, self.tr('Select Files'), os.path.expanduser('~'), 
                                                f'Audio Files ({filter_})')
        if files:
            self.FilesList.addItems(files)
            self.ConvertButton.setEnabled(True)

    def choose_format(self, index):
        self.format = index.data()
        self.change_buttons(self.format in YoutubeDownloader.audio_formats, self.format in YoutubeDownloader.video_formats)

    def choose_conversion_format(self, format_):
        self.conversion_format = format_

    def clear_metadata_selection(self, list_widget):
        for i in range(list_widget.count()):
            list_widget.item(i).setSelected(False)

    def connect_player(self, checked, box=None):
        button = box if box else self.sender()
        player_type = self.player_boxes[button]
        if checked:
            self.player = PlayerConnector(player_type)
            self.player.moveToThread(self.player)
            self.player.started.connect(self.player.connect)
            self.player.finished.connect(self.player.disconnect)
            self.player.not_connected.connect(self.player_not_connected)
            self.player.load_done.connect(self.load_metadata)
            self.player.start()
        elif self.player:
            self.player.quit()
            self.player.wait()
            self.player = None
            for listwidget in (self.PlaylistListWidget, self.ArtistListWidget, self.GenreListWidget, self.AlbumListWidget, self.PlayerLoadingLabel):
                listwidget.clear()

    def player_not_connected(self):
        self.application_doesnt_exist.set_message(self.player.player_type.player_name)
        self.application_doesnt_exist.exec()
        for box, player_type in self.player_boxes.items():
            if player_type == self.player.player_type:
                box.setChecked(False)
                break
        for listwidget in (self.PlaylistListWidget, self.ArtistListWidget, self.GenreListWidget, self.AlbumListWidget):
            listwidget.clear()
        self.player = None

    def load_metadata(self, meta_type, metadata):
        metadata = sorted(list(metadata))
        if meta_type == 'playlists':
            self.PlaylistListWidget.addItems(metadata)
            self.PlayerLoadingLabel.setText("Playlists loaded...")
        elif meta_type == 'artists':
            self.ArtistListWidget.addItems(metadata)
            self.PlayerLoadingLabel.setText("Artists loaded...")
        elif meta_type == 'genres':
            self.GenreListWidget.addItems(metadata)
            self.PlayerLoadingLabel.setText("Genres loaded...")
        elif meta_type == 'albums':
            self.AlbumListWidget.addItems(metadata)
            self.PlayerLoadingLabel.setText("All iTunes Data loaded!")  # Albums is last data to load

    def change_buttons(self, is_audio_format, is_video_format):
        """
        Enable/Disable audio and video checkboxes depending on chosen format.
        """

        for audio_box, video_box in zip(self.audio_boxes, self.video_boxes):
            audio_box.setEnabled(is_audio_format)
            video_box.setEnabled(is_video_format)

    def download(self):
        url = self.UrlText.text().strip()
        if not self.__is_valid_url(url):
            return
        title      = self.TitleText.text().strip()
        artist     = self.ArtistText.text().strip()
        genre      = self.GenreText.text().strip()
        album      = self.AlbumText.text().strip()
        start_time = self.StartTimeText.text().strip()
        end_time   = self.EndTimeText.text().strip()
        path       = self.FolderText.text()
        filename   = self.FilenameText.text().split('.')[0]  # Split in case user inputs file format on end
        progress, data   = self.create_progress_bar(url)

        # Default the filename if not entered
        if not filename:
            filename = title if title else data['title']

        # Format end time if entered
        if end_time:
            end_time_formatted = self.__is_valid_time(end_time, data['duration'])
            if not end_time_formatted:
                return

        # Format start time if entered
        if start_time:
            start_time_formatted = self.__is_valid_time(start_time, (end_time_formatted.minute * 60 + end_time_formatted.second) if end_time else data['duration'])
            if not start_time_formatted:
                return

        metadata = {
                    'title': title,
                    'artist': artist,
                    'genre': genre,
                    'album': album,
                    'playlists': [],
                }

        # Update metadata if iTunes has been connected and selections are made
        if self.player:
            lists = {'artist': self.ArtistListWidget, 
                     'genre': self.GenreListWidget,
                     'album': self.AlbumListWidget,}
            for name, list_widget in lists.items():
                current = list_widget.currentItem()
                if current:
                    metadata[name] = current.text()
            items = self.PlaylistListWidget.selectedItems()
            metadata['playlists'] = [item.text() for item in items]

        # Update the path to include artist and album
        if self.iTunesFormatBox.isChecked():
            if not metadata['artist']:
                metadata['artist'] = 'Unknown Artist'
            if not metadata['album']:
                metadata['album'] = 'Unknown Album'
            path = os.path.join(path, metadata['artist'], metadata['album'])

        download_info = {'url': url,
                        'metadata': metadata,
                        'options': {
                            'keep_original': self.get_checked_and_enabled((self.KeepOriginalAudioBox, self.KeepOriginalVideoBox)),
                            'trim_original': self.get_checked_and_enabled((self.TrimOriginalAudioBox, self.TrimOriginalVideoBox)),
                            # 'audio_and_video': self.get_checked_and_enabled(self.audio_boxes) and self.get_checked_and_enabled(self.video_boxes)
                            'audio_and_video': self.get_checked_and_enabled(self.video_boxes)
                        },
                        'download_options': {
                            'itunes_format': self.iTunesFormatBox.isChecked(),
                            'player': self.player,
                        },
                        'start_time': start_time,
                        'end_time': end_time,
                        'path': path,
                        'filename': filename,
                        'format': self.format}

        if os.path.exists(os.path.join(path, filename + '.' + self.format)):  # Ask to overwrite file if it already exists
            self.file_exists.set_message(filename + '.' + self.format)
            self.file_exists.exec()
            if not self.file_exists.overwrite_file:
                return

        progress.start_download(download_info)

        # Clear all fields except folder field once download starts
        for field in (self.UrlText, self.TitleText, self.ArtistText, self.GenreText, self.AlbumText, self.FilenameText, self.StartTimeText, self.EndTimeText):
            field.clear()

    def create_progress_bar(self, url):
        progress = ProgessBar()
        progress.download_finished.connect(self.download_finished)
        progress.window_closed.connect(self.cleanup_download)
        progress.setWindowIcon(self.icon)
        data = progress.progress_updater.downloader.get_info(url)
        if self.player:
            progress.progress_updater.add_to_library.connect(self.player.add_to_library)
            progress.progress_updater.add_to_playlist.connect(self.player.add_to_playlists)
        self.downloads[int(progress.winId())] = progress
        return progress, data

    def convert(self):
        self.converter.convert([self.FilesList.item(i).text() for i in range(self.FilesList.count())], self.conversion_format)

        self.FilesList.clear()
        self.ConvertButton.setEnabled(False)

    def get_checked_and_enabled(self, boxes):
        """
        Return if any of the checkboxes in boxes are enables and checked.
        """

        return any([box.isEnabled() and box.isChecked() for box in boxes])

    def __is_valid_url(self, url):
        # If a url is not valid, execute dialog and return False
        if not validators.url(url):
            self.url_needed.exec()
            return False
        return True
    
    def __is_valid_time(self, trim_time, duration):
        # All time is compared in seconds
        try:
            formatted = datetime.strptime(trim_time, '%M:%S')
        except ValueError:
            self.invalid_time.exec()
            return False

        if duration:
            if (formatted.minute * 60 + formatted.second) < duration:
                return formatted
            else:
                self.invalid_time.exec()
                return False
        else:
            return formatted

    def download_finished(self):
        """
        Reformat list widgets with correct metadata.
        """
        if self.player:
            lists = {'artists': self.ArtistListWidget,
                     'genres': self.GenreListWidget,
                     'albums': self.AlbumListWidget,}
            for name, list_widget in lists.items():
                meta = getattr(self.player.player, name)
                list_widget.clear()
                list_widget.addItems(sorted(list(meta)))

    def cleanup_download(self, progress_bar_id):
        del self.downloads[progress_bar_id]

    def write_settings(self):
        """
        Save all check boxes, directory, and format in QSettings.
        Only called in closeEvent write before the program terminates.
        """

        boxes = (('keep_audio', self.KeepOriginalAudioBox), ('trim_audio', self.TrimOriginalAudioBox),
                 ('keep_video', self.KeepOriginalVideoBox), ('trim_video', self.TrimOriginalVideoBox),
                 ('itunes_format', self.iTunesFormatBox),)
        for key, box in boxes:
            self.settings.setValue(key, box.isChecked())

        self.settings.setValue('directory', self.FolderText.text())
        self.settings.setValue('format_row', self.FormatList.currentRow())
        self.settings.setValue('conversion_format', self.FormatBox.currentText())

    def restore_settings(self):
        """
        Loads the previously chosen downloads folder, format, and checkbox settings.
        Only called in constructor when program is run.
        """

        directory = self.settings.value('directory', os.path.expanduser('~'), str)
        self.FolderText.setText(directory)
        row = self.settings.value('format_row', self.FormatList.indexFromItem(self.FormatList.findItems('mp3', Qt.MatchExactly)[0]).row(), int)
        self.FormatList.setCurrentRow(row)
        self.format = self.FormatList.item(row).text()
        
        self.conversion_format = self.settings.value('conversion_format', 'mp3', str)
        self.FormatBox.setCurrentText(self.conversion_format)

        format_boxes = (('keep_audio', self.KeepOriginalAudioBox), ('trim_audio', self.TrimOriginalAudioBox),
                 ('keep_video', self.KeepOriginalVideoBox), ('trim_video', self.TrimOriginalVideoBox),
                 ('itunes_format', self.iTunesFormatBox))

        for key, box in format_boxes:
            box.setChecked(self.settings.value(key, False, bool))

        self.ConvertButton.setEnabled(False)

        self.change_buttons(self.format in YoutubeDownloader.audio_formats, self.format in YoutubeDownloader.video_formats)

    def closeEvent(self, event):
        """
        Remember to save all settings in QSettings upon termination.
        Only called when the main window is closed.
        """

        self.write_settings()
        if self.player:
            self.player.quit()
            self.player.wait()
        event.accept()


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
