from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfplumber

from skills import skills_list
from ats_score import calculate_ats_score
from job_roles import predict_job_role
from jd_matcher import calculate_jd_match
from suggestions import generate_suggestions
from ranking import rank_resume
from career_recommender import recommend_careers
from career_skills import get_career_skills
from pdf_generator import generate_pdf_report
from ml_predictor import predict_resume_role
from skill_gap import analyze_skill_gap

app = Flask(__name__)

CORS(app)

synonyms = {

    "ml": "machine learning",

    "ai": "artificial intelligence",

    "js": "javascript",

    "py": "python"

}


def semantic_matching(text):

    text = text.lower()

    for short_form, full_form in synonyms.items():

        text = text.replace(
            short_form,
            full_form
        )

    return text


@app.route('/')
def home():

    return "AI Resume Analyzer Backend Running Successfully!"


@app.route('/upload', methods=['POST'])
def upload_resume():

    if 'resume' not in request.files:

        return jsonify({
            "message": "No file uploaded"
        })

    file = request.files['resume']

    job_description = request.form.get(
        "job_description",
        ""
    )

    extracted_text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                extracted_text += text

    extracted_skills = []

    extracted_text = semantic_matching(
        extracted_text
    )

    job_description = semantic_matching(
        job_description
    )

    for skill in skills_list:

        if skill.lower() in extracted_text.lower():

            extracted_skills.append(skill)

    ats_score, missing_skills = calculate_ats_score(
        extracted_skills
    )

    predicted_role = predict_resume_role(
    extracted_text
)

    jd_match_score = calculate_jd_match(
        extracted_text,
        job_description
    )

    suggestions = generate_suggestions(
        missing_skills
    )

    resume_rank = rank_resume(
        ats_score
    )
    career_recommendations = recommend_careers(
    extracted_skills
)
    pdf_report = generate_pdf_report(

    ats_score,
    predicted_role,
    resume_rank,
    extracted_skills,
    missing_skills,
    suggestions

)

    return jsonify({

        "message": "Resume uploaded successfully!",

        "resume_text": extracted_text,

        "skills": extracted_skills,

        "ats_score": ats_score,

        "missing_skills": missing_skills,

        "predicted_role": predicted_role,

        "jd_match_score": jd_match_score,

        "suggestions": suggestions,

        "resume_rank": resume_rank,

        "career_recommendations": career_recommendations,

        "pdf_report": pdf_report

    })
@app.route('/career-skills', methods=['POST'])
def career_skills():

    data = request.json

    role = data.get(
        "role",
        ""
    )

    skills = get_career_skills(role)

    return jsonify({

        "role": role,

        "skills": skills

    })
@app.route('/skill-gap', methods=['POST'])
def skill_gap():

    data = request.json

    user_skills = data.get(
        "skills",
        []
    )

    target_role = data.get(
        "target_role",
        ""
    )

    missing_skills = analyze_skill_gap(

        user_skills,

        target_role

    )

    return jsonify({

        "missing_skills": missing_skills

    })

if __name__ == '__main__':

    app.run(debug=True)
