# Pregnancy with a Higher BMI — production review

Completed November 4, 2026 after user approval of the 23-slide outline.

## Deliverables

- `index.html`: standalone 23-slide patient presentation; no external runtime, fonts, analytics, or build step required.
- PDF: `presentation.pdf` beside the HTML deck; 23 landscape pages, selectable text and linked references.
- Local catalog entries added to the main index, presentations JSON, and both sitemaps. Existing unrelated changes retained. Publishing authorized by the user; release prepared from current origin/main in an isolated checkout.

## Content and evidence review

- Uses person-first language and separates BMI ≥30 from class III obesity (BMI ≥40).
- Preserves conditional antenatal-testing guidance: consider weekly checks at 34 weeks for BMI ≥40 and at 37 weeks for BMI 35–39.9; does not promise prevention of all adverse outcomes.
- Distinguishes early risk-based screening for preexisting diabetes from routine gestational diabetes screening at 24–28 weeks.
- Uses risk-based aspirin counseling without prescribing a patient-specific regimen.
- Discusses induction from 39 weeks as an individualized option; does not mandate early delivery or cesarean based on BMI alone.
- Uses ACOG's 2025 cervical-ripening guideline. Combination treatment is an option, not a proven class III obesity winner. Misoprostol safety after prior cesarean or major uterine surgery is explicit.
- Omits untraceable 2026 cohort statistics, the unverified 57% versus 39% comparison, drug escalation protocols, and the source packet's unsupported licensing statement.
- Includes postpartum clot prevention, warning signs, questions for an MFM specialist, educational limits, and privacy information.
- Thirteen numbered sources are linked from slides and the sources panel. Reference metadata for the obesity bulletin, 2024 diabetes update, 2025 ripening guideline, and 2024 induction trials were checked against publication/DOI/PubMed records. The 2025 ripening recommendations were available in the publisher's indexed text.
- Access limitation: the complete publisher pages for the 2021 obesity bulletin and 2024 diabetes update were not retrievable through the web tool. The supplied bulletin material was cross-checked against ACOG patient/surveillance resources. The diabetes update's recommendations were verified in the clinical recommendation excerpt reproduced by OPQIC, with primary publication metadata verified independently. No claim of complete full-text access is made.

## Browser and print validation

Chromium checks performed with Python Playwright:

- All 23 slides at 1440×900 and 1280×720: no horizontal overflow or required vertical scrolling.
- All 23 slides at 390×844 and 320×568: no horizontal overflow; long mobile slides scroll vertically within the presentation.
- Arrow navigation, Home/End, slide selector, first/last disabled controls, hash navigation, and multi-digit reference deep links passed.
- Sources dialog opens, closes with Escape, and restores focus to its trigger.
- Synthetic horizontal touch navigation passed; no physical-device gesture testing was performed.
- JavaScript-disabled view exposes all 23 slides.
- No browser JavaScript errors.
- Reduced-motion setting exercised. Semantic headings, labeled controls, native dialog, visible focus styling, and live slide announcements present. This is not a formal assistive-technology certification.
- Desktop contact sheet and selected full-size/mobile renders visually reviewed.
- PDF has exactly 23 nonempty pages. Every page contains only its matching slide footer; no footer spillover. References and closing page visually rechecked after print spacing correction.
- JSON catalog and both XML sitemaps parse successfully.

Temporary QA assets and scripts are under `tmp/obesity-qa/`, `tmp/qa_obesity_deck.py`, and `tmp/build_obesity_deck.py`. The final HTML does not depend on them.

## Release validation

- `npm test -- --runInBand`: 5 suites, 57 tests passed. Existing tracked nested-worktree package-name warnings were nonblocking.
- `npm run build` in `landing-page`: successful production build.
- New entry verified first in the shared presentation feed and first in the library list after the featured content.
- Sitemap generator and SEO injector completed; existing sitemap modification dates retained to avoid unrelated changes.
- PDF included beside the deck and linked in the catalog.
