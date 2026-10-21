# Gestational dating replacement — QA

Updated October 21, 2026. Outline approved by the user before HTML production.

## Content

- 25-slide provider/sonographer deck and 10-case quiz, with explanations for all four options, source links, slide links, score, review and retake.
- Corrected original date arithmetic: 12w0d versus 10w3d is 11 days; 9w0d versus 9w1d is one day.
- ACOG Table 1 has six gestational-age rows (the outline incorrectly called for seven). All six windows and strict greater-than thresholds are included, with LMP reliability, earlier dating and third-trimester qualifications.
- Replaced unsupported LMP percentages, blanket redating statements and unverified national audit targets. Audit measures and documentation workflow are explicitly proposed local practices.
- Distinguishes smaller size from diagnosed FGR and avoids diagnosing loss or aneuploidy from dating discordance alone.
- Retains original clinical themes and adds early-report retrieval, cycle history, outside-date reconciliation, suboptimal dating and a reusable note template.
- References: ACOG CO 700/688; AIUM 2024 standard obstetric ultrasound; ISUOG 2025 twins and 2023 early scanning; SMFM Consult #52.
- Removed the catalog link to the legacy video because it accompanies the superseded presentation. The video itself was not modified.

## Validation

- Browser: 25 slides at 1440, 768, 390 and 320 pixels; one active slide, correct counter and no page-level horizontal overflow (100 checks).
- Keyboard arrows/Space, dropdown, source dialog/Escape, horizontal touch gesture, deep links and legacy static path checked.
- Quiz: all-correct and all-incorrect runs, all option explanations, 100%/0% scores, ten review items and retake reset passed.
- No JavaScript errors. All slides readable with JavaScript disabled. Native focusable controls, focus management, heading structure, named landmarks, semantic table, reduced-motion rules and diagram descriptions included. No claim of a formal WCAG certification.
- PDF export: 25 pages, one per slide; desktop, mobile and print screenshots inspected. Print colors adjusted for legibility.
- `npm test -- --runInBand --roots ./__tests__ --cacheDirectory ./tmp/dating-jest-cache`: four suites, 36 tests passed. Default unrestricted discovery encountered unrelated nested temporary checkout copies and sandbox cache errors.
- `npm run build` in `landing-page`: successful production static build. Initial sandbox run could not fetch Google Fonts; network-enabled retry passed.
- Catalog JSON updated in place, quiz link added, both sitemaps updated, canonical/social/structured metadata included. Legacy filename has a static fallback and a permanent Vercel redirect.

Runtime output and screenshots are retained locally in `tmp/dating-qa/`; they are not deployed.
