from pydantic import BaseModel
from typing import List


class JobDescription(BaseModel):
    job_title: str
    description: str
    required_skills: List[str] = []
    experience_required: str = ""