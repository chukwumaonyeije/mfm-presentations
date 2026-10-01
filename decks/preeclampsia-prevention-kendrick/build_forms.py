"""Generate blank paper chart and audit tools. Run with reportlab installed."""
from pathlib import Path
from html import escape
import textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black

ROOT = Path(__file__).parent
OUT = ROOT / 'resources'
OUT.mkdir(exist_ok=True)
W, H = 612, 792
INK = HexColor('#183349')
PALE = HexColor('#eaf1f5')

class Form:
    def __init__(self, name, title, pages):
        self.name, self.title, self.pages = name, title, pages
        self.c = canvas.Canvas(str(OUT / (name + '.pdf')), pagesize=(W,H))
        self.c.setTitle(title)
        self.c.setAuthor('OpenMFM; adapted from Nadia Kendrick project materials')
        self.parts=[]; self.page=0; self.y=0

    def line(self, s, size=10.5, bold=False, gap=13):
        self.c.setFillColor(black)
        self.c.setFont('Helvetica-Bold' if bold else 'Helvetica',size)
        self.c.drawString(36,self.y,s)
        self.y-=gap
        self.parts.append('<p'+(' class="bold"' if bold else '')+'>'+escape(s)+'</p>')

    def para(self,s,size=10,gap=13):
        lines=textwrap.wrap(s, width=int(103*10/size))
        for x in lines:
            self.c.setFont('Helvetica',size); self.c.setFillColor(black)
            self.c.drawString(36,self.y,x); self.y-=gap
        self.parts.append('<p>'+escape(s)+'</p>')

    def section(self,s):
        self.y-=6
        self.c.setFillColor(PALE); self.c.rect(36,self.y-7,540,22,fill=1,stroke=0)
        self.c.setFillColor(INK); self.c.setFont('Helvetica-Bold',11)
        self.c.drawString(43,self.y,s); self.y-=23
        self.parts.append('<h2>'+escape(s)+'</h2>')

    def checks(self,labels,size=10,gap=17):
        x=36
        self.c.setFont('Helvetica',size); self.c.setFillColor(black)
        for label in labels:
            self.c.rect(x,self.y-1,8,8,stroke=1,fill=0)
            self.c.drawString(x+12,self.y,label)
            x+=self.c.stringWidth(label,'Helvetica',size)+27
            if x>577: raise ValueError('Checkbox line overflow: '+str(labels))
        self.y-=gap
        self.parts.append('<p class="choices">'+' '.join('<span>□ '+escape(t)+'</span>' for t in labels)+'</p>')

    def table(self, labels, headers=('Yes','No','Not sure'), font=10, row=21, colx=(410,452,499)):
        self.c.setFont('Helvetica-Bold',9)
        self.c.drawString(36,self.y,'Check ONE answer per row; blank = not completed.')
        for x,h in zip(colx,headers): self.c.drawString(x-3,self.y,h)
        self.y-=15
        self.parts.append('<table><thead><tr><th>Check one answer per row</th>'+''.join('<th>'+escape(h)+'</th>' for h in headers)+'</tr></thead><tbody>')
        for label in labels:
            self.c.setStrokeColor(HexColor('#c3cdd3')); self.c.line(36,self.y-6,576,self.y-6)
            self.c.setFillColor(black); self.c.setFont('Helvetica',font)
            self.c.drawString(36,self.y,label)
            self.c.setStrokeColor(black)
            for x in colx: self.c.rect(x,self.y-1,8,8,fill=0,stroke=1)
            self.parts.append('<tr><td>'+escape(label)+'</td>'+''.join('<td>□</td>' for _ in headers)+'</tr>')
            self.y-=row
        self.parts.append('</tbody></table>')

    def newpage(self,subtitle,chart=True):
        if self.page:
            self.finish_page(); self.c.showPage(); self.parts.append('</article>')
        self.page+=1; self.y=752
        self.parts.append('<article class="page"><header><span>OPENMFM / ATLANTA PERINATAL ASSOCIATES</span><h1>'+escape(self.title)+'</h1><p>'+escape(subtitle)+'</p></header>')
        self.c.setFillColor(INK); self.c.setFont('Helvetica-Bold',10)
        self.c.drawString(36,self.y,'OPENMFM / ATLANTA PERINATAL ASSOCIATES'); self.y-=23
        self.c.setFont('Helvetica-Bold',17); self.c.drawString(36,self.y,self.title); self.y-=21
        self.c.setFont('Helvetica-Bold',11); self.c.drawString(36,self.y,subtitle); self.y-=22
        if chart:
            self.line('Patient name: __________________________  DOB: __________  MRN: ______________',10)
            self.line('Visit date: __________  Visit type: __________  GA: _____ weeks _____ days',10)
            self.line('Place patient label here if preferred. Repeat identifiers on every page.',9,gap=17)

    def finish_page(self):
        if self.y<48: raise ValueError(f'{self.name} page {self.page} content too low: {self.y}')
        self.c.setStrokeColor(HexColor('#b4c2cb')); self.c.line(36,37,576,37)
        self.c.setFont('Helvetica',8); self.c.setFillColor(INK)
        self.c.drawString(36,24,'v1.0 | September 30, 2026 | '+('Clinical chart copy; not a research consent form' if self.name=='chart-checklist' else 'De-identified research working sheet; not a clinical chart form'))
        self.c.drawRightString(576,24,f'Page {self.page} of {self.pages}')
        self.parts.append('<footer>v1.0 · September 30, 2026 · '+('Clinical chart copy; not research consent' if self.name=='chart-checklist' else 'De-identified working sheet')+f' · Page {self.page} of {self.pages}</footer>')

    def save(self):
        self.finish_page(); self.c.save(); self.parts.append('</article>')
        css='''body{font:11pt Arial,sans-serif;color:#142c3d;background:#e6edf2;margin:0}.tools{max-width:7.5in;margin:20px auto;padding:15px;background:white}.page{box-sizing:border-box;width:8.5in;min-height:11in;background:white;padding:.5in;margin:20px auto;position:relative;page-break-after:always}.page:last-child{page-break-after:auto}header span{font-size:9pt;letter-spacing:1px}h1{font-size:19pt;margin:12px 0 8px}header p{font-weight:bold}h2{font-size:12pt;padding:7px;background:#eaf1f5;margin:12px 0 9px}p{font-size:10pt;margin:7px 0;line-height:1.3}.bold{font-weight:bold}.choices{display:flex;flex-wrap:wrap;gap:12px}.choices span{white-space:nowrap}table{border-collapse:collapse;width:100%;font-size:10pt;margin:10px 0}td,th{padding:5px 3px;border-bottom:1px solid #d4dde3;text-align:center}td:first-child,th:first-child{text-align:left;width:70%}footer{font-size:8pt;border-top:1px solid #b4c2cb;margin-top:16px;padding-top:8px}button,a{font:inherit;color:#123b57}button{padding:8px 15px;margin-right:15px}@media(max-width:850px){.page{width:auto;margin:12px;padding:20px;min-height:0}.tools{margin:12px}td:first-child{width:60%}}@media print{@page{size:letter;margin:0}body{background:white}.tools{display:none}.page{margin:0;width:8.5in;min-height:11in;padding:.5in}a{color:inherit}h2,table{break-inside:avoid}}'''
        css+='@media print{.page{font-size:10pt}header span{font-size:8pt}h1{font-size:17pt;margin:7px 0 5px}h2{font-size:10.5pt;margin:8px 0 5px;padding:5px}p{font-size:9.5pt;line-height:1.2;margin:4px 0}table{font-size:9.5pt;margin:5px 0}td,th{padding:3px}.choices{gap:8px}footer{margin-top:10px;padding-top:5px}}'
        html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>'+escape(self.title)+'</title><style>'+css+'</style></head><body><nav class="tools" aria-label="Print tools"><button onclick="window.print()">Print blank form</button><a href="'+self.name+'.pdf">Download print-ready PDF</a><p>Blank paper form only. Write patient information on the printed chart copy. This webpage does not collect, save, or transmit answers.</p></nav>'+''.join(self.parts)+'</body></html>'
        (OUT/(self.name+'.html')).write_text(html,encoding='utf-8')

f=Form('chart-checklist','Preeclampsia Prevention Chart Checklist',3)
f.newpage('1 / Patient history and front-office routing')
f.section('A. FRONT OFFICE - distribute and route; do not make clinical decisions')
f.checks(['Patient label / identifiers checked','Blank form given','Interpreter requested'])
f.line('Language / assistance: ____________________  Staff initials: ______  Time: ______',10)
f.para('If urgent symptoms are reported, alert the clinical team immediately using the office emergency process. Do not wait for form completion or independently reassure the patient.')
f.checks(['No concern reported','Concern routed to clinical team','Unable to complete'])
f.line('Clinical staff notified: __________________________  Date / time: ______________',10)
f.section('B. PATIENT - tell staff immediately if you have concerning symptoms')
f.para('Severe headache that will not go away, vision changes, severe belly pain, chest pain, or trouble breathing need medical care right away. This list is not complete. If outside the office, call your care team; if unreachable, go to the emergency department. Call 911 for a life-threatening emergency.',9.5,12)
f.section('C. PATIENT - mark Yes, No, or Not sure; clinician will confirm')
f.table([
 'Preeclampsia in a previous pregnancy?',
 'High blood pressure before this pregnancy?',
 'Type 1 or type 2 diabetes before this pregnancy?',
 'Kidney disease?',
 'Lupus or antiphospholipid syndrome?',
 'Pregnant with twins or more babies?',
 'Is this your first pregnancy?',
 'Mother or sister had preeclampsia?',
 'This pregnancy conceived using IVF?',
 'Over 10 years since your last pregnancy?',
 'Prior pregnancy problem (for example, a very small baby)?',
 'You were born at a low birth weight / small for gestational age?',
 'Past aspirin / anti-inflammatory medicine reaction?',
 'Stomach ulcers, bleeding problems, or serious liver disease?'
],font=10,row=18)
f.line('Are you taking aspirin now?  Yes / No / Not sure   Dose: ______  Since: __________',10)
f.line('Other medicines / concerns: __________________________________________________',10)
f.line('Patient / assisting person initials (optional): ______  Clinician review pending.',9)

f.newpage('2 / Doctor or APP - risk confirmation and safety review')
f.section('D. CONFIRM RISK - patient answers alone do not establish eligibility')
f.table(['History of preeclampsia (especially with adverse outcome)',
 'Multifetal gestation','Chronic hypertension','Pregestational type 1 or type 2 diabetes',
 'Kidney disease','Autoimmune disease (SLE / antiphospholipid syndrome)'],headers=('Present','Absent','Unknown'),row=16,colx=(410,452,505))
f.line('High-risk factors confirmed: _____  Any unknowns / plan: ________________________',10)
f.table(['Nulliparity','Prepregnancy BMI >30 (BMI: ______)','Age at delivery >=35 years (age: ______)',
 'Family history: mother or sister with preeclampsia','In vitro fertilization',
 'Personal history category*','Self-identified Black race (proxy for racism, not biology)',
 'Lower income (clinical discussion; do not infer from insurance alone)'],headers=('Present','Absent','Unknown'),font=9.3,row=16,colx=(410,452,505))
f.para('*Personal history: low birth weight / SGA, previous adverse pregnancy outcome, or >10-year pregnancy interval. Count this category once, even if multiple examples apply.',9,11)
f.line('Distinct moderate-risk factors: _____  Supporting history: ______________________',9.8)
f.section('E. CLINICIAN INTERPRETATION - select one and explain exceptions')
f.checks(['>=1 high-risk factor','>=2 moderate-risk factors'],9.8)
f.checks(['Black identity or lower income alone: consider aspirin','Other / individualized'],9.3)
f.checks(['No indication identified','Assessment incomplete: clarification needed'],9.8)
f.para('ACOG/SMFM permits consideration with Black race (a proxy for underlying racism) or lower income alone. Social and structural inequities drive this risk; race is not a biological cause.',9,11)
f.section('F. SAFETY REVIEW - complete before recommending aspirin')
f.checks(['Medication / allergy list reviewed','Contraindications assessed'],10)
f.checks(['Aspirin / salicylate / NSAID hypersensitivity','Nasal polyps / aspirin bronchospasm'],9)
f.checks(['GI bleeding / active ulcer / other bleeding','Severe liver dysfunction'],9.5)
f.checks(['No concern identified','Concern present','Uncertain: resolve before prescribing'],9.5)
f.line('Details / interaction review / individualized risk: ______________________________',9.8)
f.line('Reviewed by (doctor / APP): __________________  Initials: _____  Date: __________',10)
f.para('Guidance: ACOG/SMFM aspirin advisory (2021); ACOG Committee Opinion 743 (2018). Review gestational timing and sign the final clinical plan on page 3.',8.5,10)

f.newpage('3 / Doctor or APP plan, follow-up, and chart filing')
f.section('G. COUNSELING - mark completed, N/A with reason, or not completed')
f.table(['Personal risk and reason for recommendation discussed',
 'Benefits and limits: risk reduced, not eliminated',
 'Safety, side effects, medication questions reviewed',
 'Dose, start date, duration and missed-dose instructions reviewed',
 'Access, cost, adherence barriers and preferences discussed',
 'Warning signs and contact / follow-up plan reviewed'],headers=('Done','N/A','Not done'),font=9.8,row=20,colx=(410,452,505))
f.checks(['Teach-back completed','Education handout provided','Interpreter used'],9.5)
f.line('N/A reasons / unresolved questions: ___________________________________________',10)
f.section('H. ASPIRIN DECISION - clinician selects ONE primary status')
f.checks(['Initiated today','Continued','Not indicated','Patient declined'],10)
f.checks(['Contraindicated','Held temporarily','Pending clarification','Planned start'],9.5)
f.line('Indication / reason for decision or exception: __________________________________',10)
f.line('____________________________________________________________________________',10)
f.line('Dose: ______ mg by mouth daily   Actual start date (if known): __________________',10)
f.line('GA at actual start: ____ weeks ____ days / unknown   Planned start date: __________',9.8)
f.line('Planned start GA: ____ weeks ____ days   Duration / stop plan: ___________________',9.8)
f.para('US guidance: 81 mg daily; initiate at 12-28 weeks, ideally before 16 weeks; continue until delivery unless individualized. Before 12 weeks, document a future plan. After 28 weeks or for a different dose, document clinical reasoning. This form is not a standing medication order.',9,11)
f.checks(['Order / medication list updated when indicated','Instructions given to patient'],9.5)
f.section('I. FOLLOW-UP AND SIGN-OFF - doctor / APP or clinical care team')
f.line('Next review / visit: __________  BP plan: ______________________________________',10)
f.line('Office / after-hours contact given: ____________________________________________',10)
f.line('At follow-up: taking as directed? Yes / No / Unknown / N/A   Barrier: _______________',9.5)
f.line('Follow-up action / responsible clinician: _______________________________________',10)
f.line('Doctor / APP name & role: ________________________  Signature: _________________',10)
f.line('Decision date / time: __________  GA at decision: ____ weeks ____ days',10)
f.section('J. FRONT OFFICE / RECORDS - file after clinician completion')
f.checks(['All 3 pages identified','Signed clinical plan present','Filed in correct chart'],9.5)
f.line('Filed by initials: ______  Date: ______  Clinical team notified if incomplete: ______',9.5)
f.para('Keep completed pages in the clinical chart. Do not send names, DOBs, MRNs, or signatures to the researcher. Use only the approved de-identified extraction process. Paper adaptation is not research consent or proof of enrollment.',9,11)
f.save()

a=Form('audit-worksheet','Preeclampsia Prevention Audit Worksheet',1)
a.newpage('Approved extractor only / one encounter per sheet / no chart identifiers',chart=False)
a.para('Proposed paper-workflow data collection companion. Confirm eligibility, denominators, repeat-visit handling, and coding with the investigator before use. Do not include names, dates of birth, MRNs, exact encounter dates, signatures, or identifying free text.',10,13)
a.section('A. STUDY LINKAGE - managed within the approved extraction process')
a.line('Approved study ID: _______________  Encounter sequence: _____  Study week: _____',10)
a.line('Extraction completeness: Complete / Incomplete / Unable to assess',10)
a.section('B. ORIGINAL PROJECT DOMAINS - keep missing separate from No')
a.table(['Risk screening completed and documented',
 'Counseling documented when indicated',
 'Aspirin decision documented'],headers=('Yes','No','Missing'),row=24,colx=(410,452,505))
a.line('Counseling not applicable with documented reason? Yes / No / Unknown',10)
a.line('GA at screening: _____ weeks _____ days / Missing',10)
a.line('GA at decision: _____ weeks _____ days / Missing',10)
a.section('C. DECISION CODE - transcribe the clinician record; do not infer')
a.checks(['Initiated','Continued','Not indicated','Declined'],10)
a.checks(['Contraindicated','Held','Pending','Planned start','Missing'],10)
a.para('Exception codes supplement the four original project categories. Do not silently classify contraindicated, held, pending, or planned-start encounters as not indicated. Investigator must predefine research mapping.',9.5,12)
a.line('Dose documented: _____ mg / Missing / N/A',10)
a.line('GA at actual initiation: _____ weeks _____ days / Unknown / N/A',10)
a.section('D. QUALITY CHECK - proposed supplemental fields')
a.checks(['Clinician signature present','Paper form filed','Incomplete record flagged'],10)
a.line('Clinical eligibility category: High risk / Multiple moderate / Consideration / None / Unknown',9.5)
a.line('Contraindication review documented: Yes / No / Missing',10)
a.line('Reason for justified exception documented: Yes / No / Missing / N/A',10)
a.para('Report process measures separately. A prescription does not establish actual medication use. This worksheet does not measure preeclampsia outcomes or prove causality.',10,13)
a.section('E. PRIVACY AND COUNTING RULES')
a.para('Use an approved study ID. Any linkage key stays under the approved practice data process, separate from the research extract. Suppress identifying details and small-cell disclosures as required. Do not upload completed worksheets to the public website.',10,13)
a.para('Suggested encounter-level reporting: completed assessments / eligible encounters; documented counseling / encounters requiring counseling; documented decisions / reviewed encounters. Patient-level reporting requires a prespecified repeat-visit rule. All definitions require investigator agreement.',9.5,12)
a.save()
print('Generated 3-page chart checklist and 1-page audit worksheet (PDF + printable HTML).')
