import json
import time 
import math
import random
import base64

from celery import Celery
from spotipy import Spotify
import redis 
import spotipy

from db import redis_client
from artists import artist_manager

celery = Celery(__name__, broker='redis://localhost:6379/0')

playlist_img = "../data/playlist_img.jpeg"
# Read the image file and encode it in base64
with open(playlist_img, 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read())
    
if len(encoded_image) > 256000: # check if image is too big
    print("Image is too big: ", len(encoded_image))

playlist_len = 200

# Job 1: Get top artists
@celery.task
def start_job_1(user_id, access_token):
    
    artists = artist_manager.artists
    
    print(f"Starting job 1 for user {user_id}")
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
            filtered_top_artists.append({"name": artist, "bio": artists[artist]['bio']})

    # Store the result in Redis
    redis_client.set(f"job_1_result_{user_id}", json.dumps(filtered_top_artists))
        
    # Trigger job 2
    top_artists_names = [artist['name'] for artist in filtered_top_artists]
    start_job_2.delay(user_id, access_token, top_artists_names)

# Job 2: Get recommended artists
@celery.task
def start_job_2(user_id, access_token, top_artists_data):
    print(f"Starting job 2 for user {user_id}")
        
    desired_reccs = 30
    required_reccs = desired_reccs - len(top_artists_data)
        
    recommended_artists = artist_manager.get_reccs(top_artists_data, required_reccs)
    
    # Store the result in Redis
    redis_client.set(f"job_2_result_{user_id}", json.dumps(recommended_artists))
    
    recc_names = [artist['name'] for artist in recommended_artists]
    
    start_job_3.delay(user_id, access_token, top_artists_data, recc_names)
    

# Job 3: Generate playlist
@celery.task
def start_job_3(user_id, access_token, top_artists, recc_artists):
    print(f"Starting job 3 for user {user_id}")
    artists_data = artist_manager.artists
    sp = spotipy.Spotify(auth=access_token)
    
    all_artists = top_artists + recc_artists
    
    playlist_name = "GlastoJam 2024"
    playlist_description = "A personal playlist created by GlastoJam with your favourite artists and brand new finds for you to get hyped for Glastonbury."

    # Create the playlist
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description)
    playlist_id = playlist['id']
    
    # Search for tracks by matched artists and add to the playlist
    track_uris = []
    num_artists = len(all_artists)
    num_tracks_per_artist = math.ceil(playlist_len / num_artists) if num_artists > 0 else 0
    
    # Loop through all artists
    for artist in all_artists:
        print(f"Searching for tracks by {artist}")
        artist_tracks = []

        # If known spotify problem skip
        print(artists_data[artist]['problem'])
        if artists_data[artist]['problem']:
            print(f"Skipping {artist} due to known problem")
            continue
        
        # If an artist name pulls up many matches, check more tracks
        lim = 10 if artists_data[artist]['matches'] <= 10 else 50

        # Search for top tracks
        # spotify api does fuzzy artist name matching so expect tracks from other (similarly named) artists
        search_results = sp.search(q=f'artist:{artist}', type='track', limit=lim)        
        items = search_results.get('tracks', {}).get('items', [])
                    
        # Loop through the tracks
        print("Looping through tracks")
        for track in items:
            track_artists = [artist['name'].upper() for artist in track['artists']]
            # Eliminate tracks by other artists
            if artist not in track_artists:
                continue
            
            artist_tracks.append(track['uri'])
            
            # Break when enough
            if len(artist_tracks) >= num_tracks_per_artist:
                break
                    
        # Add the tracks to all tracks
        track_uris.extend(artist_tracks)
    
    # Limit the total number of tracks to 100
    track_uris = track_uris[:playlist_len]

    # Shuffle the track URIs
    random.shuffle(track_uris)
    
    # Add tracks to the playlist in chunks of 100
    for i in range(0, len(track_uris), 100):
        sp.playlist_add_items(playlist_id, track_uris[i:i+100])
        
    try:
        sp.playlist_upload_cover_image(playlist_id, encoded_image)
    except Exception as e:
        print(f"Failed to upload cover image: {e}")
        
    # Put into redis
    redis_client.set(f"job_3_result_{user_id}", json.dumps({"playlist_id": playlist_id}))

# Job 4: Clashes

def get_job_result(job_id, user_id):
    result = redis_client.get(f"{user_id}_{job_id}")
    if result:
        return json.loads(result)
    return None


