from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Request, Query
from fastapi.responses import JSONResponse
from typing import List, Optional
import json
import jwt
from config import SECRET_KEY, ALGORITHM
from db import redis_client

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.user_connections: dict = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        if user_id not in self.user_connections:
            self.user_connections[user_id] = []
        self.user_connections[user_id].append(websocket)

    def disconnect(self, websocket: WebSocket, user_id: str):
        self.active_connections.remove(websocket)
        self.user_connections[user_id].remove(websocket)
        if not self.user_connections[user_id]:
            del self.user_connections[user_id]

    async def send_personal_message(self, message: dict, user_id: str):
        if user_id in self.user_connections:
            for connection in self.user_connections[user_id]:
                await connection.send_text(json.dumps(message))

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def handle_redis_messages(self):
        pubsub = redis_client.pubsub()
        pubsub.subscribe('job_updates')
        for message in pubsub.listen():
            if message['type'] == 'message':
                data = json.loads(message['data'])
                user_id = data['user_id']
                await self.send_personal_message(data, user_id)

manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, user: str = Query(...)):
    print(f"User {user} connected")
    await manager.connect(websocket, user)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message({"message": f"You wrote: {data}"}, user)
    except WebSocketDisconnect:
        print(f"User {user} disconnected")
        manager.disconnect(websocket, user)

def get_user_id_from_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        return user_id
    except jwt.PyJWTError:
        return None

@router.get("/get_connections")
async def get_connections():
    data = {"active_connections": len(manager.active_connections), "user_connections": list(manager.user_connections.keys())}
    return JSONResponse(data)