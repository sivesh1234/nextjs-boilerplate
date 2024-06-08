from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from clashfinder import *
app = FastAPI()

# Allow CORS for your frontend application
origins = [
    "http://localhost:3002",  # Your Next.js frontend URL
]

artists_variable = ['Sugababes','Aurora','Sprints','Lulu','Dervish','Jada Star','Kneecap']

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
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
