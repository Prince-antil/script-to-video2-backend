from fastapi import FastAPI
from pydantic import BaseModel
from gtts import gTTS
from moviepy.editor import *
import os
import uuid

app = FastAPI()

class ScriptInput(BaseModel):
    text: str

os.makedirs("static", exist_ok=True)

@app.get("/")
def root():
    return {"message": "✅ Script to Video backend is running!"}

@app.post("/generate-video/")
async def generate_video(data: ScriptInput):
    text = data.text
    audio_path = f"static/audio_{uuid.uuid4().hex}.mp3"
    video_path = f"static/video_{uuid.uuid4().hex}.mp4"

    # Step 1: Generate audio using gTTS
    tts = gTTS(text)
    tts.save(audio_path)

    # Step 2: Generate video with text + audio
    clip_duration = AudioFileClip(audio_path).duration
    txt_clip = TextClip(text, fontsize=48, color='white', bg_color='black', size=(720, 480))
    txt_clip = txt_clip.set_duration(clip_duration)

    video = txt_clip.set_audio(AudioFileClip(audio_path))
    video.write_videofile(video_path, fps=24)

    return {"video_url": f"/{video_path}"}
