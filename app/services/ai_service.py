import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from app.schemas.resume_schema import ResumeAnalysis
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

structured_llm = llm.with_structured_output(
    ResumeAnalysis
)


def analyze_resume(resume_text: str):

    prompt = f"""
    Analyze this resume.

    Provide:
    - ATS score
    - strengths
    - weaknesses
    - missing skills
    - suggestions

    Resume:
    {resume_text}
    """

    response = structured_llm.invoke(prompt)

    return response