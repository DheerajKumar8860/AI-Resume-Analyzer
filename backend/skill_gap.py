role_skills = {

    "AI Engineer": [

        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "NLP"

    ],

    "Data Scientist": [

        "Python",
        "Pandas",
        "NumPy",
        "Statistics",
        "Machine Learning",
        "SQL"

    ],

    "Frontend Developer": [

        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Tailwind CSS"

    ],

    "Backend Developer": [

        "Python",
        "Flask",
        "Django",
        "SQL",
        "MongoDB"

    ]

}


def analyze_skill_gap(

    user_skills,

    target_role

):

    required_skills = role_skills.get(

        target_role,

        []

    )

    missing_skills = []

    for skill in required_skills:

        if skill not in user_skills:

            missing_skills.append(skill)

    return missing_skills