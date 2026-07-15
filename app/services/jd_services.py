from app.schemas.jd_schema import JDMatchResponse
from app.services.ai_service import llm

structured_llm = llm.with_structured_output(
    JDMatchResponse
)


def compare_resume_with_jd(
    resume_text: str,
    job_description: str
):

    prompt = f"""
    Compare the resume with the job description.

    Return:

    - Match percentage
    - Strengths
    - Missing skills
    - Recommendations

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    response = structured_llm.invoke(prompt)

    return response