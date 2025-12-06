# Trading System - Complete Demo

This is a runnable demo of the Trading Automation system (Telegram-like reader -> parser -> FXBlue mock -> FastAPI backend -> simple React frontend).  
It is simplified for demo use so you can run everything locally without real Telegram or FXBlue credentials.

## What is included
- Backend (FastAPI) that:
  - Accepts incoming "messages" from a simple message reader
  - Parses signals in English/Dutch/Spanish-ish formats
  - Places orders against a local mock FXBlue service
  - Stores signals and orders in SQLite
- FXBlue mock server that simulates placing orders
- Frontend (React + Vite) that shows incoming signals and orders
- Docker Compose to run all components, or run locally with Python and Node

## Quickstart (local, without Docker)
Requirements: Python 3.10+, Node 18+, npm

### Backend
```
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# create sample messages file
python -m backend.seed_samples
# run backend
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### FXBlue mock
```
# FXBlue mock is part of backend and started automatically by Uvicorn on /fxblue route
```

### Frontend
```
cd frontend
npm install
npm run dev
# Visit http://localhost:5173
```

## Quickstart (Docker)
Install Docker and Docker Compose v2.
```
docker compose up --build
# frontend at http://localhost:5173
# backend at http://localhost:8000
```

docker build -t trading-tips .

## Notes
- This demo **does not** connect to real Telegram. It includes a simple "message reader" that reads sample messages from `backend/samples/messages.txt` and pushes them through the pipeline.
- To connect Telethon later, replace `backend/reader.py` with a Telethon listener and call `process_raw_message`.
