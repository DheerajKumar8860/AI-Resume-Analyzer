import streamlit as st
import pdfplumber
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

.main-title {
    text-align: center;
    color: #38bdf8;
    font-size: 52px;
    font-weight: bold;
    margin-top: 10px;
}

.sub-title {
    text-align: center;
    color: #cbd5e1;
    font-size: 20px;
    margin-bottom: 40px;
}

.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    margin-bottom: 15px;
}

.card h3 {
    color: #94a3b8;
    margin-bottom: 10px;
}

.card h1 {
    color: white;
    font-size: 32px;
}

.skill-box {
    background-color: #2563eb;
    color: white;
    padding: 8px 14px;
    border-radius: 10px;
    display: inline-block;
    margin: 5px;
    font-size: 14px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SKILLS LIST ---------------- #

skills_list = [
    "Python",
    "Machine Learning",
    "Data Science",
    "Artificial Intelligence",
    "Deep Learning",
    "Flask",
    "React",
    "SQL",
    "JavaScript",
    "TensorFlow",
    "Pandas",
    "Numpy",
    "HTML",
    "CSS",
    "Java",
    "C++"
]

# ---------------- CAREER PATHS ---------------- #

career_paths = {
    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow"
    ],

    "Data Scientist": [
        "Python",
        "Data Science",
        "SQL",
        "Pandas"
    ],

    "AI Engineer": [
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning"
    ],

    "Frontend Developer": [
        "React",
        "JavaScript",
        "HTML",
        "CSS"
    ]
}

# ---------------- TITLE ---------------- #

st.markdown(
    '<h1 class="main-title">🤖 AI Resume Analyzer</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Smart ATS & Career Recommendation System</p>',
    unsafe_allow_html=True
)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

# ---------------- JOB DESCRIPTION ---------------- #

job_description = st.text_area(
    "📝 Paste Job Description"
)

# ---------------- MAIN LOGIC ---------------- #

if uploaded_file is not None:

    extracted_text = ""

    try:

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text

    except Exception as e:

        st.error(f"Error reading PDF: {e}")
        st.stop()

    # ---------------- SKILL EXTRACTION ---------------- #

    extracted_skills = []

    for skill in skills_list:

        if skill.lower() in extracted_text.lower():

            extracted_skills.append(skill)

    # Remove duplicates
    extracted_skills = list(set(extracted_skills))

    # ---------------- ATS SCORE ---------------- #

    ats_score = min(len(extracted_skills) * 10, 100)

    # ---------------- JOB DESCRIPTION MATCH ---------------- #

    jd_match = 0

    if job_description:

        matched_words = 0

        for skill in extracted_skills:

            if skill.lower() in job_description.lower():
                matched_words += 1

        jd_match = min(matched_words * 10, 100)

    # ---------------- ROLE PREDICTION ---------------- #

    predicted_role = "General Developer"

    if "Machine Learning" in extracted_skills:
        predicted_role = "Machine Learning Engineer"

    elif "Data Science" in extracted_skills:
        predicted_role = "Data Scientist"

    elif "React" in extracted_skills:
        predicted_role = "Frontend Developer"

    elif "Artificial Intelligence" in extracted_skills:
        predicted_role = "AI Engineer"

    # ---------------- CAREER RECOMMENDATIONS ---------------- #

    recommended_paths = []

    for role, required_skills in career_paths.items():

        common_skills = set(required_skills).intersection(
            set(extracted_skills)
        )

        if len(common_skills) >= 2:
            recommended_paths.append(role)

    # ---------------- MISSING SKILLS ---------------- #

    target_skills = career_paths.get(predicted_role, [])

    missing_skills = []

    for skill in target_skills:

        if skill not in extracted_skills:
            missing_skills.append(skill)

    # ---------------- RESUME RANK ---------------- #

    if ats_score >= 80:
        rank = "Excellent"

    elif ats_score >= 60:
        rank = "Good"

    elif ats_score >= 40:
        rank = "Average"

    else:
        rank = "Needs Improvement"

    # ---------------- DASHBOARD ---------------- #

    st.markdown("## 📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>ATS Score</h3>
            <h1>{ats_score}%</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <h3>Predicted Role</h3>
            <h1>{predicted_role}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <h3>Resume Rank</h3>
            <h1>{rank}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="card">
            <h3>JD Match</h3>
            <h1>{jd_match}%</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- EXTRACTED SKILLS ---------------- #

    st.subheader("🛠 Extracted Skills")

    if extracted_skills:

        for skill in extracted_skills:

            st.markdown(
                f'<span class="skill-box">{skill}</span>',
                unsafe_allow_html=True
            )

    else:

        st.warning("No skills detected.")

    st.markdown("---")

    # ---------------- CAREER PATHS ---------------- #

    st.subheader("🚀 Recommended Career Paths")

    if recommended_paths:

        for role in recommended_paths:
            st.success(role)

    else:

        st.warning("No recommendation found.")

    st.markdown("---")

    # ---------------- MISSING SKILLS ---------------- #

    st.subheader("❌ Missing Skills")

    if missing_skills:

        for skill in missing_skills:
            st.error(skill)

    else:

        st.success("No missing skills detected.")

    st.markdown("---")

    # ---------------- CHARTS ---------------- #

    if extracted_skills:

        st.subheader("📈 Skills Analytics")

        skill_df = pd.DataFrame({
            "Skill": extracted_skills,
            "Value": [1] * len(extracted_skills)
        })

        pie_chart = px.pie(
            skill_df,
            names="Skill",
            values="Value",
            title="Skills Distribution"
        )

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

        bar_chart = px.bar(
            skill_df,
            x="Skill",
            y="Value",
            title="Skills Bar Chart"
        )

        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

    st.markdown("---")

    # ---------------- RESUME CONTENT ---------------- #

    with st.expander("📄 Resume Content"):

        st.write(extracted_text)

else:

    st.info("📌 Upload your resume to start analysis.")