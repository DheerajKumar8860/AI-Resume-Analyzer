required_skills = [

    "Python",
    "JavaScript",
    "React",
    "SQL",
    "Machine Learning",
    "Git",
    "Docker",
    "AWS"

]


def calculate_ats_score(extracted_skills):

    matched_skills = []

    missing_skills = []

    extracted_skills_lower = [
        skill.lower() for skill in extracted_skills
    ]

    for skill in required_skills:

        if skill.lower() in extracted_skills_lower:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    score = int(
        (len(matched_skills) / len(required_skills)) * 100
    )

    return score, missing_skills