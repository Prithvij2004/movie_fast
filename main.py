from typing import Annotated

from fastapi import FastAPI, Form
from starlette.middleware.cors import CORSMiddleware
import httpx

import dotenv
import os

dotenv.load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

api_key = os.getenv("API_KEY")

 
async def fetch_movie_details(id: str):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        movie_details = response.json()
    return movie_details

@app.get("/movie")
async def get_movie_details(id: Annotated[str, Form(...)]):
    movie_details = await fetch_movie_details(id)
    return movie_details



