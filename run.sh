#!/bin/bash

cd glastojam

# Start Redis server in the background
echo "Starting Redis server..."
redis-server &

# Give Redis a moment to start
sleep 2

# # Start Celery worker in the background
# echo "Starting Celery worker..."
celery -A jobs worker --loglevel=info &

# Give Celery a moment to start
sleep 2

# Start FastAPI server in the foreground
echo "Starting FastAPI server..."
python main.py
uvicorn main:app --reload --host 0.0.0.0 --port 8080
