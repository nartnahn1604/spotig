from utils.cloudinary_config import *

class Song():
    def __init__(self, id, song_name, artist_name, author_name, album_name, genre, song_url, song_thumb):
        self.id = id
        self.song_name = song_name
        self.artist_name = artist_name
        self.author_name = author_name
        self.album_name = album_name
        self.genre = genre
        self.song_url = song_url
        self.song_thumb = song_thumb
    
    