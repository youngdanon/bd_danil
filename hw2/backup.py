import json


def write_backup_file(path, artists, albums, musics, users, playlists):
    json_db_dump = {"db": {
        "artists": {},
        "albums": {},
        "musics": {},
        "users": {},
        "playlists": {}
    }}
    for artist in artists:
        obj_attr = artist.__dict__
        json_db_dump["db"]["artists"][obj_attr.pop("id")] = obj_attr
    for music in musics:
        obj_attr = music.__dict__
        json_db_dump["db"]["musics"][obj_attr.pop("id")] = obj_attr
    for album in albums:
        obj_attr = album.__dict__
        json_db_dump["db"]["albums"][obj_attr.pop("id")] = obj_attr
    for user in users:
        obj_attr = user.__dict__
        json_db_dump["db"]["users"][obj_attr.pop("id")] = obj_attr
    for playlist in playlists:
        obj_attr = playlist.__dict__
        json_db_dump["db"]["playlists"][obj_attr.pop("id")] = obj_attr

    with open(path, "w") as file:
        json.dump(json_db_dump, file, ensure_ascii=False, indent=4)