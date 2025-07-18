from fastapi import FastAPI
from app.routes.story import story_router  # ✅ FIXED IMPORT

app = FastAPI()

# Mount your story routes
app.include_router(story_router, prefix="/story")

@app.get("/")
def root():
    return {"message": "Script to Video Backend is running"}
