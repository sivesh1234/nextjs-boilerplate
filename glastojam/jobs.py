import json
import time

from celery import Celery
from spotipy import Spotify
import redis
import spotipy

from db import redis_client
from artists import artists

celery = Celery(__name__, broker='redis://localhost:6379/0')

# Job 1: Get top artists
@celery.task
def start_job_1(user_id, access_token):
    
    print(f"Starting job 1 for user {user_id}")
    time.sleep(5)
    top_artists_data = [{"name": "Artist 1", "bio": "demo bio"}, {"name": "Artist 2", "bio": "demo bio"}, {"name": "Artist 3", "bio": "demo bio"}]

    sp = spotipy.Spotify(auth=access_token)

    # Fetch user's top tracks for all time ranges
    print("Fetching top tracks")
    top_tracks_short = sp.current_user_top_tracks(limit=50, time_range='short_term')['items']
    top_tracks_medium = sp.current_user_top_tracks(limit=50, time_range='medium_term')['items']
    top_tracks_long = sp.current_user_top_tracks(limit=50, time_range='long_term')['items']

    # Combine all top tracks
    print("Combining top tracks")
    all_tracks = top_tracks_short + top_tracks_medium + top_tracks_long

    # Extract unique artist names
    user_artist_set = set()
    for track in all_tracks:
        artist_names = [artist['name'] for artist in track['artists']]
        user_artist_set.update(artist_names)

    # Fetch top 10 artists over the last medium term
    top_artists_medium = sp.current_user_top_artists(limit=50, time_range='medium_term')['items']
    top_10_artists = [artist['name'] for artist in top_artists_medium]

    # Cmbine top 10 artists with unique artist names
    user_artist_set.update(top_10_artists)
    
    filtered_top_artists = []
    for artist in user_artist_set:
        artist = artist.upper()
        print(f"Checking artist: {artist}")
        if artist in artists:
            filtered_top_artists.append({"name": artist, "bio": artists[artist]})

    # Store the result in Redis
    redis_client.set(f"job_1_result_{user_id}", json.dumps(filtered_top_artists))
        
    # Trigger job 2
    start_job_2.delay(user_id, access_token, top_artists_data)

# Job 2: Get recommended artists
@celery.task
def start_job_2(user_id, access_token, top_artists_data):
    print(f"Starting job 2 for user {user_id}")
    time.sleep(10)
    recommended_artists = [{"name": "Artist 4", "bio": "demo bio"}, {"name": "Artist 5", "bio": "demo bio"}, {"name": "Artist 6", "bio": "demo bio"}]

    # Store the result in Redis
    redis_client.set(f"job_2_result_{user_id}", json.dumps(recommended_artists))

# Job 3: Generate playlist

# Job 4: Clashes

def get_job_result(job_id, user_id):
    result = redis_client.get(f"{user_id}_{job_id}")
    if result:
        return json.loads(result)
    return None


