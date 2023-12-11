from fastapi import FastAPI
from services.sentiment_service import sentiment_analyze_service
from services.music_service import create_melody_service
from fastapi.middleware.cors import CORSMiddleware
from models.content_model import Content

import os, sys

current_directory = os.path.dirname(os.path.realpath(__file__))
services_path = os.path.join(current_directory, 'services')
sys.path.append(services_path)

app = FastAPI()
origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/sentiment/")
async def sentiment_analyze(content: Content):
    return await sentiment_analyze_service(content)

@app.post("/music/")
async def create_melody(content: Content):
    return await create_melody_service(content)


# uvicorn main:app --reload
