from datetime import datetime, timedelta

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.security import OAuth2PasswordBearer
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import jwt

from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SECRET_KEY, ALGORITHM
from jobs import start_job_1
from db import redis_client

router = APIRouter()

credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

class User(BaseModel):
    id: str
    username: str

class TokenData(BaseModel):
    username: str

def create_jwt_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private user-read-email playlist-modify-public user-top-read ugc-image-upload"
    
)

@router.get("/login")
async def login():
    print("At endpoint /login")
    auth_url = sp_oauth.get_authorize_url()
    print(f"Redirecting to {auth_url}")
    return JSONResponse({"auth_url": auth_url})

@router.get("/check_auth")
async def check_auth(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return JSONResponse({"status": "authenticated"})
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
@router.get('/get_user_id')
async def get_id(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return JSONResponse({"id": user_id})
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/callback")
async def callback(code: str):
    print("At endpoint /callback")
    token_info = sp_oauth.get_access_token(code, check_cache=False)
    if not token_info:
        raise HTTPException(status_code=400, detail="Invalid Spotify token")
    
    access_token = token_info['access_token']
    spotify = Spotify(auth=access_token)
    user_info = spotify.me()
    user = User(id=user_info['id'], username=user_info['display_name'])
    
    # Create a JWT containing only the user ID
    jwt_token = create_jwt_token(data={"sub": user.id})
    
    # If user is already in Redis, don't start the jobs
    if not redis_client.exists(user.id):
        print("Callback starting jobs")
        # Start the jobs with the user ID and Spotify access token
        job_1 = start_job_1.delay(user.id, access_token)
        
        # Put job ID for user in Redis
        redis_client.set(user.id, job_1.id)

    response = RedirectResponse(url=f"http://localhost:3000/data")
    response.set_cookie(key="access_token", value=jwt_token, httponly=True)
    return response

def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(username=user_id)
    except jwt.PyJWTError:
        raise credentials_exception
    return User(id=token_data.username, username=token_data.username)