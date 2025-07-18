from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter
from pydantic import BaseModel
from gtts import gTTS
import os
import uuid

app = FastAPI()
router = APIRouter()

# ✅ Ensure the static folder exists
os.makedirs("static", exist_ok=True)

# ✅ Pydantic model for request body
class TextRequest(BaseModel):
    text: str

# ✅ POST endpoint to generate audio
@router.post("/generate-audio/")
async def generate_audio(request: TextRequest):
    text = request.text
    filename = f"output_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("static", filename)

    # Generate and save audio
    tts = gTTS(text)
    tts.save(filepath)

    return {"audio_url": f"/static/{filename}"}

# ✅ Root health check endpoint
@app.get("/")
def root():
    return {"message": "✅ Script to Video Backend is running!"}

# ✅ Register router
app.include_router(router)

# ✅ Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")
