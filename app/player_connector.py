from PyQt5.QtCore import QThread, pyqtSignal

class PlayerConnector(QThread):

    not_connected = pyqtSignal()
    load_done = pyqtSignal(str, set)

    def __init__(self, player_type=None):
        super().__init__()
        self.player = player_type()
        self.metadata = (
            ('playlists', self.player.get_playlists),
            ('artists', self.player.get_artists),
            ('genres', self.player.get_genres),
            ('albums', self.player.get_albums),
        )

    def connect(self):
        if not self.player.connect():
            self.not_connected.emit()
        else:
            for meta_type, meta_data in self.metadata:
                self.load_done.emit(meta_type, meta_data())

    def disconnect(self):
        self.player.disconnect()

    def add_to_library(self, track):
        self.player.add_to_library(track)

    def add_to_playlists(self, playlists, track):
        for playlist in playlists:
            self.player.add_to_playlist(playlist, track)
