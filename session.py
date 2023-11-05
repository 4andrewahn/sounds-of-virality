import requests
import base64
import os
from dotenv import load_dotenv
import datetime as dt
import time

load_dotenv()

# Spotify API related constants
BASE_API_URL = 'https://api.spotify.com/v1'
MAX_API_CALLS = 25 # Max allowed request sent per function
SLEEP_TIME = 1

# 12 Audio attributes for data collection 
ATTRIBUTES = [
    'id', # string - Spotify ID for the track
    'acousticness', # number [float]
    'danceability', # number [float]
    'energy', # number [float]
    'instrumentalness', # number [float]
    'key', # integer 
    'liveness', # number [float]
    'loudness', # number [float]
    'mode', # integer 
    'speechiness', # number [float]
    'tempo', # number [float]
    'time_signature', # integer 
    'valence' # number [float]
]


class SessionError(Exception):
    '''Exception for all session-related errors'''
    pass

class Session:
    def __init__(self):
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.token = ' '


    def get_token(self):
        '''
        Returns the current access token string 
        '''
        return self.token


    def renew_token(self):
        '''
        Update access token in session
        '''
        # Generate request 
        auth_header = base64.b64encode(f'{self.client_id}:{self.client_secret}'.encode('utf-8')).decode('utf-8')
        headers = {
            'Authorization': f'Basic {auth_header}'
        }
        form = {
            'grant_type': 'client_credentials'
        }

        # Send POST request
        response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=form)

        # Update access token
        if response.status_code == 200:
            # Update Session values 
            self.token = response.json()['access_token']
        else:
            raise SessionError(f'Something went wrong renewing access token: API status code = {response.status_code}')

    
    def get_playlist_tracks(self, playlist_id: str):
        '''
        Return a list of dictionaries storing Spotify IDs, track name, main artist name for the tracks in a playlist 
        '''
        tracks = [] # List to output 
        request_count = 0 # Counter for requests sent
        at_playlist_end = False 

        # Generate request constants
        api_url = f'{BASE_API_URL}/playlists/{playlist_id}/tracks'
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        # Send requests until all tracks have been parsed from the playlist 
        while not at_playlist_end:
            # Check rate limiting 
            if request_count >= MAX_API_CALLS: 
                raise SessionError('Too many API calls to /playlists/playlist_id/tracks')
            
            # Specify request parameters  
            params = {
                'fields': 'items(track(artists(name), id, name))',
                'limit': 50, # Spotify API limits requests to 50 tracks max
                'offset': 50 * request_count
            }

            # Send GET request
            response = requests.get(api_url, headers=headers, params=params)

            # Parse response 
            if response.status_code == 200:
                items = response.json()['items']
                num_items = len(items)

                # Add received tracks to output 
                for item in items:
                    # Check if 'track' data is none null
                    if item and 'track' in item and item['track']:
                        entry = {
                            'id': item['track']['id'],
                            'name': item['track']['name'],
                            'artist': item['track']['artists'][0]['name']
                            }
                        tracks.append(entry)

                # Check if the end of the playlist has been reached 
                if num_items < 50:
                    at_playlist_end = True
                else:
                    request_count += 1
                    time.sleep(SLEEP_TIME)
            elif response.status_code == 401:
                # Invalid access token, session must renew token 
                self.renew_token()
            else:
                raise SessionError(f'Something went wrong retrieving playlist tracks: API status code = {response.status_code}')
        return tracks


    def get_audio_features(self, track_ids: [str]):
        '''
        Returns a list of audio features for each track id stored as a dictionary
        '''
        audio_features_output = [] # List to output 

        # Generate request constants
        api_url = f'{BASE_API_URL}/audio-features'
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        # Send requests until all tracks have been parsed from the playlist
        request_count = 0 
        limit = 100 # Spotify's audio-features API track limit 
        num_tracks_inputted = len(track_ids)
        has_completed_list = False

        tracks_requested = 0
        while not has_completed_list: 
            # Check rate limiting 
            if request_count >= MAX_API_CALLS: 
                raise SessionError('Too many API calls to /audio-features')
            
            # Specify request parameters  
            offset = limit * request_count
            selected_track_ids = track_ids[offset:offset+limit]
            tracks_requested += len(selected_track_ids)
            
            params = {
                'ids': ','.join(selected_track_ids)
            }

            # Send GET request
            response = requests.get(api_url, headers=headers, params=params)

            # Parse response 
            if response.status_code == 200:
                features = response.json()['audio_features']

                # Add received tracks to output 
                for entry in features:
                    if entry:
                        track_features = {} # Dictionary to hold a track's audio features
                        for attr in ATTRIBUTES: 
                            if attr in entry:
                                track_features[attr] = entry[attr]
                        if len(track_features) > 0: 
                            audio_features_output.append(track_features)

                # Check if all tracks inputted have been collected 
                if tracks_requested < num_tracks_inputted:
                    request_count += 1
                    time.sleep(SLEEP_TIME)
                else:
                    has_completed_list = True
            elif response.status_code == 401:
                # Invalid access token, session must renew token 
                self.renew_token()
            else:
                raise SessionError(f'Something went wrong retrieving audio features, status_code = {response.status_code}')
        return audio_features_output
