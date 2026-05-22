def compare_resumes(resume_scores):
    
    sorted_resumes = sorted(

        resume_scores,

        key=lambda x: x["score"],

        reverse=True

    )

    return sorted_resumes