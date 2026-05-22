from fpdf import FPDF


def generate_pdf_report(

    ats_score,
    predicted_role,
    resume_rank,
    skills,
    missing_skills,
    suggestions

):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=14
    )

    pdf.cell(
        200,
        10,
        txt="AI Resume Analyzer Report",
        ln=True,
        align='C'
    )

    pdf.ln(10)

    pdf.cell(
        200,
        10,
        txt=f"ATS Score: {ats_score}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Predicted Role: {predicted_role}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Resume Ranking: {resume_rank}",
        ln=True
    )

    pdf.ln(10)

    pdf.cell(
        200,
        10,
        txt="Detected Skills:",
        ln=True
    )

    for skill in skills:

        pdf.cell(
            200,
            10,
            txt=f"- {skill}",
            ln=True
        )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        txt="Missing Skills:",
        ln=True
    )

    for skill in missing_skills:

        pdf.cell(
            200,
            10,
            txt=f"- {skill}",
            ln=True
        )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        txt="Suggestions:",
        ln=True
    )

    for suggestion in suggestions:

        pdf.multi_cell(
            0,
            10,
            txt=f"- {suggestion}"
        )

    pdf.output(
        "resume_report.pdf"
    )

    return "resume_report.pdf"