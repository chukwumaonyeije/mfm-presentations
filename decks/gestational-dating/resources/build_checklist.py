"""Rebuild the single-page OpenMFM EDD checklist (requires reportlab)."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

HERE = Path(__file__).resolve().parent
PDF = HERE / 'edd-verification-checklist.pdf'
INK = HexColor('#172b3a')
TEAL = HexColor('#006778')
GRAY = HexColor('#40515e')
LINE = HexColor('#afbbc3')
c = canvas.Canvas(str(PDF), pagesize=(612, 792))
c.setTitle('EDD Verification Checklist | OpenMFM')
c.setAuthor('Dr. Chukwuma Onyeije, MD | Atlanta Perinatal Associates')
c.setSubject('One-page clinical checklist and dating documentation template')
c.setFillColor(TEAL)
c.rect(36, 748, 540, 4, fill=1, stroke=0)

def text(x, y, content, size=10, bold=False, color=INK):
    c.setFillColor(color)
    c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    c.drawString(x, y, content)

def para(x, top, content, width=540, size=9.5, leading=12):
    p = Paragraph(content, ParagraphStyle('body', fontName='Helvetica', fontSize=size,
                   leading=leading, textColor=INK))
    _, h = p.wrap(width, 700)
    p.drawOn(c, x, top-h)
    return top-h

def check(x, top, content, width=252):
    c.setStrokeColor(GRAY)
    c.setLineWidth(.7)
    c.rect(x, top-9, 7, 7, fill=0, stroke=1)
    return para(x+13, top+1, content, width-13, 9.3, 12)-6

def heading(x, top, label):
    text(x, top-11, label, 11, True, TEAL)
    return top-24

text(36, 727, 'EDD VERIFICATION CHECKLIST', 21, True)
text(36, 708, 'Sonographers + providers  |  New-visit dating review', 11, False, GRAY)
para(36, 696, '<b>Verify the source before making gestational-age-based recommendations.</b> '
     'Use with the OpenMFM dating presentation and local reporting policy.', size=9.5)
text(36, 655, 'Patient / chart ID: ________________________   Encounter date: __________________', 9.5)

y=heading(36, 637, '01  ASK: evaluate the menstrual history')
y=check(36,y,'First day of last normal menstrual period (LMP), certainty, usual cycle length and regularity.')
y=check(36,y,'Typical bleeding? Recent contraception, lactation / amenorrhea or fertility treatment?')
y=heading(36,y-3,'02  RETRIEVE: find the earliest evidence')
y=check(36,y,'Ask about prior OB, emergency-department and fertility scans. Obtain the original report.')
y=check(36,y,'Verify scan date, CRL / biometry, ultrasound age, adequacy and original EDD; check ART records.')

z=heading(318,637,'03  RECONCILE: review the dating basis')
z=check(318,z,'Compare LMP, assigned dating and earliest adequate scan; calculate the discrepancy in days.')
z=check(318,z,'Use the exact ACOG age window and LMP reliability. Preserve reliable early dating; verify ART dating.')
z=heading(318,z-3,'04  DOCUMENT: make the decision traceable')
z=check(318,z,'Complete the template below, including why the EDD was retained or changed and any uncertainty.')

y=min(y,z)-3
y=heading(36,y,'05  COMMUNICATE: close the loop')
y=check(36,y,'Sonographer flags discrepancies; responsible provider confirms the EDD and rationale. Align the report and chart; explain the final date to the patient and referring team.',540)

# Safety-critical reminders remain adjacent to the workflow, rather than buried in references.
box_top=y-1
c.setFillColor(HexColor('#eef4f5'))
c.roundRect(36,box_top-47,540,47,5,fill=1,stroke=0)
para(46,box_top-7,'<b>Escalate:</b> missing / conflicting records, inadequate images, ART discordance or concerning size. '
     'Do not redate simply to normalize growth. No confirming or revising ultrasound before <b>22w0d</b> '
     'means suboptimal dating; document the best estimate and a provider-directed plan.',520,9.2,11.5)

top=box_top-62
text(36,top,'DATING DOCUMENTATION TEMPLATE',11,True,TEAL)
text(36,top-15,'Complete in the chart or use these lines as a structured handoff.',9,False,GRAY)
lines=[
 'LMP / certainty: ______________________________________________________________',
 'Cycles (usual length, range, regularity): ___________________________________________',
 'Relevant history / ART (transfer date, embryo age): _________________________________',
 'Earliest report (source, scan date): _______________________________________________',
 'CRL / biometry, ultrasound age and image adequacy: _________________________________',
 'LMP / assigned age at scan; discrepancy in days: ___________________________________',
 'Final EDD; basis and reason retained / changed: ____________________________________',
 '____________________________________________________________________________',
 'Provider review; patient / referring-team communication: ______________________________',
 'Missing evidence; follow-up owner and plan: ________________________________________',
]
for i,line in enumerate(lines):text(36,top-37-i*19,line,9.2)
bottom=top-37-9*19
assert bottom>93, f'Template would overlap footer: {bottom}'
c.setStrokeColor(LINE);c.line(36,85,576,85)
para(36,77,'<b>Sources:</b> ACOG CO 700 (2017), <link href="https://doi.org/10.1097/AOG.0000000000002046" color="#006778">doi:10.1097/AOG.0000000000002046</link>; '
     'CO 688 (2017), <link href="https://doi.org/10.1097/AOG.0000000000001949" color="#006778">doi:10.1097/AOG.0000000000001949</link>.<br/>'
     'AIUM standard obstetric ultrasound (2024), <link href="https://doi.org/10.1002/jum.16406" color="#006778">doi:10.1002/jum.16406</link>. '
     'Proposed workflow; supports clinical judgment.',540,7.6,10)
text(36,42,'OpenMFM.org  |  Atlanta Perinatal Associates',8,True,TEAL)
text(389,42,'Updated October 21, 2026  |  1 / 1',8,False,GRAY)
c.linkURL('https://openmfm.org/decks/gestational-dating/index.html',(36,38,290,52),relative=0)
c.showPage();c.save()
print(PDF)
