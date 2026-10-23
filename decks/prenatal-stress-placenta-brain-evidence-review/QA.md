# Quality review

October 23, 2026 · OpenMFM Presentation Standard v1.0

## Content and teaching

- Approved outline implemented; final reference slide expanded into three readable slides (38 total).
- Explicit mouse versus human evidence labels; RNA expression distinguished from function and clinical outcomes.
- Reported IFN-beta ratio 0.19 (95% CI 0.04–0.98), adjusted p=0.047, and small biological sample sizes retained.
- Planned p=0.033 comparison distinguished from nonsignificant p=0.132 interaction.
- Human n=20, multiplicity, confounding, timing, cell capture, and unproven placental mediation addressed in slides and notes.
- No individual fetal-risk estimate, new fetal surveillance schedule, delivery indication, or fetal-protective treatment claim introduced.
- Patient segment includes practical support, screening-to-care pathways, therapy, individualized medication discussion, urgent assessment, questions, and educational/privacy statements.
- Original diagrams and an original chart use reported findings; no third-party figure reuse.

## Browser checks

Headless Chrome 146, local HTML:

- All 38 slides checked at 1440 × 900, 1280 × 720, and 390 × 844.
- One visible slide at a time; no document-level horizontal overflow.
- No desktop/laptop slide content extends beneath the available slide area after compact-height refinements.
- Narrow screens scroll vertically; tables and the chart have local horizontal scrolling where needed.
- Arrow, Home/End, selector, deep-link reload, out-of-range hash clamping, and swipe navigation tested.
- Speaker-note and reference dialogs open and close with Escape.
- Patient-mode entry, final-slide boundary, and deep-link restoration tested.
- Coping-option interaction changes the selected state and accessible feedback.
- No browser JavaScript errors.

## Accessibility and print

- Semantic headings, table headers, labeled navigation and progress, live slide announcements, focusable slide titles, visible focus styling, native modal dialogs, SVG text alternative, and reduced-motion styling are present.
- Keyboard behavior was tested; this is not a comprehensive screen-reader or formal WCAG certification.
- PDFs verified at 38 pages (full deck) and 12 pages (patient counseling with guideline references).
- No print container overflow. All 38 PDF pages inspected in a contact sheet, with selected full-size chart and reference pages inspected separately.
- Desktop and mobile screenshots inspected; print reference colors adjusted for white-background readability.

## Integration and limits

- Local homepage and presentation catalog entries added at the top; catalog JSON parses.
- Only the new deck URL was inserted into existing sitemap files, preserving their pre-existing edits.
- Review limits are disclosed in the notes and reference panel: full supplied paper reviewed, no raw-data reanalysis or standalone supplement audit, and some web full text access-restricted.
- Release prepared for commit, push, and production deployment; live verification is recorded separately after deployment.

## Publishing validation

- Production build passed: `npm run build -- --webpack`.
- Repository tests passed: 4 suites, 36 tests, using `npm test -- --runInBand --roots ./__tests__` to exclude an old embedded checkout.
- Initial sandbox attempts hit font-fetch and Jest-cache restrictions; both checks passed when rerun with the required permissions.
- Generated homepage feature contains the deck and both PDF links; exactly one catalog resource is featured.
- Deck has one canonical URL, repository SEO metadata, and an integrated library backlink without a duplicate fixed overlay.
