from fastapi import FastAPI
from routes.story import story_router  # ✅ relative import (works inside app/ folder)

app = FastAPI()

app.include_router(story_router, prefix="/story")

@app.get("/")
def root():
    return {"message": "Script to Video Backend is running"}

