def predict_job_role(skills):
    
    skills = [skill.lower() for skill in skills]

    if "react" in skills or "javascript" in skills:
        return "Frontend Developer"

    elif "python" in skills and "machine learning" in skills:
        return "Machine Learning Engineer"

    elif "sql" in skills and "flask" in skills:
        return "Backend Developer"

    elif "python" in skills:
        return "Python Developer"

    else:
        return "Software Developer"