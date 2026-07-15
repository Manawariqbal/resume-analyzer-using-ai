from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
from fastapi import Form

from app.services.jd_services import compare_resume_with_jd
from app.services.file_services import save_file
from app.services.pdf_service import extract_text_from_pdf
from app.services.ai_service import analyze_resume

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # Save PDF
    file_path = await save_file(file)

    # Extract Text
    resume_text = extract_text_from_pdf(file_path)

    # Analyze Resume using Groq + LangChain
    analysis = analyze_resume(resume_text)

    return {
    "message": "Resume uploaded and analyzed successfully",
    "filename": file.filename,
    "analysis": analysis.model_dump()
}
@router.post("/match-jd")
async def match_jd(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # Save Resume
    file_path = await save_file(file)

    # Extract Resume Text
    resume_text = extract_text_from_pdf(file_path)

    # Compare Resume vs JD
    analysis = compare_resume_with_jd(
        resume_text=resume_text,
        job_description=job_description
    )

    return {
        "message": "Resume matched successfully",
        "filename": file.filename,
        "analysis": analysis.model_dump()
    }