from celery import Celery
from spotipy import Spotify
import redis
from websocket import send_job_update
import json


celery = Celery(__name__, broker='redis://localhost:6379/0')
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@celery.task
def start_job_1(user_id, access_token):
    print(f"Starting job 1 for user {user_id}")
    # spotify = Spotify(auth=access_token)
    # top_artists = spotify.current_user_top_artists(limit=10)
    # top_artists_data = {"top_artists": [artist['name'] for artist in top_artists['items']]}
    top_artists_data = {"top_artists": ["Artist 1", "Artist 2", "Artist 3"]}

    # Store the result in Redis
    redis_client.set(f"job_1_result_{user_id}", json.dumps(top_artists_data))
    
    # Notify the user via WebSocket
    send_job_update(user_id, {"job": "job_1", "result": top_artists_data})
    
    # Trigger job 2
    start_job_2.delay(user_id, access_token, top_artists_data)

@celery.task
def start_job_2(user_id, access_token, top_artists_data):
    print(f"Starting job 2 for user {user_id}")
    # Example: Get recommendations based on top artists
    # spotify = Spotify(auth=access_token)
    # artist_ids = [artist['id'] for artist in top_artists_data['top_artists']]
    # recommendations = spotify.recommendations(seed_artists=artist_ids, limit=10)
    # recommendations_data = {"recommendations": [track['name'] for track in recommendations['tracks']]}
    recommended_artists = ["Recommended Artist 1", "Recommended Artist 2", "Recommended Artist 3"]

    # Store the result in Redis
    redis_client.set(f"job_2_result_{user_id}", json.dumps(recommended_artists))

    # Notify the user via WebSocket
    send_job_update(user_id, {"job": "job_2", "result": recommended_artists})

def get_job_result(job_id, user_id):
    result = redis_client.get(f"{user_id}_{job_id}")
    if result:
        return json.loads(result)
    return None


