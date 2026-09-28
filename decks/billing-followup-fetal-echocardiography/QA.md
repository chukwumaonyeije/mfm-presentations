# Quality Assurance & Educational Audit
## Topic: Billing for Follow-up Fetal Echocardiography (CPT 76826, 76828, 93325)
**Standard:** OpenMFM Presentation Standard v1.0  
**Date:** September 28, 2026  
**Audience:** Billers, Sonographers, MFM Physicians, and APPs  

---

## 1. Deliverables Summary

- `OUTLINE.md`: Approved Stage 0 Educational Design, evidence corrections, and 25-slide lesson-led outline.
- `index.html`: Complete 25-slide interactive presentation with custom theme, original SVGs, responsive layout, modal references, print styling, keyboard/touch navigation, and OpenMFM library links.
- `quiz-data.json`: 10-question case-based assessment covering baseline rules, Doppler criteria, modifiers, and audit shields.
- `quiz.html`: Interactive single-page quiz with immediate feedback, detailed rationales, live score tracking, and question review.
- `QA.md`: Comprehensive quality assurance and clinical audit report.

---

## 2. Clinical & Coding Review

1. **Coding Integrity (76826 / 76828 / 93325):**  
   - Established that 76826 (2D follow-up) requires a documented prior complete fetal echocardiogram (76825) in the current pregnancy. If no baseline exists, the study is coded as Complete (76825/76827).
   - Clarified that CPT 76828 requires saved, measured spectral Doppler velocity waveforms (pulsed-wave / continuous-wave) across inflows, outflows, DV, or mechanical PR interval. If spectral Doppler is omitted, 76828 cannot be unbundled.
   - Emphasized that CPT 93325 is an add-on code that must accompany a base code and cannot be billed alone.

2. **Dual-Encounter Rules (Modifier 59 / XE):**  
   - Clearly documented the rules for same-day growth/fluid follow-up (76816) combined with fetal echo follow-up (76826/76828/93325), requiring distinct indications, discrete reports, and Modifier 59/XE appended to 76816.

3. **Technical & Sonographic Protocols:**  
   - Emphasized the mandatory archiving of real-time cine loops of the beating heart across segmental views (static still frames fail audits).
   - Illustrated mechanical PR interval acquisition (mitral A wave onset to aortic V wave onset; normal <150 ms) for anti-Ro/SSA maternal antibody surveillance.
   - Standardized end-systolic fluid-only millimeter caliper placement for pericardial effusions per ISUOG/ASE standards.

4. **Standalone Physician Reporting:**  
   - Provided compliant macro text and documented that embedding cardiac findings in an OB growth report legally restricts coders to 76816.

---

## 3. Technical & Browser Validation

- **Keyboard Navigation:** ArrowRight / Space / PageDown (Next), ArrowLeft / PageUp (Prev), Home (First slide), End (Last slide), F (Fullscreen toggle), Esc (Close modal).
- **Touch Navigation:** Horizontal touch swipes with directional threshold detection.
- **Hash Navigation:** Direct deep-linking via `#slide-1` through `#slide-25` with browser history integration.
- **Accessibility:** Semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<figure>`, `<dialog>`), ARIA labels, live announcer for screen readers, high contrast color palette, reduced-motion media query support.
- **Print / PDF Mode:** Dedicated `@media print` rules ensuring clean layout across pages with hidden UI controls.
- **Quiz Functionality:** 10 questions with single-choice selection, answer lock on click, instant explanation display, final score calculation, detailed review dropdowns, and retake functionality.
