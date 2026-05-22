career_data = {

    "ai engineer": [

        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "NLP",
        "SQL"

    ],

    "data scientist": [

        "Python",
        "Statistics",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "SQL"

    ],

    "frontend developer": [

        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Tailwind CSS"

    ],

    "backend developer": [

        "Python",
        "Flask",
        "Django",
        "Node.js",
        "SQL",
        "MongoDB"

    ],

    "cloud engineer": [

        "AWS",
        "Docker",
        "Linux",
        "Kubernetes"

    ]

}


def get_career_skills(role):

    role = role.lower()

    return career_data.get(

        role,

        ["No data available"]

    )