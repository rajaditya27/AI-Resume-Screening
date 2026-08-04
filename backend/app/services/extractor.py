import re

def extract_name(text: str):

    lines=text.splitlines()
    for line in lines:
        line=line.strip()
        if line:
            return line
    return "Not Found"

def extract_email(text: str):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()
    return "Not Found"

def extract_phone(text: str):

    pattern = r'(\+91[\-\s]?)?[0]?(91)?[789]\d{9}'

    match = re.search(pattern, text)

    if match:
        return match.group()
    return "Not Found"

def extract_skills(text: str):

    SKILLS = [
        "Python",
        "Java",
        "C",
        "C++",
        "FastAPI",
        "SQL",
        "AWS",
        "Docker",
        "Git",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js"
    ]

    found_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills

def extract_resume_details(text: str):

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }