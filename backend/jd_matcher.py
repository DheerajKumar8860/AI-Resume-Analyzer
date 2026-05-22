def calculate_jd_match(resume_text, job_description):
    
    resume_words = set(resume_text.lower().split())

    jd_words = set(job_description.lower().split())

    matched_words = resume_words.intersection(jd_words)

    if len(jd_words) == 0:
        return 0

    match_score = int(
        (len(matched_words) / len(jd_words)) * 100
    )

    return match_score