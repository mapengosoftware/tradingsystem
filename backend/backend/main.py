import asyncio
import os
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from .db import database, metadata, engine
from .api import router
from .reader import start_sample_reader
from .fxblue.mock_server import create_mock_app
import threading
import uvicorn

app = FastAPI(title="Trading Automation - Demo Backend")
app.include_router(router, prefix="/api")

@app.on_event("startup")
async def startup():
    # create tables
    metadata.create_all(engine)
    await database.connect()
    # start sample reader in background thread
    loop = asyncio.get_event_loop()
    loop.create_task(start_sample_reader())

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/health")
async def health():
    return {"status":"ok"}

# Mount a tiny HTML page for quick view (optional)
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'static')), name="static")

if __name__ == '__main__':
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
