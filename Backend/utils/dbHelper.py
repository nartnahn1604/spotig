import cx_Oracle
from utils.get_config import getConfig
from utils.cloudinary_config import *
from utils.get_track import *
from models.song_model import Song
from models.author_model import Author
from models.artist_model import Artist
from models.album_model import Album
from models.genre_model import Genre


class OracleConnection:
    def __init__(self, username, password, host, port, sid, role):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.sid = sid
        self.role = role
        self.connection = None

    def connect(self):
        try:
            if self.role == 'SYSDBA':
                mode = cx_Oracle.SYSDBA
            elif self.role == 'SYSOPER':
                mode = cx_Oracle.SYSOPER
            else:
                raise ValueError('Invalid role specified.')

            dsn = cx_Oracle.makedsn(self.host, self.port, sid=self.sid)
            self.connection = cx_Oracle.connect(self.username, self.password, dsn, mode=mode)
            print('Connected to Oracle database as', self.role)

        except cx_Oracle.DatabaseError as e:
            print('Error while connecting to Oracle database:', e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print('Disconnected from Oracle database.')

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result

        except cx_Oracle.DatabaseError as e:
            print('Error executing query:', e)
    
    def call_func(self, func_name, args = None, type = None):
        try:
            cursor = self.connection.cursor()
            results_cursor = ''
            if args != None:
                results_cursor = cursor.callfunc(func_name, cx_Oracle.CURSOR, [args])
            else:
                results_cursor = cursor.callfunc(func_name, cx_Oracle.CURSOR)
            results = results_cursor.fetchall()
            cursor.close()
            return results
        except cx_Oracle.DatabaseError as e:
            print('Error executing query:', e)
    
    def call_procedure(self, procedure_name, args):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(procedure_name, [args])
        except cx_Oracle.DatabaseError as e:
            print('Error executing query:', e)


# Usage example:
# Create an instance of OracleConnection and connect as SYS with the SYSDBA role
config_db = getConfig()

connection = OracleConnection(config_db['username'], config_db['password'], config_db['host'], config_db['port'], config_db['sid'], config_db['role'])
connection.connect()

edit_img = 'c_fill,g_face,w_300,h_300,r_max/'

def get_all_songs():
    # Execute a query
    song_list = []
    result = connection.call_func('get_songs')
    for row in result:
        # print(row)
        song = Song(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        # song.song_url = get_song_url(song.song_url)
        # song.song_thumb = create_img_url(edit_img, song.song_thumb)
        song_list.append(song)
    return song_list

def get_songs_by_artist(id):
    song_list = []
    result = connection.call_func('GET_SONGS_BY_ARTIST', id, cx_Oracle.NUMBER)
    for row in result:
        # print(row)
        song = Song(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        # song.song_url = get_song_url(song.song_url)
        song.song_thumb = create_img_url(edit_img, song.song_thumb)
        song_list.append(song)
    return song_list

def get_all_artists():
    artist_list = []
    result = connection.call_func('get_artists')
    for row in result:
        artist = Artist(row[0], row[1], row[2], row[3], row[4])
        # artist.artist_avt = create_img_url(edit_img, artist.artist_avt)
        artist_list.append(artist)
    return artist_list

def add_user(access_token):
    connection.call_procedure('add_user', access_token)

def get_user(access_token):
    result = connection.call_func('get_user', access_token, str)
    return result[0]

