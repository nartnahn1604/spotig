from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
from flask.helpers import get_flashed_messages
import json
import requests
from controller.home import *
from models.song_model import Song
from utils.get_track import *
app = Flask(__name__)
app.secret_key = 'ssss'

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'CALLBACK_URL'

# Authorization endpoint URL
AUTH_URL = 'https://accounts.spotify.com/authorize'

# Token endpoint URL
TOKEN_URL = 'https://accounts.spotify.com/api/token'

# Scopes for accessing user data
SCOPES = 'user-read-private user-read-email user-read-playback-state user-modify-playback-state streaming'

@app.route('/')
def index():
    songs = getSongs()
    artists = getArtists()

    flag = dict(session)
    try:
        if flag['flag']:
            for song in songs:
                song.song_url = get_song_url(song.song_url, flag['access token'])
            session['flag'] = False
            return render_template('index.html', songs=songs, artists=artists)
    except:
            session['flag'] = False

    
    auth_params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPES
    }
    auth_url = f"{AUTH_URL}?{'&'.join(f'{k}={v}' for k, v in auth_params.items())}"

    # Redirect the user to the authorization URL
    return redirect(auth_url)

@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')

    token_params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    response = requests.post(TOKEN_URL, data=token_params)
    response_data = response.json()

    access_token = response_data.get('access_token')
    refresh_token = response_data.get('refresh_token')
    session['access token'] = access_token
    session['flag'] = True

    # if not getUser(access_token):
    #     addUser(access_token)

    return redirect('/')

@app.route('/get-session-data', methods=['GET'])
def get_session_data():
    session_data = dict(session)
    return jsonify(session_data)

if __name__ == '__main__':
    app.run()
