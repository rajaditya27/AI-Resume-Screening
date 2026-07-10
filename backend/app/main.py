from fastapi import FastAPI
from app.models.user import User

from app.database.database import engine,Base

app = FastAPI(
    title="AI Resume Screening System",
    description="An AI-powered ATS Resume Screening Application",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Screening System 🚀"
    }