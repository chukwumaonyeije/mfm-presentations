# RVUs and Medical Billing in the MFM Clinic

OpenMFM Presentation Standard v1.0 · 2026 service-year edition · November 23, 2026

## Open the teaching resources

- `index.html`: 28-slide interactive presentation. Open directly in a modern browser. Includes keyboard/touch navigation, slide links, reference dialog, worked calculator, case reveals and print layout.
- `quiz.html`: choose MFM Physician (12 questions), MFM APP (12 questions), or Both Tracks (16 questions).
- `quiz.html?track=physician` and `quiz.html?track=app`: direct entry to each track when served on a website.
- `answer-key.html`: complete printable facilitator key with all options, explanations, references and slide links.
- `presentation.pdf`: 28-page printable deck.
- `answer-key.pdf`: printable facilitator resource.

The HTML files embed their styles, scripts and quiz data. No server, build step, external script, account, analytics or network request is required for learning activities. External reference links require internet access. Quiz answers remain in browser memory and clear on reload. The calculator uses fictional RVUs and contract terms; it is not a claim-pricing tool.

Navigation: Left/Right arrows or Page Up/Page Down, Home/End, the slide selector, Back/Next buttons, or horizontal touch swipe. On small screens, scroll vertically to read a slide. Print/PDF includes all slides and expanded case answers. The references dialog closes with Escape.

## Educational scope

Focus: MFM consultations and co-management, diabetes follow-up, fetal imaging, office E/M, physician–APP service attribution, and the difference between work RVUs, payer reimbursement and compensation. NPs and PAs are the primary APP examples; the deck distinguishes CNM Medicare payment rules.

Medicare-specific policies are labeled. Medicaid and commercial contracts require separate verification. Service-year scope is 2026; this resource does not apply 2027 rates or future maternity coding changes to 2026 encounters. Cases are fictional. No CME credit, certification, or billing guarantee is offered.

## Source review decisions

1. Used the user-provided SMFM Career Center article as an introductory foundation, not a formal coding guideline.
2. Corrected its simplified single-conversion-factor framing for 2026: CMS has distinct qualifying/nonqualifying APM conversion factors. Employment-contract conversion rates remain separate.
3. Used current CMS E/M guidance, AMA E/M explanations and CMS/MAC incident-to resources. Distinguished Medicare same-specialty wording from the CPT specialty/subspecialty framework.
4. Included the 2026 audio/video direct-supervision provision for eligible incident-to services, its 010/090 global-surgery exclusions, and the continued need to satisfy all other requirements.
5. Used current CMS NCCI modifier guidance. No individual ultrasound/echo code-pair exception or automatic modifier-59 workaround is asserted.
6. Used the 2018 SMFM global-obstetric coding tip only as historical specialty context. Its broad modifier language is not applied as a universal current payer rule.
7. Avoided unverified CPT-specific RVU tables, universal APP percentages, compensation benchmarks, and E/M levels inferred from diagnosis labels alone.

Full linked citations are available on slide 28, in the reference dialog, and in the answer key. Review date: November 23, 2026. Annual or payer-policy changes should trigger content review.

## Maintenance

`build.py` and `style.css` are authoring sources. `python build.py` regenerates the three standalone HTML pages and `quiz-data.json`. PDFs must then be regenerated from the current HTML. `verify.py` performs browser acceptance checks and PDF generation using Python Playwright and PyMuPDF; configure its Chromium executable path for another computer. Browser output is stored in `qa/`.

The approved educational outline is retained in `OUTLINE.md`. This standalone resource is published through the OpenMFM repository pipeline. Rebuilding the teaching files does not itself deploy the site.
