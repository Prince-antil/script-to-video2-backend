from gtts import gTTS
import os
from uuid import uuid4

def text_to_speech(text: str) -> str:
    filename = f"{uuid4().hex}.mp3"
    path = os.path.join("output", filename)
    os.makedirs("output", exist_ok=True)
    tts = gTTS(text)
    tts.save(path)
    return path
