from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Screening System",
    description="An AI-powered ATS Resume Screening Application",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Screening System 🚀"
    }