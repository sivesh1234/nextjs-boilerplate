import json
import signal
import sys
import subprocess
import os
import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from auth import router as auth_router, get_current_user, User
from websocket import router as websocket_router, manager  # Ensure this import is correct
from jobs import get_job_result, celery_app
from db import redis_client

# Lifespan context for startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up")
    start_redis_listener()
    yield
    print("Shutting down")
    celery_app.control.shutdown()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(websocket_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/job-result/{job_id}")
async def job_result(job_id: str, current_user: User = Depends(get_current_user)):
    result = get_job_result(job_id, current_user.id)
    if result is None:
        raise HTTPException(status_code=404, detail="Job not found or not finished yet")
    return result

@app.get("/fetch_results")
async def fetch_results(user: User = Depends(get_current_user)):
    job_1_result = redis_client.get(f"job_1_result_{user.id}")
    job_2_result = redis_client.get(f"job_2_result_{user.id}")

    return JSONResponse({
        "job_1_result": json.loads(job_1_result) if job_1_result else None,
        "job_2_result": json.loads(job_2_result) if job_2_result else None
    }) 

subprocesses = []

def start_redis_listener():
    loop = asyncio.get_event_loop()
    loop.create_task(manager.handle_redis_messages())



# Function to handle termination signals
def signal_handler(sig, frame):
    print("Terminating processes...")
    for process in subprocesses:
        process.terminate()
    celery_app.control.shutdown()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    worker = subprocess.Popen(
        ["celery", "-A", "jobs", "worker", "--loglevel=info"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        preexec_fn=os.setpgrp
    )
    subprocesses.append(worker)
    
    
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
