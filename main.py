from fastapi import FastAPI
from pydantic import BaseModel
from gtts import gTTS
import os
import uuid

app = FastAPI()

# Define request body model
class TextRequest(BaseModel):
    text: str

# Make sure the static directory exists
os.makedirs("static", exist_ok=True)

@app.post("/generate-audio/")
async def generate_audio(request: TextRequest):
    text = request.text
    filename = f"output_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("static", filename)

    # Generate audio using gTTS
    tts = gTTS(text)
    tts.save(filepath)

    return {"audio_url": f"/static/{filename}"}

