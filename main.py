from fastapi import FastAPI
from pydantic import BaseModel
from gtts import gTTS
import os
import uuid
from moviepy.editor import *
from fastapi.responses import FileResponse

app = FastAPI()

# Ensure directories exist
os.makedirs("static/audio", exist_ok=True)
os.makedirs("static/video", exist_ok=True)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "✅ Script to Video Backend is running!"}

@app.post("/generate-video/")
async def generate_video(request: TextRequest):
    text = request.text.strip()
    audio_filename = f"audio_{uuid.uuid4().hex}.mp3"
    audio_path = os.path.join("static/audio", audio_filename)

    # 1. Generate audio from text
    tts = gTTS(text)
    tts.save(audio_path)

    # 2. Generate video with text and audio
    video_filename = f"video_{uuid.uuid4().hex}.mp4"
    video_path = os.path.join("static/video", video_filename)

    # Create a text clip
    txt_clip = TextClip(
        text, fontsize=48, color='white', bg_color='black', size=(720, 480), method='caption'
    ).set_duration(AudioFileClip(audio_path).duration)

    # Set audio
    video = txt_clip.set_audio(AudioFileClip(audio_path))

    # Export video
    video.write_videofile(video_path, fps=24)

    return {"video_url": f"/static/video/{video_filename}"}
