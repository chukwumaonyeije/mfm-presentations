# AI-Assisted PACS for Maternal-Fetal Medicine

## Presentation brief

- **Audience:** MFM physicians, ultrasound medical directors, health-system purchasers, clinical informaticists, and imaging IT leaders
- **Single most important message:** Do not buy “AI PACS.” Buy a validated clinical workflow whose intended use, integration boundary, human oversight, and post-deployment performance are explicit.
- **Six-month takeaway:** A 510(k) clearance is product- and indication-specific. It does not prove local performance, interoperability, diagnostic superiority, or return on investment.
- **Common misconceptions to correct:**
  - PACS, reporting software, console AI, patient-sharing apps, and diagnostic image-analysis software are interchangeable.
  - “FDA-cleared” applies to every module marketed under a vendor brand.
  - High sensitivity and specificity automatically translate into safer care.
  - Device-agnostic software is plug-and-play.
  - AI can replace physician interpretation or a local quality program.
- **Key purchasing decisions:** workflow location, exact intended use, supported gestational ages/views, device compatibility, DICOM/HL7/FHIR integration, latency, cybersecurity, site validation, monitoring, contracting, and exit strategy.
- **Visual language:** cinematic dark clinical interface; cyan workflow paths; amber cautions; green verified claims; red category errors; diagrams instead of dense bullet lists.

## Proposed slide outline

### 1. AI does not fix a fragmented imaging workflow

- **Objective:** Establish the purchasing problem.
- **Key teaching point:** The clinical value comes from the complete acquisition-to-report pathway, not from an isolated model.
- **Visual concept:** A fetal ultrasound study travels through acquisition, QA, archive, interpretation, report, EHR, and audit; failure points glow red.
- **Anticipated references:** AIUM Practice Parameter for Documentation of an Ultrasound Examination; FDA AI-enabled device lifecycle materials.

### 2. Today’s decision is architectural, not cosmetic

- **Objective:** Define what learners should be able to decide after the talk.
- **Key teaching point:** Purchasers must classify the product, verify its claim, test it locally, and govern it after launch.
- **Visual concept:** Four-part compass: classify, verify, validate, monitor.
- **Anticipated references:** FDA device classification and lifecycle resources.

### 3. “AI-assisted PACS” hides five different products

- **Objective:** Build the prerequisite taxonomy.
- **Key teaching point:** Archive/viewer, ultrasound reporting, console AI, concurrent image QA, and report-generation AI solve different problems.
- **Visual concept:** Five stacked layers with example outputs and regulatory boundaries.
- **Anticipated references:** DICOM workflow concepts; vendor indications for use and product documentation.

### 4. The clinical workflow determines where AI can help

- **Objective:** Map AI functions to the MFM exam.
- **Key teaching point:** Acquisition guidance and image-quality feedback must act before the patient leaves; reporting and archive functions act later.
- **Visual concept:** Horizontal timeline from order to final report with “recoverability window” closing after acquisition.
- **Anticipated references:** AIUM documentation and obstetric practice parameters.

### 5. Image validation is not anomaly detection

- **Objective:** Separate four frequently conflated claims.
- **Key teaching point:** View recognition, quality-criteria verification, biometric automation, and anomaly detection require different evidence and produce different risks.
- **Visual concept:** Four diagnostic targets with distinct inputs, outputs, and failure modes.
- **Anticipated references:** FDA Sonio Detect indications for use; GE SonoLyst; Samsung Intelligent Assist documentation.

### 6. Five familiar names represent four product categories

- **Objective:** Reframe the supplied shortlist without a misleading rank order.
- **Key teaching point:** The candidates are complementary components, not direct substitutes.
- **Visual concept:** Evidence-coded comparison matrix adapted from the supplied `pacs_slides.html`, replacing unsupported yes/no labels with exact product category, workflow location, supported task, regulatory evidence, hardware boundary, and confidence level:
  - Philips Ultrasound Workspace: review, quantification, reporting, and PACS integration
  - GE ViewPoint 6 + SonoLyst: reporting layer plus Voluson console AI
  - Samsung Intelligent Assist + HelloMom: console AI plus non-diagnostic patient app
  - Microsoft PowerScribe One: radiology reporting and AI orchestration
  - Sonio Detect: concurrent fetal image QA and workflow software
- **Anticipated references:** Official vendor product pages, IFUs, and FDA summaries.

### 7. Philips: broad workspace, limited evidence for real-time fetal QA

- **Objective:** Evaluate Philips against the intended use case.
- **Key teaching point:** Ultrasound Workspace is cleared for fetal quantification/reporting and third-party integration, but its documented AI features are not equivalent to real-time OB view validation.
- **Visual concept:** Strengths on the integration side; evidence gap on the acquisition-QA side.
- **Anticipated references:** Philips Ultrasound Workspace 6.0/7.0 IFU; FDA K241659.

### 8. GE: the strongest integrated Voluson pathway

- **Objective:** Evaluate the GE stack.
- **Key teaching point:** ViewPoint manages women’s-health reporting; SonoLyst supplies real-time anatomy recognition and image-quality support on compatible Voluson systems.
- **Visual concept:** Two connected boxes, “console intelligence” and “department workflow,” with the vendor-lock boundary visible.
- **Anticipated references:** GE HealthCare ViewPoint 6 and SonoLyst official pages.

### 9. Samsung: separate clinical AI from patient engagement

- **Objective:** Correct the HelloMom classification error.
- **Key teaching point:** Samsung BiometryAssist, ViewAssist, and HeartAssist are clinical console functions; HelloMom transfers keepsake images and explicitly is not for medical use.
- **Visual concept:** Split screen: clinician console vs patient phone, divided by a regulatory firewall.
- **Anticipated references:** Samsung Medison Intelligent Assist materials; HelloMom app labeling; relevant FDA summaries for specific console functions.

### 10. PowerScribe One: powerful reporting, not fetal image QA

- **Objective:** Place reporting AI correctly.
- **Key teaching point:** PowerScribe One can improve structured reporting, quality checks, and AI-service orchestration, but it does not itself validate fetal ultrasound planes or exam completeness.
- **Visual concept:** Report pipeline with PACS/RIS context synchronization and third-party AI input.
- **Anticipated references:** Microsoft PowerScribe One product page and PowerCast integration guide.

### 11. Sonio Detect: the closest match to the stated use case

- **Objective:** Evaluate the device-agnostic fetal QA option.
- **Key teaching point:** FDA-cleared Sonio Detect analyzes fetal images and clips concurrently for views, anatomy, and quality criteria; coverage remains bounded by version and supported protocols.
- **Visual concept:** Live checklist filling as DICOM images arrive, with unsupported criteria left visibly manual.
- **Anticipated references:** FDA K230365, K240406, and K252433; Sonio regulatory and product pages.

### 12. Clearance answers one question, not every question

- **Objective:** Teach precise regulatory interpretation.
- **Key teaching point:** Verify the exact trade name, version, intended use, users, gestational ages, outputs, contraindications, and human-review requirements.
- **Visual concept:** A 510(k) decision letter magnified into eight procurement fields.
- **Anticipated references:** FDA 510(k) database and AI-enabled medical device resources.

### 13. Vendor accuracy is not your site’s accuracy

- **Objective:** Translate published performance into local validation.
- **Key teaching point:** Test across ultrasound vendors, BMI, gestational age, multiple gestations, anomalies, sonographers, and network conditions before clinical reliance.
- **Visual concept:** Validation cohort grid feeding a go/no-go gate.
- **Anticipated references:** FDA Sonio Detect v3 performance summary; FDA performance-evaluation materials.

### 14. Integration failure can erase model performance

- **Objective:** Make workflow integration concrete.
- **Key teaching point:** Require DICOM conformance, accession matching, worklist behavior, measurement transfer, report reconciliation, latency targets, downtime mode, and audit logs.
- **Visual concept:** DICOM/HL7/FHIR sequence diagram with failure injection points.
- **Anticipated references:** Vendor integration guides; DICOM/FHIRcast documentation; AIUM documentation standard.

### 15. The RFP should purchase evidence and control

- **Objective:** Give purchasers a practical scoring tool.
- **Key teaching point:** Start with the practice profile, then score clinical fit, evidence, interoperability, safety, security, operations, economics, and vendor accountability before price.
- **Visual concept:** The useful practice-profile idea from the supplied HTML becomes a conditional shortlist rather than a brand recommendation: single-vendor console fleet, mixed-vendor enterprise, acquisition-QA priority, reporting priority, or patient-sharing priority. Each route ends in a weighted scorecard with mandatory pass/fail gates.
- **Anticipated references:** FDA lifecycle principles; NIST AI Risk Management Framework as governance context.

### 16. Pilot the workflow before you sign the enterprise contract

- **Objective:** Present a concise implementation algorithm.
- **Key teaching point:** Define the use case, establish baseline metrics, run silent mode, validate prospectively, train users, launch narrowly, and monitor drift.
- **Visual concept:** Seven-step clinical procurement algorithm with stop gates.
- **Anticipated references:** FDA postmarket-performance discussions; institutional AI governance literature.

### 17. Measure patient care, not clicks

- **Objective:** Define a balanced evaluation dashboard.
- **Key teaching point:** Monitor incomplete exams, recalls, acquisition time, report turnaround, overrides, false reassurance, disparities, downtime, and downstream outcomes.
- **Visual concept:** Executive dashboard balancing quality, safety, equity, efficiency, and cost.
- **Anticipated references:** FDA lifecycle resources; peer-reviewed implementation and monitoring literature.

### 18. Clinical pearls: buy the boundary, not the brand

- **Objective:** Consolidate five to ten memorable rules.
- **Key teaching point:** Category clarity, indication specificity, human oversight, local validation, interoperability, monitoring, and exit rights determine safety and value.
- **Visual concept:** Eight compact rules arranged around the physician as accountable system owner.
- **Anticipated references:** Synthesis of preceding sources.

### 19. Evidence and controversies

- **Objective:** Separate knowns from unresolved questions.
- **Key teaching point:** Real-time QA can standardize acquisition, but evidence remains limited on anomaly detection, outcome improvement, generalizability, automation bias, and long-term economics.
- **Visual concept:** Three columns: known, uncertain, disputed; a fourth row for research priorities.
- **Anticipated references:** FDA summaries; peer-reviewed validation studies; professional-society guidance.

### 20. References and purchaser worksheet

- **Objective:** Make the deck auditable and actionable.
- **Key teaching point:** Every product claim links to its primary source; the final view offers a downloadable/copyable RFP checklist.
- **Visual concept:** Filterable reference panel plus one-page procurement checklist.
- **Anticipated references:** Complete linked citations used throughout the presentation.

## Primary sources already verified for the HTML phase

1. Philips. *Ultrasound Workspace 7.0 Instructions for Use.* 2025. https://www.documents.philips.com/assets/Instruction%20for%20Use/20250711/2b423faa66f84ab4926eb3170078473d.pdf
2. U.S. Food and Drug Administration. *Ultrasound Workspace (UWS 6.0), K241659.* 2025. https://www.accessdata.fda.gov/cdrh_docs/pdf24/K241659.pdf
3. GE HealthCare. *ViewPoint 6 Ultrasound Reporting Software for Women’s Health.* https://www.gehealthcare.com/en-us/products/ultrasound/ultrasound-reporting/viewpoint-womens-health
4. GE HealthCare. *SonoLyst.* https://www.gehealthcare.com/en-us/products/ultrasound/voluson/sonolyst
5. Samsung Medison. *Samsung Showcases AI-Based Automatic Measurement and Diagnostic Solutions at ISUOG World Congress 2023.* https://news.samsung.com/global/samsung-showcases-ai-based-automatic-measurement-and-diagnostic-solutions-at-isuog-world-congress-2023
6. Samsung Medison. *Hello Mom app labeling.* https://play.google.com/store/apps/details?id=com.samsungmedison.sonic&hl=en
7. Microsoft. *PowerScribe One.* https://www.microsoft.com/en-us/health-solutions/radiology-workflow/powerscribe-one
8. Microsoft/Nuance. *PowerCast Integration Guide.* https://connect2.nuancepowerscribe.com/psonesetup/PO-PowerCastIntegrationGuide.pdf
9. U.S. Food and Drug Administration. *Sonio Detect, K230365.* 2023. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm?ID=K230365
10. U.S. Food and Drug Administration. *Sonio Detect v3, K252433.* 2026. https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252433.pdf
11. AIUM. *Practice Parameter for Documentation of an Ultrasound Examination.* https://www.aium.org/docs/default-source/resources/guidelines/aium-practice-parameter-for-documentation-of-an-ultrasound-examination.pdf
12. U.S. Food and Drug Administration. *Performance Evaluation Methods for Evolving AI-Enabled Medical Devices.* https://www.fda.gov/medical-devices/medical-device-regulatory-science-research-programs-conducted-osel/performance-evaluation-methods-evolving-artificial-intelligence-ai-enabled-medical-devices

## Audit of the supplied `pacs_slides.html`

### Material retained

- A five-candidate comparison view, redesigned around product category and evidence rather than a rank order.
- Strength/limitation framing for each candidate.
- Practice-profile segmentation for purchasers.
- Dedicated views for regulatory status, integration, and acquisition-quality functions.
- Dark, high-contrast clinical visual direction.

### Claims corrected or excluded

- **Philips:** Exclude unsupported claims that Ultrasound Workspace provides real-time fetal auto-labeling, anomaly detection, or Philips-only compatibility. The verified IFU describes review, quantification, reporting, third-party platform integration, and fetal indications; its named AI features are predominantly cardiac.
- **GE:** Separate ViewPoint 6 reporting from SonoLyst console AI. Do not label the combined stack “Edison AI” without a product-specific source. Exclude unsupported claims about old-system latency, mandatory high-end local hardware, and anomaly-detection superiority.
- **Samsung:** Do not describe HelloMom as a clinical AI platform. Its labeling states that it is not intended for medical or diagnostic use. Clinical functions such as BiometryAssist, ViewAssist, and HeartAssist will be discussed separately and only within their documented labeling.
- **PowerScribe One:** Retain reporting, quality-check, and interoperability strengths. Exclude claims that it performs fetal image validation or fetal anomaly detection, and avoid blanket “FDA-cleared” labeling without a product-function-specific regulatory source.
- **Sonio:** Replace “CE-cleared with partial FDA clearance” and “U.S. clearance in progress.” Sonio Detect has multiple FDA 510(k) clearances, including v3 (K252433, 2026), for concurrent fetal view, anatomy, and quality-criteria analysis. Do not equate Sonio Detect quality assurance with Sonio Suspect anomaly detection unless each function’s distinct clearance and intended use are shown.
- **All vendors:** Exclude unsourced superlatives such as “top anomaly detection,” “best integration,” “strong,” “moderate,” and “very high.” The production matrix will use verifiable capabilities, labeled evidence gaps, and local-validation requirements.

## HTML production acceptance criteria

- One self-contained `index.html`; no build step.
- Twenty slides; each clinical content slide at or below 30 words, excluding citations and accessible labels.
- Keyboard, click, touch/swipe, URL hash, progress, slide counter, overview, fullscreen, print/PDF, and references panel.
- Semantic landmarks, visible focus, screen-reader labels, contrast compliance, reduced-motion mode, and mobile reflow.
- Inline SVG/CSS diagrams; no decorative stock-photo dependency.
- Every vendor and regulatory claim linked to a primary source.
- Representative slides visually inspected at desktop and mobile sizes.
- Automated checks for slide count, word count, navigation, broken internal anchors, and missing citations.
