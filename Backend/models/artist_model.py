from utils.cloudinary_config import *

class Artist():
    def __init__(self, id, artist_name, artist_avt,  artist_bio, num_of_songs):
        self.id = id
        self.artist_name =artist_name
        self.artist_bio = artist_bio
        self.artist_avt = artist_avt
        self.num_of_songs = num_of_songs
