from cloudinary import *
# import sys
# print(sys.path)
from utils.dbHelper import *

def getSongs():
    song_list = get_all_songs()
    return song_list

def getSongsByArtists(id):
    song_list = get_songs_by_artist(id)
    return song_list

def getArtists():
    artist_list = get_all_artists()
    return artist_list

def addUser(access_token):
    add_user(access_token)

def getUser(access_token):
    get_user(access_token)
