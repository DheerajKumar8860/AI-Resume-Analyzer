def recommend_careers(skills):
    
    skills = [skill.lower() for skill in skills]

    recommendations = []

    # AI / ML Careers
    if (
        "python" in skills
        or "machine learning" in skills
        or "deep learning" in skills
        or "artificial intelligence" in skills
    ):

        recommendations.append("AI Engineer")
        recommendations.append("Data Scientist")
        recommendations.append("ML Engineer")

    # Web Development
    if (
        "html" in skills
        or "css" in skills
        or "javascript" in skills
        or "react" in skills
    ):

        recommendations.append("Frontend Developer")
        recommendations.append("UI/UX Developer")

    # Backend
    if (
        "flask" in skills
        or "django" in skills
        or "sql" in skills
    ):

        recommendations.append("Backend Developer")
        recommendations.append("API Developer")

    # Cloud / DevOps
    if (
        "aws" in skills
        or "docker" in skills
        or "linux" in skills
    ):

        recommendations.append("Cloud Engineer")
        recommendations.append("DevOps Engineer")

    # Default recommendation
    if len(recommendations) == 0:

        recommendations.append(
            "Software Developer"
        )

    return list(set(recommendations))