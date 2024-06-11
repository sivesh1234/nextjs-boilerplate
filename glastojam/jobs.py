from celery import Celery
from spotipy import Spotify
import redis
import json
from db import redis_client
import time

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task
def start_job_1(user_id, access_token):
    print(f"Starting job 1 for user {user_id}")
    time.sleep(5)
    top_artists_data = [{"name": "Artist 1", "bio": "demo bio"}, {"name": "Artist 2", "bio": "demo bio"}, {"name": "Artist 3", "bio": "demo bio"}]

    # Store the result in Redis
    redis_client.set(f"job_1_result_{user_id}", json.dumps(top_artists_data))
    
    # Notify the user via Redis
    redis_client.publish('job_updates', json.dumps({"user_id": user_id, "job": "job_1", "result": top_artists_data}))
    
    # Trigger job 2
    start_job_2.delay(user_id, access_token, top_artists_data)

@celery.task
def start_job_2(user_id, access_token, top_artists_data):
    print(f"Starting job 2 for user {user_id}")
    time.sleep(10)
    recommended_artists = [{"name": "Artist 4", "bio": "demo bio"}, {"name": "Artist 5", "bio": "demo bio"}, {"name": "Artist 6", "bio": "demo bio"}]

    # Store the result in Redis
    redis_client.set(f"job_2_result_{user_id}", json.dumps(recommended_artists))

    # Notify the user via Redis
    redis_client.publish('job_updates', json.dumps({"user_id": user_id, "job": "job_2", "result": recommended_artists}))

def get_job_result(job_id, user_id):
    result = redis_client.get(f"{user_id}_{job_id}")
    if result:
        return json.loads(result)
    return None


