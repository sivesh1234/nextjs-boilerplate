from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Request
from typing import List, Optional
import json
import asyncio
import jwt
from config import SECRET_KEY, ALGORITHM

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

manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, request: Request):
    token = request.cookies.get("access_token")
    if not token:
        await websocket.close(code=1008, reason="Token required")
        return

    user_id = get_user_id_from_token(token)
    if not user_id:
        await websocket.close(code=1008, reason="Invalid token")
        return

    print(f"User {user_id} connected")
    await manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message({"message": f"You wrote: {data}"}, user_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, user_id)

def send_job_update(user_id: str, result: dict):
    asyncio.run(manager.send_personal_message(result, user_id))

def get_user_id_from_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        return user_id
    except jwt.PyJWTError:
        return None
