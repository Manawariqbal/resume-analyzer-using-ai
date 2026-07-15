from pydantic import BaseModel


class ResumeAnalysis(BaseModel):
    ats_score: int
    strengths: list[str]
    weaknesses: list[str]
    missing_skills: list[str]
    suggestions: list[str]