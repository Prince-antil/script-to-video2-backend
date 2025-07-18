from fastapi import APIRouter, UploadFile, File, Form
from app.services.speech import text_to_speech
from app.services.parser import extract_text_from_docx
from app.services.video import generate_video_from_text
import os

story_router = APIRouter()

@story_router.post("/process/")
async def process_story(
    story_text: str = Form(None),
    story_file: UploadFile = File(None),
    generate_video: bool = Form(False)
):
    if story_file:
        text = extract_text_from_docx(await story_file.read())
    elif story_text:
        text = story_text
    else:
        return {"error": "No story text or file provided."}

    audio_path = text_to_speech(text)

    video_path = None
    if generate_video:
        video_path = generate_video_from_text(text, audio_path)

    return {
        "message": "Success",
        "audio_path": audio_path,
        "video_path": video_path
    }
