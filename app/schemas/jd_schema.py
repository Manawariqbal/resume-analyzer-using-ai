from pydantic import BaseModel


class JDMatchResponse(BaseModel):
    match_percentage: int
    strengths: list[str]
    missing_skills: list[str]
    recommendations: list[str]