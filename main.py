from fastapi import FastAPI, UploadFile, File
from utils.audio_generator import generate_audio_from_text

app = FastAPI()

@app.post("/generate-audio/")
async def generate_audio(text: str):
    return generate_audio_from_text(text)


