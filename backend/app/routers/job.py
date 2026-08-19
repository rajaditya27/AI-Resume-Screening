from fastapi import APIRouter
from app.schemas.job import JobDescription
from app.services.job_extractor import extract_job_details

router = APIRouter()


@router.post("/job")
def create_job(job: JobDescription):

    extracted_details = extract_job_details(job.description)

    return {
        "message": "Job Description processed successfully",
        "job_title": job.job_title,
        "description": job.description,
        "required_skills": extracted_details["required_skills"],
        "experience_required": extracted_details["experience_required"]
    }