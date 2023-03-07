
import win32com.client
import pythoncom

class iTunesPlayer:

    player_name = 'iTunes'

    def __init__(self, player):
        self.player = player
        self.excluded_playlists = {'Library', 'Music', 'Movies', 'TV Shows', 'Podcasts', 'Audiobooks', 'Genius'}
        self.main_playlist = self.player.LibraryPlaylist
        self.main_library = self.player.LibrarySource
        self.exluded_info = {'', ' '}

    def get_playlists(self) -> list[str]:
        mainLibrary = self.player.LibrarySource
        playlists = mainLibrary.Playlists
        
        return sorted([playlist.name for playlist in playlists if playlist.name not in self.excluded_playlists])

    def get_artists(self):
        artists = {track.Artist for track in self.main_playlist.Tracks}
        artists.difference_update(self.exluded_info)
        return sorted(list(artists))

    def get_genres(self):
        genres = {track.Genre for track in self.main_playlist.Tracks}
        genres.difference_update(self.exluded_info)
        return sorted(list(genres))

    def get_albums(self):
        albums = {track.Album for track in self.main_playlist.Tracks}
        albums.difference_update(self.exluded_info)
        return sorted(list(albums))

    def add_to_playlist(self, playlist, filename):
        playlists = self.main_library.Playlists
        playlist = playlists.ItemByName(playlist)
        playlist.AddFile(filename)

    def add_to_library(self, filename):
        print(filename)
        self.main_playlist.AddFile(filename)

    @classmethod
    def connect(cls):
        try:
            itunes = win32com.client.Dispatch('iTunes.application', pythoncom.CoInitialize())
        except pythoncom.com_error:
            return False

        return cls(itunes)

    def disconnect(self):
        try:
            self.player.Quit()
        except:
            pass
