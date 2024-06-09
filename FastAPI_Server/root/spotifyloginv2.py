import os
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import pandas as pd
import math
from datetime import datetime, timedelta
import random
import logging
from typing import List
from root.lineup import DATA

# Import clashfinder functionality
from root.clashfinder import clashfinder_Function

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define constants
CLIENT_ID = '706e874fa0b646c4a3cc975944e2564f'
CLIENT_SECRET = 'f861fef03f134a67908cef710baa2d5b'
REDIRECT_URI = 'http://localhost:8080/callback'
SCOPE = 'playlist-modify-public user-top-read'

# List of stages to be removed
stages_to_remove = [
    "The Information", "Circus Big Top", "The Astrolabe Theatre", "Left Field",
    "Free University of Glastonbury", "Humblewell Active Platform", "Humblewell Retreat Yurt",
    "Temple Uprising", "Greenpeace (Beam)", "Speakers Forum", "Laboratory Stage",
    "Glasto Latino", "Pilton Palais Cinema", "Terminal 1", "Cabaret", "Poetry&Words",
    "Atchin Tan", "Kidzfield Big Top", "Outside Circus Stage"
]

acts_to_remove = [
    "Diddy"
]



# Initialize FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Allow CORS for your frontend application
origins = [
    "http://localhost:3003",  # Your Next.js frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Top artists variable for clashfinder
artists_variable = [

]

clashes_variable = []
playlist_id = ""

def clear_cache():
    # Clear any cache files if they exist
    if os.path.exists(".cache"):
        os.remove(".cache")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@app.get("/login")
async def login():
    clear_cache()
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE, cache_path=None, show_dialog=True)
    auth_url = sp_oauth.get_authorize_url()
    logger.info(f"Redirecting to Spotify auth URL: {auth_url}")
    return RedirectResponse(auth_url)

@app.get("/callback")
async def callback(request: Request):
    clear_cache()
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE, cache_path=None, show_dialog=True)
    code = request.query_params.get('code')
    if not code:
        logger.error("No code found in request parameters")
        raise HTTPException(status_code=400, detail="No code found in request parameters")

    try:
        token_info = sp_oauth.get_access_token(code)
        if not token_info:
            logger.error("Could not get access token")
            raise HTTPException(status_code=400, detail="Could not get access token")
        logger.info(f"Access token retrieved: {token_info['access_token']}")
    except Exception as e:
        logger.error(f"Error during token exchange: {e}")
        raise HTTPException(status_code=500, detail="Error during token exchange")

    sp = spotipy.Spotify(auth=token_info['access_token'])

    # Fetch user's top tracks for all time ranges
    top_tracks_short = sp.current_user_top_tracks(limit=50, time_range='short_term')['items']
    top_tracks_medium = sp.current_user_top_tracks(limit=50, time_range='medium_term')['items']
    top_tracks_long = sp.current_user_top_tracks(limit=50, time_range='long_term')['items']

    # Combine all top tracks
    all_tracks = top_tracks_short + top_tracks_medium + top_tracks_long

    # Extract unique artist names
    artist_set = set()
    for track in all_tracks:
        artist_names = [artist['name'] for artist in track['artists']]
        artist_set.update(artist_names)

    # Create a list of unique top artists
    unique_top_artists = sorted(artist_set)

    # Print the list of unique top artists for debugging
    logger.info("\nUnique Top Artists:")
    for idx, artist in enumerate(unique_top_artists):
        logger.info(f"{idx + 1}. {artist}")

    # Fetch top 10 artists over the last medium term
    top_artists_medium = sp.current_user_top_artists(limit=10, time_range='medium_term')['items']
    top_10_artists = [artist['name'] for artist in top_artists_medium]

    # Print top 10 artists for debugging
    logger.info("\nTop 10 Artists (Medium Term):")
    for idx, artist in enumerate(top_10_artists):
        logger.info(f"{idx + 1}. {artist}")

    # Read the lineup CSV file
    DATA.seek(0)
    lineup_df = pd.read_csv(DATA)

    # Initialize an empty list to store matching rows
    matching_rows = []

    # Filter the lineup based on the unique top artists
    for artist in unique_top_artists:
        # Use regular expressions with word boundaries to ensure full word match
        regex_pattern = rf'\b{re.escape(artist)}\b'
        matches = lineup_df[lineup_df['Act'].str.contains(regex_pattern, case=False, na=False)].copy()
        if not matches.empty:
            matches['Matched Artist'] = artist
            matching_rows.append(matches)

    # Combine all matching rows into a single DataFrame
    if matching_rows:
        matched_df = pd.concat(matching_rows).drop_duplicates().reset_index(drop=True)
        # Select the required columns
        matched_df = matched_df[['Act', 'Day', 'Stage', 'Start', 'Finish', 'Matched Artist']]
    else:
        matched_df = pd.DataFrame(columns=['Act', 'Day', 'Stage', 'Start', 'Finish', 'Matched Artist'])

    # Remove entries with specific stages
    matched_df = matched_df[~matched_df['Stage'].isin(stages_to_remove)]
    # Remove entries with specific Acts
    matched_df = matched_df[~matched_df['Act'].isin(acts_to_remove)]

    # Create a list of unique matched artists
    unique_matched_artists = matched_df['Matched Artist'].unique().tolist()

    # Store the unique matched artists in the artists_variable for serving to the frontend
    global artists_variable
    artists_variable = unique_matched_artists

    # Print the list of unique matched artists for debugging
    logger.info("\nUnique Matched Artists:")
    for idx, artist in enumerate(unique_matched_artists):
        logger.info(f"{idx + 1}. {artist}")

    # Create a playlist and add songs from the matched artists
    user_id = sp.current_user()['id']
    playlist_name = "Glastotify Playlist"
    playlist_description = "A personal playlist created by Glastotify with your favourite artists and brand new finds for you to get hyped for Glastonbury."

    # Create the playlist
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description)
    global playlist_id
    playlist_id = playlist['id']

    # Search for tracks by matched artists and add to the playlist
    track_uris = []
    num_artists = len(unique_matched_artists)
    num_tracks_per_artist = math.ceil(100 / num_artists) if num_artists > 0 else 0

    for artist in unique_matched_artists:
        search_results = sp.search(q=f'artist:{artist}', type='track', limit=num_tracks_per_artist)
        tracks = search_results['tracks']['items']
        for track in tracks:
            track_uris.append(track['uri'])

    # Limit the total number of tracks to 100
    track_uris = track_uris[:100]

    # Shuffle the track URIs
    random.shuffle(track_uris)

    # Add tracks to the playlist in chunks of 100
    for i in range(0, len(track_uris), 100):
        sp.playlist_add_items(playlist_id, track_uris[i:i+100])

    # Adjust days for events between midnight and 8:00 AM
    def adjust_day_and_time(row):
        start_time = datetime.strptime(row['Start'], '%H:%M').time()
        finish_time = datetime.strptime(row['Finish'], '%H:%M').time()
        start_date = datetime.strptime(day_map[row['Day']], '%Y-%m-%d')
        finish_date = start_date

        if start_time < datetime.strptime('08:00', '%H:%M').time():
            start_date += timedelta(days=1)

        if finish_time < datetime.strptime('08:00', '%H:%M').time() and row['Start'] < row['Finish']:
            finish_date += timedelta(days=1)

        row['Start DateTime'] = datetime.combine(start_date, start_time)
        row['Finish DateTime'] = datetime.combine(finish_date, finish_time)
        return row

    day_map = {'Thursday': '2023-06-27', 'Friday': '2023-06-28', 'Saturday': '2023-06-29', 'Sunday': '2023-06-30'}
    matched_df = matched_df.apply(adjust_day_and_time, axis=1)

    # Generate a list of unique stages
    stages = matched_df['Stage'].unique().tolist()

    # Update clashes_variable with the clashfinder function's results
    global clashes_variable
    clashes_variable = clashfinder_Function(artists_variable)

    # Instead of rendering HTML, redirect to the frontend URL
    if os.environ.get("ENVIRONMENT") == "production":
        return RedirectResponse(url="/")
    return RedirectResponse(url="http://localhost:3003/")

@app.get("/generate_playlist")
async def generate_playlist(request: Request):
    return await callback(request)

@app.post("/receive_top_artist")
async def receive_top_artist(request: Request):
    top_artist_info = await request.json()
    # Process the top artist information as needed
    return JSONResponse({"message": "Top artist received successfully", "top_artist": top_artist_info})

@app.get("/artists")
def get_artists():
    global artists_variable
    artists = artists_variable
    return {"artists": artists}

@app.get("/clashes")
def get_clashes():
    global clashes_variable
    clashes = clashes_variable
    return {"clashes": clashes}

@app.get("/playlist_id")
def get_playlist_id():
    global playlist_id
    return {"playlist_id": playlist_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003, reload=True)
