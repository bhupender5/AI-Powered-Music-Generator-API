from fastapi import FastAPI
from pydantic import BaseModel
from music_generator import generate_music

app = FastAPI()

class MusicRequest(BaseModel):
    prompt: str


@app.post("/generate-music")
def generate_music_api(request: MusicRequest):

    file_path = generate_music(request.prompt)

    return {
        "prompt": request.prompt,
        "result": file_path
    }