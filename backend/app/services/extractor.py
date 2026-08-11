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

    pattern = r'(?<!\d)(?:\+91[\s-]?|91[\s-]?)?[6-9]\d{9}(?!\d)'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"

def extract_skills(text: str):

    SKILLS = [
        "Python",
        "Java",
        "C++",
        "C",
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

def extract_education(text: str):

    EDUCATION_KEYWORDS = [
        "B.Tech",
        "B.E",
        "Bachelor of Technology",
        "Bachelor of Engineering",
        "M.Tech",
        "M.E",
        "MBA",
        "BCA",
        "MCA",
        "B.Sc",
        "M.Sc",
        "10th",
        "12th"
    ]

    found_education = []

    for education in EDUCATION_KEYWORDS:
        if education.lower() in text.lower():
            found_education.append(education)

    return found_education

def extract_experience_section(text: str):

    lines = text.splitlines()

    EXPERIENCE_HEADINGS = [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "career history"
    ]

    NEXT_SECTION_HEADINGS = [
        "education",
        "skills",
        "projects",
        "certifications",
        "achievements",
        "languages"
    ]

    experience_started = False
    experience_lines = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        line_lower = line.lower()

        # Start Experience section
        if line_lower in EXPERIENCE_HEADINGS:
            experience_started = True
            continue

        # Stop at next section
        if experience_started and line_lower in NEXT_SECTION_HEADINGS:
            break

        # Store experience content
        if experience_started:
            experience_lines.append(line)

    return experience_lines   

def extract_projects(text: str):

    PROJECT_HEADINGS = [
        "projects",
        "project",
        "academic projects",
        "personal projects",
        "key projects"
    ]

    NEXT_SECTION_HEADINGS = [
        "education",
        "experience",
        "work experience",
        "professional experience",
        "skills",
        "certifications",
        "achievements",
        "languages"
    ]

    lines = text.splitlines()

    project_started = False
    project_lines = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        line_lower = line.lower()

        # Start Projects section
        if line_lower in PROJECT_HEADINGS:
            project_started = True
            continue

        # Stop when next section starts
        if project_started and line_lower in NEXT_SECTION_HEADINGS:
            break

        # Store project content
        if project_started:
            project_lines.append(line)

    return project_lines


def extract_resume_details(text: str):

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience_section(text),
        "projects": extract_projects(text)
    }

# if __name__ == "__main__":

#     text = """
#     Experienced in JavaScript, React, Python and C++.
#     """

#     print(extract_skills(text))