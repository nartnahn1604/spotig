import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Create an instance of the Spotify client with your credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_song(query):
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        return results['tracks']['items'][0]
    return None

def get_song_url(track_id, access_token):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'  # Replace with your Spotify access token
    }


    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        track_data = response.json()
        song_url = track_data['uri']
        return song_url

    return None