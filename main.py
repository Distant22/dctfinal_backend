from typing import Union
from services.sentiment_service import analyze
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.content_model import Content
import os

credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
app = FastAPI()
origins = [
    "https://dctfinal-frontend.vercel.app"
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

@app.get("/sentiment/")
def read_root():
    return {"text": "sentiment page"}

@app.post("/sentiment/")
async def read_item(content: Content):
    return await analyze(content)
