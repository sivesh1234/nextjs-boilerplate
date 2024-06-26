import json

from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from auth import router as auth_router, get_current_user, User
from websocket import router as websocket_router
from jobs import get_job_result
from db import redis_client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(websocket_router)

app.mount("/", StaticFiles(directory="static/", html=True), name="static")

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
    job_3_result = redis_client.get(f"job_3_result_{user.id}")

    return JSONResponse({
        "job_1_result": json.loads(job_1_result) if job_1_result else None,
        "job_2_result": json.loads(job_2_result) if job_2_result else None,
        "job_3_result": json.loads(job_3_result) if job_3_result else None,
    }) 

