from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .clashfinder import *
import requests
app = FastAPI()

# Allow CORS for your frontend application
origins = [
    "http://localhost:3004",  # Your Next.js frontend URL
]

@app.post("/receive_top_artist")
async def receive_top_artist(request: Request):
    top_artist_info = await request.json()
    # Process the top artist information as needed
    return JSONResponse({"message": "Top artist received successfully", "top_artist": top_artist_info})



artists_variable = [
    "ALMA",
    "Anish Kumar",
    "BICEP",
    "Barry Can't Swim",
    "Blue",
    "Diddy",
    "Honey Dijon",
    "Jamie xx",
    "Jayda G",
    "Jungle",
    "Kate Nash",
    "MIMI",
    "MJ Cole",
    "O'Flynn",
    "Peggy Gou",
    "Pola & Bryson",
    "Prospa",
    "Ross from Friends",
    "Sammy Virji",
    "Unglued",
    "Young Marco",
    "salute"
]

clashes_variable = clashfinder_Function(artists_variable)

# clashes_variable_DEMO = [
#     {
#         "id": 1,
#         "artists": ["Dua Lipa", " Styles"],
#         "start": "2023-06-24T19:00:00",
#         "end": "2023-06-24T19:30:00",
#         "day_of_clash": "Sunday",
#     },
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/artists")
def get_artists():
    artists = artists_variable
    return {"artists": artists}

@app.get("/clashes")
def get_clashes():
    clashes = clashes_variable
    return {"clashes": clashes}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003, reload=True)
