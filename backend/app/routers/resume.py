from fastapi import APIRouter, UploadFile, File, HTTPException,Depends
import shutil
import os
import uuid
from app.utils.auth import get_current_user
from app.models.user import User
from app.services.parser import extract_text, extract_docx_text
from app.services.extractor import extract_resume_details

router = APIRouter()

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):

    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX, and TXT files are allowed."
        )
    
    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    #extract text based on file type
    if file_extension ==".pdf":
        extracted_text = extract_text(file_path)

    elif file_extension ==".docx":
        extracted_text = extract_docx_text(file_path)
    else:
        extracted_text = ""
    resume_details = extract_resume_details(extracted_text)
   
    return {
        "message": "Resume uploaded successfully",
        "uploaded_by": current_user.name,
        "email":current_user.email,
        "stored_filename": unique_filename,
        "orginal_filename": file.filename,
        "resume_details": resume_details
    }

    