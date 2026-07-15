from fastapi import FastAPI

from app.api.resume import router as resume_router

app = FastAPI(
    title="AI Resume Analyzer",
    version="1.0.0"
)

app.include_router(resume_router)

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer Running"
    }