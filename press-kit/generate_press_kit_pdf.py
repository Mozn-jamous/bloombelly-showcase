"""
Generate a professional press-kit PDF for BloomBelly.
Single-page, designed for sharing with grant reviewers, accelerators, investors.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.pdfgen import canvas


# ---- Brand colors ----
NAVY = HexColor("#214782")
ACCENT = HexColor("#4267B2")
LIGHT_BG = HexColor("#F2F4F8")
WARM = HexColor("#B45F06")
DARK_TEXT = HexColor("#1F2937")
GREY = HexColor("#6B7280")


# ---- Styles ----
styles = getSampleStyleSheet()

TITLE = ParagraphStyle(
    "Title", parent=styles["Title"],
    fontName="Helvetica-Bold", fontSize=28,
    textColor=NAVY, alignment=TA_LEFT,
    spaceAfter=2,
)

SUBTITLE = ParagraphStyle(
    "Subtitle", parent=styles["Normal"],
    fontName="Helvetica", fontSize=11,
    textColor=ACCENT, alignment=TA_LEFT,
    spaceAfter=10,
)

TAGLINE = ParagraphStyle(
    "Tagline", parent=styles["Normal"],
    fontName="Helvetica-Oblique", fontSize=10,
    textColor=GREY, alignment=TA_LEFT,
    spaceAfter=14,
)

H_SECTION = ParagraphStyle(
    "HSection", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=11,
    textColor=NAVY, alignment=TA_LEFT,
    spaceBefore=6, spaceAfter=4,
)

BODY = ParagraphStyle(
    "Body", parent=styles["Normal"],
    fontName="Helvetica", fontSize=9,
    textColor=DARK_TEXT, alignment=TA_LEFT,
    leading=12, spaceAfter=4,
)

BODY_SMALL = ParagraphStyle(
    "BodySmall", parent=BODY,
    fontSize=8, leading=10, textColor=GREY,
)

BULLET = ParagraphStyle(
    "Bullet", parent=BODY,
    leftIndent=10, bulletIndent=0,
    spaceAfter=2,
)

ACCENT_TEXT = ParagraphStyle(
    "Accent", parent=BODY,
    textColor=WARM, fontName="Helvetica-Bold",
)

FOOTER = ParagraphStyle(
    "Footer", parent=styles["Normal"],
    fontName="Helvetica-Oblique", fontSize=8,
    textColor=GREY, alignment=TA_CENTER,
)


def make_box(content, bg=LIGHT_BG, border=True):
    """Wrap content in a soft-background box."""
    t = Table([[content]], colWidths=[None])
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]
    if border:
        style.append(("BOX", (0, 0), (-1, -1), 0.5, NAVY))
    t.setStyle(TableStyle(style))
    return t


def header_band(canvas_obj, doc):
    """Draw a navy band at the top and brand info."""
    canvas_obj.saveState()
    width, height = A4
    # Top band
    canvas_obj.setFillColor(NAVY)
    canvas_obj.rect(0, height - 18*mm, width, 18*mm, fill=1, stroke=0)
    # Title in band
    canvas_obj.setFillColor(white)
    canvas_obj.setFont("Helvetica-Bold", 14)
    canvas_obj.drawString(20*mm, height - 12*mm, "BloomBelly — Press Kit")
    canvas_obj.setFont("Helvetica-Oblique", 9)
    canvas_obj.drawRightString(width - 20*mm, height - 12*mm,
                               "Graduation Project · ASPU · 2026")
    # Footer
    canvas_obj.setFillColor(GREY)
    canvas_obj.setFont("Helvetica-Oblique", 7)
    canvas_obj.drawCentredString(width / 2, 10*mm,
        "github.com/Mozn-jamous/bloombelly-showcase · asaierafi@clinlab.ai · linkedin.com/in/mozn-jamous")
    canvas_obj.restoreState()


# ---- Build ----
doc = SimpleDocTemplate(
    r"c:\Users\mesho\OneDrive\Desktop\portfolio-showcase\bloombelly-showcase\press-kit\BloomBelly-Press-Kit.pdf",
    pagesize=A4,
    topMargin=25*mm, bottomMargin=15*mm,
    leftMargin=16*mm, rightMargin=16*mm,
    title="BloomBelly Press Kit",
    author="Mozn Jamous & Shahd Bureghsh",
)

flow = []

# --- HEADER ---
flow.append(Paragraph("🌸 BloomBelly", TITLE))
flow.append(Paragraph(
    "AI-Assisted, Arabic-First Maternal & Child Health Platform", SUBTITLE))
flow.append(Paragraph(
    "Graduation Thesis · College of Informatics Engineering · "
    "Al-Sham Private University (ASPU) · Damascus, Syria · 2026", TAGLINE))

# --- 2-col layout: Problem & Solution ---
problem_html = (
    "<b>The Problem.</b> Maternal and child mortality in Arabic-speaking "
    "regions is among the world's highest. Most digital health apps are "
    "English-first; translations are mechanical; fathers have no clear "
    "role; information is contradictory. This documentably increases "
    "anxiety and delays detection of warning signs during the highest-leverage "
    'health window known: the "first 1,000 days."'
)

solution_html = (
    "<b>The Solution.</b> BloomBelly unifies pregnancy tracking, AI medical "
    "image analysis, evidence-based fetal movement monitoring, nutrition "
    "evaluation, and a dedicated father module under one Arabic-first interface. "
    "Three specialized AI components — Gemini for medical images, a LoRA-tuned "
    "transformer for the chatbot, and a Random Forest classifier for "
    "nutrition — operate behind a Python Flask backend with Supabase persistence."
)

problem_p = Paragraph(problem_html, BODY)
solution_p = Paragraph(solution_html, BODY)

two_col = Table(
    [[problem_p, solution_p]],
    colWidths=[(A4[0] - 32*mm) / 2 - 4*mm, (A4[0] - 32*mm) / 2 - 4*mm],
    style=TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]),
)
flow.append(two_col)
flow.append(Spacer(1, 8))

# --- Evidence-based feature box ---
flow.append(Paragraph("📚 Evidence-Based Foundation", H_SECTION))
ev_data = [
    ["Feature", "Reference"],
    ["Kick counter (ACOG-aligned)", "Saastad et al., PLOS ONE (2011, RCT, n=1076)"],
    ["Reduced movement awareness", "Weller et al., PLOS Global Public Health (2023)"],
    ["Partner support", "Versele et al., Frontiers in Public Health (2022)"],
    ["Maternal nutrition", "WHO Guidelines · King (2016)"],
    ["Pediatric sleep", "Paruthi et al., AASM (2016)"],
    ["Vaccination schedules", "Syrian Ministry of Health · WHO EPI"],
]
ev_table = Table(ev_data, colWidths=[5.5*cm, 11*cm])
ev_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_BG, white]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
]))
flow.append(ev_table)
flow.append(Spacer(1, 8))

# --- Three info boxes: SDGs / Market / Team ---
sdgs_p = Paragraph(
    "<b>🌍 SDG Alignment</b><br/>"
    "• SDG 3 — Good Health (3.1, 3.2, 3.7, 3.8)<br/>"
    "• SDG 5 — Gender Equality (5.6, 5.b)<br/>"
    "• SDG 10 — Reduced Inequalities (10.2)<br/>"
    "• SDG 4 — Quality Education (4.7)",
    BODY)

market_p = Paragraph(
    "<b>📊 Market</b><br/>"
    "• <b>TAM:</b> ~5.6M annual pregnancies (Arab League, smartphone-equipped)<br/>"
    "• <b>SAM:</b> $8M–$15M (Levant + Gulf + Egypt)<br/>"
    "• <b>SOM (3 yr):</b> $1.6M–$4.5M<br/>"
    "• <b>Distribution:</b> Clinic partnerships",
    BODY)

team_p = Paragraph(
    "<b>👥 Team</b><br/>"
    "• <b>Mozn Jamous</b> — Backend, AI, architecture<br/>"
    "• <b>Shahd Bureghsh</b> — Frontend, UX, product<br/>"
    "• <b>Dr. Afaf Al-Shalabi</b> — Principal Supervisor<br/>"
    "• <b>Eng. Rahaf Abdul Qader</b> — Technical Supervisor",
    BODY)

triple_col = Table(
    [[make_box(sdgs_p), make_box(market_p), make_box(team_p)]],
    colWidths=[(A4[0] - 32*mm) / 3 - 3*mm] * 3,
    style=TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]),
)
flow.append(triple_col)
flow.append(Spacer(1, 8))

# --- Tech Stack ---
flow.append(Paragraph("🧰 Technology Stack", H_SECTION))
tech_data = [
    ["Layer", "Choice", "Why"],
    ["Mobile", "Flutter (MVVM + Provider)", "Single codebase, mature Arabic typography"],
    ["Backend", "Python Flask", "Native ecosystem for AI orchestration"],
    ["Medical AI", "Google Gemini API", "Strong multimodal image analysis"],
    ["Chatbot", "LoRA fine-tuned transformer", "Lightweight domain specialization"],
    ["Nutrition", "Random Forest (scikit-learn)", "Interpretable, deterministic, fast"],
    ["Database", "Supabase (PostgreSQL + RLS)", "Realtime sync, robust auth, free tier"],
    ["Auth", "JWT + bcrypt", "Stateless, industry-standard"],
]
tech_table = Table(tech_data, colWidths=[2.5*cm, 5*cm, 9*cm])
tech_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_BG, white]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
]))
flow.append(tech_table)
flow.append(Spacer(1, 8))

# --- CTA ---
cta_p = Paragraph(
    "<b>We are actively seeking:</b><br/>"
    "Digital health grants (Grand Challenges, UNICEF, WHO) · "
    "Accelerator partnerships (Plug and Play Health, Flat6Labs, Misk, MBRF) · "
    "Research collaborations on Arabic medical NLP · "
    "Letters of support and pilot clinics in the Levant and Gulf regions.",
    BODY)
flow.append(make_box(cta_p, bg=HexColor("#FFF8E1"), border=True))

# --- Closing ---
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<i>Maternal and child health is the single highest-leverage investment "
    "any society can make. BloomBelly is our contribution to that investment, "
    "built in the region we know best, for the population that has been "
    "underserved by global digital health to date.</i>",
    BODY_SMALL))

doc.build(flow, onFirstPage=header_band, onLaterPages=header_band)
print(f"Generated: BloomBelly-Press-Kit.pdf")
