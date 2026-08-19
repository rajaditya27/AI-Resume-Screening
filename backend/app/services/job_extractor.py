import re


SKILLS = [
    "Python",
    "Java",
    "C++",
    "C",
    "FastAPI",
    "SQL",
    "PostgreSQL",
    "MySQL",
    "AWS",
    "Docker",
    "Git",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js"
]


def extract_job_skills(text: str):

    found_skills = []

    for skill in SKILLS:

        if skill == "C++":
            pattern = r"(?<!\w)C\+\+(?!\w)"

        elif skill == "C":
            pattern = r"(?<!\w)C(?!\w)"

        else:
            pattern = rf"(?<!\w){re.escape(skill)}(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills
def extract_experience_required(text: str):

    patterns = [
        r'(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s*)?(?:experience|work experience)',
        r'(?:experience|work experience)\s*(?:of\s*)?(\d+)\+?\s*(?:years?|yrs?)'
    ]

    for pattern in patterns:

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return f"{match.group(1)} years"

    return "Not Specified"
def extract_job_details(text: str):

    return {
        "required_skills": extract_job_skills(text),
        "experience_required": extract_experience_required(text)
    }