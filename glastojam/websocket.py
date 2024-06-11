import json
from typing import List, Optional

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from fastapi.responses import JSONResponse
import jwt
import asyncio
import aioredis

async def get_redis_client():
    return await aioredis.from_url("redis://localhost")  # Update with your Redis URL

from config import SECRET_KEY, ALGORITHM
from db import redis_client

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.user_connections: dict = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.user_connections[user_id] = websocket
        
    def disconnect(self, websocket: WebSocket, user_id: str):
        if user_id in self.user_connections:
            del self.user_connections[user_id]
            
        print("User disconnected")
        print(self.user_connections)

    async def send_personal_message(self, message: dict, user_id: str):
        if user_id in self.user_connections:
            await self.user_connections[user_id].send_text(json.dumps(message))

manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, user: str = Query(...)):
    print(f"User {user} connected")
    await manager.connect(websocket, user)
    
    async_redis_client = await get_redis_client()
    
    statuses = {
        'job_1': False,
        'job_2': False,
    }

    async def poll_redis_for_results(user_id):
        print(f"Polling Redis for results for user {user_id}")
        try:
            while True:
                print("loop")
                # If all jobs returned - exit
                if all(statuses.values()):
                    break
                
                # Check for job results in Redis
                for job_num in range(1, 3):
                    # Skip if already sent
                    if statuses[f"job_{job_num}"]:
                        continue
                    
                    key = f"job_{job_num}_result_{user_id}"
                    print(key)
                    
                    result = await async_redis_client.get(key)
                    if result:
                        await manager.send_personal_message({"job": f"job_{job_num}", "result": json.loads(result.decode("utf-8"))}, user_id)
                        statuses[f"job_{job_num}"] = True
                
                # Polling interval
                await asyncio.sleep(1)  # Adjust the sleep interval as needed

        except WebSocketDisconnect as e:
            print(f"User {user} disconnected during polling - {e}")
            manager.disconnect(websocket, user)

    poll_task = asyncio.create_task(poll_redis_for_results(user))

    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message({"message": f"You wrote: {data}"}, user)
    except WebSocketDisconnect as e:
        print(f"User {user} disconnected - {e}")
        manager.disconnect(websocket, user)
        poll_task.cancel()

@router.get("/get_connections")
async def get_connections():
    data = {"active_connections": len(manager.active_connections), "user_connections": list(manager.user_connections.keys())}
    return JSONResponse(data)