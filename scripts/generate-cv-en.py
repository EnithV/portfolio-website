"""Generate CV-EGicela_Vargas_En.pdf with merged civil engineering experience."""

from pathlib import Path

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = Path(__file__).resolve().parent.parent / "CV-EGicela_Vargas_En.pdf"


def build_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=16,
            spaceAfter=2,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=12,
            spaceAfter=2,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11,
            spaceAfter=10,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=12,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            spaceAfter=6,
            alignment=TA_LEFT,
        ),
        "job_title": ParagraphStyle(
            "JobTitle",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=12,
            spaceBefore=4,
            spaceAfter=2,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11,
            leftIndent=12,
            bulletIndent=0,
            spaceAfter=2,
        ),
        "edu_line": ParagraphStyle(
            "EduLine",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11,
            spaceAfter=2,
        ),
    }


def job_block(story, styles, title, dates, bullets):
    story.append(Paragraph(f"{title} &nbsp;&nbsp;&nbsp;&nbsp; {dates}", styles["job_title"]))
    for bullet in bullets:
        story.append(Paragraph(f"• {bullet}", styles["bullet"]))


def main():
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
    )
    story = []

    story.append(Paragraph("ENITH GICELA VARGAS VARGAS", styles["name"]))
    story.append(
        Paragraph(
            "Full-Stack Developer | Java | Data Analyst | AI | Civil Engineer",
            styles["subtitle"],
        )
    )
    story.append(
        Paragraph(
            "ingegvargas@gmail.com | LinkedIn | Portfolio<br/>Bogotá, Colombia",
            styles["contact"],
        )
    )

    story.append(Paragraph("PROFESSIONAL SUMMARY", styles["section"]))
    story.append(
        Paragraph(
            "Java Full-Stack Developer with backend and frontend experience, including REST APIs "
            "with Java and Spring Boot and interfaces with JavaScript, HTML, and CSS. Civil Engineer "
            "and Environmental Specialist with experience in infrastructure project management, "
            "technical auditing, and regulatory compliance. Participated in LLM evaluation and "
            "optimization projects, strengthening skills in logic, data validation, and complex "
            "problem-solving. Brings analytical thinking, structured workflows, and adaptability "
            "across technology and engineering environments.",
            styles["body"],
        )
    )

    story.append(Paragraph("WORK EXPERIENCE", styles["section"]))

    job_block(
        story,
        styles,
        "LLM Trainer (Freelance)",
        "May 2024 – Mar 2026",
        [
            "Improved consistency and response quality in language models through prompt and dataset design and validation.",
            "Designed structured evaluation criteria that enabled reproducible results in technical tasks.",
            "Applied analytical and debugging logic to identify output errors and optimize results.",
            "Implemented responsible AI practices, helping reduce bias in training data.",
        ],
    )

    job_block(
        story,
        styles,
        "Civil Engineer – Independent Consultant",
        "Jun 2022 – Present",
        [
            "Planned and supervised construction and infrastructure projects.",
            "Oversaw technical, administrative, and environmental compliance.",
            "Analyzed technical and financial information to optimize project decision-making.",
        ],
    )

    job_block(
        story,
        styles,
        "Municipal Controller – San Eduardo Town Hall, Boyacá",
        "Aug 2019 – Dec 2019",
        [
            "Performed technical, administrative, and financial audits for water treatment plant maintenance contracts.",
        ],
    )

    job_block(
        story,
        styles,
        "Municipal Controller – Jericó Town Hall, Boyacá",
        "Dec 2017 – Feb 2018",
        [
            "Audited rural aqueduct rehabilitation projects, evaluating technical, financial, and administrative compliance.",
        ],
    )

    job_block(
        story,
        styles,
        "Inventory Inspector – Consorcio Intervial SV",
        "Oct 2016 – Feb 2017",
        [
            "Inspected urban road maintenance projects with technical, environmental, administrative, and financial auditing.",
        ],
    )

    job_block(
        story,
        styles,
        "Cadastre Coordinator – EMSER E.S.P",
        "Jun 2015 – Dec 2016",
        [
            "Coordinated the Aqueduct Micro-Metering Implementation Plan in Líbano, Tolima.",
            "Led data collection, report generation, and compliance documentation.",
        ],
    )

    story.append(Paragraph("KEY PROJECTS", styles["section"]))

    job_block(
        story,
        styles,
        "Style Factory | Generation Colombia | Full-Stack Developer",
        "Feb 2026 – Jun 2026",
        [
            "Developed a modular web application for service and booking management using JavaScript, HTML, CSS, and Bootstrap.",
            "Implemented user authentication, session management, an administrative dashboard, and dynamic loading of reusable components.",
        ],
    )

    job_block(
        story,
        styles,
        "Aurelion | Guayerd | Developer",
        "Jul 2025 – Dec 2025",
        [
            "Developed an end-to-end application with business logic, exploratory analysis, and predictive models for data processing and visualization.",
            "Implemented clustering techniques and automated documentation within the data pipeline.",
        ],
    )

    story.append(Paragraph("EDUCATION", styles["section"]))
    education = [
        ("Generation Colombia", "Full-Stack Java Development", "Feb 2026 – Jun 2026"),
        ("Guayerd / IBM", "Fundamentals of Artificial Intelligence and Data Analytics", "Jul 2025 – Dec 2025"),
        (
            "Universidad Pedagógica y Tecnológica de Colombia",
            "Environmental Engineering Specialist",
            "2015",
        ),
        (
            "Universidad Pedagógica y Tecnológica de Colombia",
            "Civil Engineering",
            "Dec 2014",
        ),
    ]
    for school, program, dates in education:
        story.append(Paragraph(f"<b>{school}</b> &nbsp;&nbsp;&nbsp;&nbsp; {dates}", styles["edu_line"]))
        story.append(Paragraph(program, styles["edu_line"]))

    story.append(Paragraph("SKILLS", styles["section"]))
    story.append(
        Paragraph(
            "Java | Spring Boot | Python | REST APIs | JavaScript | Node.js | HTML | CSS | Bootstrap | SQL | Git | GitHub | Power BI | Looker Studio | Excel | Technical Auditing | Project Compliance",
            styles["body"],
        )
    )

    story.append(Paragraph("LANGUAGES", styles["section"]))
    story.append(Paragraph("Spanish: Native | English: B2", styles["body"]))

    doc.build(story)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
