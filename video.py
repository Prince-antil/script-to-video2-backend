from moviepy.editor import *
import os
from uuid import uuid4

def generate_video_from_text(text: str, audio_path: str) -> str:
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{uuid4().hex}.mp4"
    output_path = os.path.join(output_dir, filename)

    clip = TextClip(text, fontsize=24, color='white', size=(1280, 720)).set_duration(10)
    audioclip = AudioFileClip(audio_path)
    videoclip = clip.set_audio(audioclip)
    videoclip.write_videofile(output_path, fps=24)

    return output_path
