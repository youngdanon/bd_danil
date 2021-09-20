from objects import *
from backup import *

artists, albums, musics, users, playlists = [], [], [], [], []
artists.append(Artist("Николай Басков", "*description*"))
musics.append(Music("Чаша золотая", 0, 4.52, "2010-01-10"))
albums.append(Album("Чаша золотая", 0, 0, "2010-01-10"))

artists.append(Artist("Morgenstern", "desc"))
musics.append(Music("Я съел деда", 1, 3.28, "2020-01-10"))
albums.append(Album("Легендарная пыль", 1, 1, "2020-01-10"))

users.append(User("Danil", "youngdanon", "qwertyuiop", [0, 1]))
playlists.append(Playlist("Liked music", "i love this shit", users[0]))
playlists[0].add_music(musics[0])
playlists[0].add_music(musics[1])

write_backup_file("backup.json", artists, albums, musics, users, playlists)