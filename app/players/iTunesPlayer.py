
import win32com.client
import pythoncom
class iTunesPlayer:

    player_name = 'iTunes'

    def __init__(self):
        self.player = None
        self.main_playlist = None
        self.excluded_playlists = {'Library', 'Music', 'Movies', 'TV Shows', 'Podcasts', 'Audiobooks', 'Genius'}
        self.excluded_info = {'', ' '}
        self.playlists = set()
        self.artists = set()
        self.genres = set()
        self.albums = set()

    def get_playlists(self, reload: bool=False) -> set[str]:
        if not self.playlists or reload:
            playlists = self.player.LibrarySource.Playlists
            self.playlists = {playlist.Name for playlist in playlists if playlist.Name not in self.excluded_playlists}
        return self.playlists

    def get_artists(self, reload: bool=False) -> set[str]:
        if not self.artists or reload:
            self.artists = {track.Artist for track in self.main_playlist.Tracks if track.Artist not in self.excluded_info}
        return self.artists

    def get_genres(self, reload: bool=False) -> set[str]:
        if not self.genres or reload:
            self.genres = {track.Genre for track in self.main_playlist.Tracks if track.Genre not in self.excluded_info}
        return self.genres

    def get_albums(self, reload: bool=False) -> set[str]:
        if not self.albums or reload:
            self.albums = {track.Album for track in self.main_playlist.Tracks if track.Album not in self.excluded_info}
        return self.albums

    def add_to_playlist(self, playlist: str, filename: str ) -> None:
        playlists = self.player.LibrarySource.Playlists
        playlist = playlists.ItemByName(playlist)
        playlist.AddFile(filename)

    def add_to_library(self, filename: str) -> None:
        self.main_playlist.AddFile(filename)

    def connect(self) -> bool:
        try:
            self.player = win32com.client.Dispatch('iTunes.application', pythoncom.CoInitialize())
        except pythoncom.com_error:
            return False
        self.main_playlist = self.player.LibraryPlaylist
        return True

    def disconnect(self) -> None:
        try:
            self.player.Quit()
        except:
            pass
