from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from gtts import gTTS
from moviepy.editor import *
import os
import uuid

app = FastAPI()

# ✅ Make sure static folder exists
os.makedirs("static", exist_ok=True)

# ✅ Request model
class ScriptRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "✅ Script to Video Backend is running!"}

@app.post("/generate-video/")
async def generate_video(request: ScriptRequest):
    # Generate unique filenames
    uid = uuid.uuid4().hex
    audio_path = f"static/audio_{uid}.mp3"
    video_path = f"static/video_{uid}.mp4"

    # ✅ Generate voiceover using gTTS
    tts = gTTS(request.text)
    tts.save(audio_path)

    # ✅ Load audio duration
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration

    # ✅ Create background with subtitle text
    text_clip = TextClip(
        request.text,
        fontsize=36,
        color='black',
        size=(1280, 720),
        method='caption',
        align='center'
    ).set_duration(duration).set_position('center')

    background = ColorClip(size=(1280, 720), color=(255, 255, 255)).set_duration(duration)

    # ✅ Combine background, text, and audio
    final_video = CompositeVideoClip([background, text_clip]).set_audio(audio_clip)
    final_video.write_videofile(video_path, fps=24)

    return {"video_url": f"/static/video_{uid}.mp4"}
