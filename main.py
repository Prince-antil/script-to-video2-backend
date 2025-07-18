from fastapi import FastAPI
from routes.story import story_router

app = FastAPI()
app.include_router(story_router)
