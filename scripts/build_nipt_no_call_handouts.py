from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "decks" / "nipt-no-call-labcorp"
OUT_DIR.mkdir(parents=True, exist_ok=True)


OPENMFM_NAVY = colors.HexColor("#07111C")
OPENMFM_BLUE = colors.HexColor("#003865")
OPENMFM_CYAN = colors.HexColor("#35D0FF")
OPENMFM_GOLD = colors.HexColor("#F2A900")
INK = colors.HexColor("#17212B")
MUTED = colors.HexColor("#5B6770")
LIGHT_BG = colors.HexColor("#F4F8FB")
PALE_CYAN = colors.HexColor("#EAF6FB")


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="HandoutTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=20,
        textColor=OPENMFM_BLUE,
        alignment=TA_LEFT,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="HandoutSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=11,
        textColor=MUTED,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionHeader",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10.2,
        leading=11.2,
        textColor=OPENMFM_BLUE,
        spaceBefore=3,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="BodySmall",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.4,
        leading=10.3,
        textColor=INK,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyPatient",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=11.4,
        textColor=INK,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="BulletSmall",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.3,
        leading=10.2,
        textColor=INK,
        leftIndent=10,
        firstLineIndent=0,
        bulletIndent=0,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="BulletPatient",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.1,
        leading=11.1,
        textColor=INK,
        leftIndent=10,
        firstLineIndent=0,
        bulletIndent=0,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="Callout",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=OPENMFM_BLUE,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="FooterSmall",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.5,
        leading=9,
        textColor=MUTED,
        spaceAfter=0,
    )
)


def bullet(text: str, style_name: str):
    return Paragraph(text, styles[style_name], bulletText="-")


def boxed_section(title: str, body_items: list[Paragraph], width: float):
    content = [Paragraph(title, styles["SectionHeader"])] + body_items
    table = Table([[content]], colWidths=[width])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#C8D7E3")),
                ("LINEBEFORE", (0, 0), (0, -1), 4, OPENMFM_CYAN),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def add_header(story: list, title: str, subtitle: str):
    story.append(Paragraph(title, styles["HandoutTitle"]))
    story.append(Paragraph(subtitle, styles["HandoutSubtitle"]))
    story.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=OPENMFM_GOLD,
            spaceBefore=0,
            spaceAfter=8,
        )
    )


def build_physician_pdf():
    path = OUT_DIR / "NIPT_Physician_Handout.pdf"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=letter,
        rightMargin=0.48 * inch,
        leftMargin=0.48 * inch,
        topMargin=0.46 * inch,
        bottomMargin=0.42 * inch,
    )

    story = []
    add_header(
        story,
        "When NIPT Goes Silent",
        "Physician one-pager | OpenMFM clinician summary | Chukwuma I. Onyeije, MD",
    )

    intro = Table(
        [[Paragraph(
            "This featured OpenMFM deck covers the operational and emotional cost of no-call NIPT results. The key clinical move is not reassurance. It is disciplined recovery of a decision pathway.",
            styles["BodySmall"],
        )]],
        colWidths=[7.1 * inch],
    )
    intro.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE_CYAN),
                ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#B8DCEE")),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(intro)
    story.append(Spacer(1, 8))

    col_width = 3.5 * inch
    left = [
        boxed_section(
            "Core message",
            [
                Paragraph(
                    "The high-friction clinical event is often the unclear result: low fetal fraction, atypical language, or specimen may be mosaic.",
                    styles["BodySmall"],
                ),
                Paragraph(
                    "A reportable result matters because it restores a clearer counseling and diagnostic pathway.",
                    styles["BodySmall"],
                ),
            ],
            col_width,
        ),
        Spacer(1, 7),
        boxed_section(
            "What to say in clinic",
            [
                bullet("cfDNA is screening, not diagnosis.", "BulletSmall"),
                bullet("cfDNA largely reflects placental DNA in maternal blood.", "BulletSmall"),
                bullet("No-call is not the same as screen-negative.", "BulletSmall"),
                bullet("Discordant or mosaic results require source-of-signal analysis.", "BulletSmall"),
                bullet("Diagnostic testing is needed when a definitive fetal answer will change management.", "BulletSmall"),
            ],
            col_width,
        ),
        Spacer(1, 7),
        boxed_section(
            "Low fetal fraction / no-call pathway",
            [
                bullet("Confirm gestational age, BMI, and sample details.", "BulletSmall"),
                bullet("Review or obtain ultrasound findings.", "BulletSmall"),
                bullet("Offer repeat screening only in selected settings.", "BulletSmall"),
                bullet("Escalate to genetics and diagnostic testing when ultrasound is abnormal, risk is high, or repeat failure occurs.", "BulletSmall"),
            ],
            col_width,
        ),
    ]

    right = [
        boxed_section(
            "How to frame platform comparison safely",
            [
                bullet("Say workflow fit, not universal superiority.", "BulletSmall"),
                bullet("Say a discrete result can clarify next steps.", "BulletSmall"),
                bullet("Use published data, not sales language.", "BulletSmall"),
                bullet("Do not imply that broader screening removes the need for diagnostic confirmation.", "BulletSmall"),
            ],
            col_width,
        ),
        Spacer(1, 7),
        boxed_section(
            "Cases that should slow you down",
            [
                bullet("Atypical result with normal ultrasound", "BulletSmall"),
                bullet("Specimen may be mosaic", "BulletSmall"),
                bullet("Positive screen with normal amnio", "BulletSmall"),
                bullet("Vanishing twin or multifetal gestation", "BulletSmall"),
                bullet("Genome-wide or multiple abnormality pattern", "BulletSmall"),
            ],
            col_width,
        ),
        Spacer(1, 7),
        boxed_section(
            "Three lines worth keeping",
            [
                Paragraph(
                    '<font color="#003865"><b>"No-call is a clinical incident, not a neutral event."</b></font>',
                    styles["BodySmall"],
                ),
                Paragraph(
                    '<font color="#003865"><b>"The value of a reportable result is often the recovery of a decision pathway."</b></font>',
                    styles["BodySmall"],
                ),
                Paragraph(
                    '<font color="#003865"><b>"Diagnostic testing assigns fetal truth."</b></font>',
                    styles["BodySmall"],
                ),
            ],
            col_width,
        ),
    ]

    story.append(
        Table(
            [[left, right]],
            colWidths=[3.58 * inch, 3.58 * inch],
            style=TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            ),
        )
    )
    story.append(Spacer(1, 7))
    story.append(
        Paragraph(
            "Guideline anchors: cfDNA is supported for common aneuploidy screening; positive and no-call results require counseling and diagnostic discussion; single-gene cfDNA screening is not currently recommended by ACOG.",
            styles["FooterSmall"],
        )
    )

    doc.build(story)
    return path


def build_patient_pdf():
    path = OUT_DIR / "NIPT_Patient_Handout.pdf"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=letter,
        rightMargin=0.52 * inch,
        leftMargin=0.52 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.45 * inch,
    )

    story = []
    add_header(
        story,
        "Understanding an Unclear NIPT Result",
        "Patient one-pager | OpenMFM plain-language summary",
    )

    story.append(
        KeepTogether(
            [
                Paragraph("What is NIPT?", styles["SectionHeader"]),
                Paragraph(
                    "NIPT is a blood test used in pregnancy. It looks at small pieces of DNA in the mother's blood. Most of that DNA comes from the placenta. This test is a screening test. It is not the same as a diagnostic test.",
                    styles["BodyPatient"],
                ),
            ]
        )
    )

    story.append(
        KeepTogether(
            [
                Paragraph("What does an unclear result mean?", styles["SectionHeader"]),
                bullet("The test did not give a clear answer.", "BulletPatient"),
                bullet("An unclear result is not a diagnosis.", "BulletPatient"),
            ]
        )
    )

    callout = Table(
        [[Paragraph(
            "Getting no result does NOT mean something is wrong with your baby. It means the test needs more information. Your doctor will work with you to get that answer.",
            styles["Callout"],
        )]],
        colWidths=[6.95 * inch],
    )
    callout.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BG),
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#C8D7E3")),
                ("LINEBEFORE", (0, 0), (0, -1), 5, OPENMFM_CYAN),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(callout)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Why can this happen?", styles["SectionHeader"]))
    story.extend(
        [
            bullet("There may not have been enough placental DNA in the blood sample.", "BulletPatient"),
            bullet("The pregnancy may be very early.", "BulletPatient"),
            bullet("The placenta may be giving a mixed or unclear signal.", "BulletPatient"),
            bullet("Sometimes the test sees something that needs more checking.", "BulletPatient"),
        ]
    )

    story.append(Paragraph("What happens next?", styles["SectionHeader"]))
    story.extend(
        [
            bullet("Your doctor may review your ultrasound.", "BulletPatient"),
            bullet("You may be offered another screening test.", "BulletPatient"),
            bullet("You may be offered diagnostic testing, such as CVS or amniocentesis, if you want a more definite answer.", "BulletPatient"),
            bullet("A genetics counselor may help explain your options.", "BulletPatient"),
        ]
    )

    story.append(Paragraph("Questions you can ask your doctor", styles["SectionHeader"]))
    question_table = Table(
        [
            [Paragraph("1. What exactly did my result say?", styles["BodyPatient"])],
            [Paragraph("2. Does my ultrasound change what this result means?", styles["BodyPatient"])],
            [Paragraph("3. Should I repeat the screening test, or should I think about diagnostic testing?", styles["BodyPatient"])],
            [Paragraph("4. What would the next test tell us?", styles["BodyPatient"])],
            [Paragraph("5. How urgent is this decision?", styles["BodyPatient"])],
        ],
        colWidths=[6.95 * inch],
    )
    question_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#D9E3EA")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E7EEF3")),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    story.append(question_table)
    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            "Bottom line: An unclear NIPT result can be stressful, but it is not a final diagnosis. Ask what the result means, what it does not mean, and what test or follow-up is best for you.",
            styles["BodyPatient"],
        )
    )

    doc.build(story)
    return path


def main():
    physician = build_physician_pdf()
    patient = build_patient_pdf()
    print(physician)
    print(patient)


if __name__ == "__main__":
    main()
