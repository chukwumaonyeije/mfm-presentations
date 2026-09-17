# TOF education: evidence and release checks

Reviewed September 17, 2026. Audience-specific companion decks: 16 patient slides and 26 clinician/sonographer slides. The clinician deck includes a separate six-question quiz, linked from the deck and catalog.

## Clinical editing decisions

- The replaced deck described AVSD plus TOF physiology. The new patient guide addresses TOF broadly and preserves AVSD as a clearly conditional associated finding. It does not assert a shared valve, suspected trisomy, absent regurgitation, or non-ductal-dependent circulation in an unspecified patient.
- Removed the suggestion that pulmonary stenosis protects fetal lungs. The replacement explains placental oxygenation and the transition at birth.
- Diagnostic testing is offered through informed counseling, not mandated. CMA and cfDNA limitations are explicit.
- No universal diagnostic PA:aorta ratio or RVOT velocity cut-off is presented. Multiplanar anatomy and physiology determine the interpretation.
- Ductal-flow direction is described anatomically. Aorta-to-PA flow raises concern for postnatal ductal dependence; a usual fetal flow direction does not guarantee postnatal stability.
- Delivery location is tied to actual neonatal capabilities and anticipated physiology. Maternal facility level is not treated as proof of on-site pediatric cardiac surgery.
- Numerical outcome promises were removed. The 3–6 month repair interval is limited to asymptomatic infants in the AATS consensus context.
- The Vetten 2025 predictor is labeled observational: 253 infants with simple TOF, 28–32-week measurements, early intervention within 30 days, sensitivity 79% and specificity 70% for PV Z-score ≤−3.5 or abnormal ductal flow. It is not a delivery or treatment mandate.
- Original diagrams are labeled conceptual, not ultrasound images. Cases and quiz scenarios are hypothetical.
- References include exact publications, dates, DOI or source URLs. Quiz feedback links to both supporting sources and relevant presentation slides.

## Functional checks

- Eight TOF regression tests cover correct/mixed/zero scoring, prevention of repeated scoring and unanswered skipping, first-answer locking, six-item answer review, retake reset, focus, deep links, and navigation shortcuts.
- Full root test suite: 36 tests passed (`npm test -- --runInBand --roots __tests__`). Roots are scoped to this checkout to exclude unrelated nested worktree tests.
- Production landing-page build passed (`npm run build`). Existing multiple-lockfile warning remains; the first sandboxed attempt was denied access to the parent workspace directory, and the permitted build succeeded.
- Headless Chromium checked all 42 slides at 1440, 390, and 320 px; no document-level horizontal overflow or JavaScript page errors. All slides fit at the tested 1440 × 900 desktop viewport.
- Browser checks passed for deep links, back navigation, reference-dialog Escape behavior, full-score quiz completion, explanations, and retake.
- Print output verified at 16 patient pages and 26 clinician pages, without extra blank/orphan pages. Representative final/reference and diagram pages visually inspected.
- HTML has semantic headings, hidden inactive slides, visible interactive focus indicators, a skip link, reduced-motion rules, horizontal-swipe detection that ignores vertical scrolling and interactive content, and print styles. Mobile diagrams support horizontal panning for readable labels.
- No third-party scripts or remote fonts are needed. Quiz answers are held in memory, not submitted or persisted. Hosting and linked sources have separate privacy policies.

## Publication scope

Replace `decks/avsd-tof-physiology-patient/index.html` in place, add `decks/tetralogy-of-fallot-prenatal-diagnosis/index.html` and `quiz.html`, update both catalog surfaces and sitemaps. Stage only related files. Existing unrelated workspace files remain untouched.
