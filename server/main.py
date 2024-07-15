from threading import Thread

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.routes import locations
from server.services.video_stream import start_stream_capture

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(locations.router)

Thread(target=start_stream_capture).start()
