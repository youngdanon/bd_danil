import itertools


class Artist:
    id_iter = itertools.count()

    def __init__(self, name, desc):
        self.id = next(Artist.id_iter)
        self.name = name
        self.desc = desc


class Album:
    id_iter = itertools.count()

    def __init__(self, name, artist_id, music_ids, release_date):
        self.id = next(Album.id_iter)
        self.name = name
        self.artist_id = artist_id
        self.music_ids = music_ids
        self.release_date = release_date
        self.listening_counter = 0


class Music:
    id_iter = itertools.count()

    def __init__(self, name, artist_id, length, release_date):
        self.id = next(Music.id_iter)
        self.name = name
        self.artist_id = artist_id
        self.length = length
        self.release_date = release_date
        self.listening_counter = 0


class User:
    id_iter = itertools.count()

    def __init__(self, nickname, login, password, favorite_artists):
        self.id = next(User.id_iter)
        self.nickname = nickname
        self.login = login
        self.password = password
        self.favorite_artists = favorite_artists
        self.playlists_ids = []

    def add_playlist(self, playlist_id):
        self.playlists_ids.append(playlist_id)


class Playlist:
    id_iter = itertools.count()

    def __init__(self, name, desc, user):
        self.id = next(Playlist.id_iter)
        self.name = name
        self.desc = desc
        self.music_ids = []
        self.length = 0.0
        self.user_id = user.id
        user.add_playlist(self.id)

    def add_music(self, music):
        self.music_ids.append(music.id)
        self.length += music.length