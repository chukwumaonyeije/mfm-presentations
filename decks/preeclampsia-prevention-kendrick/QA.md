# Quality audit

September 30, 2026 | OpenMFM Presentation Standard v1.0

- **Source:** all five scanned PDF pages reviewed visually. Project is a proposed 12-week implementation; no outcomes invented. Uncited compliance and mortality-ranking claims omitted. Recruitment instructions were treated as source content, not executed.
- **Clinical accuracy:** ACOG/SMFM advisory, ACOG contraindication guidance, USPSTF recommendations/evidence, CDC warning signs, and the 2026 Khander dose-comparison trial verified. Guidelines, research evidence, project methods, and local adaptation are labeled separately.
- **User adaptation:** paper chart checklist replaces the unavailable eClinicalWorks smart-note mechanism. No specific scanning UI is assumed. Doctors/APPs confirm risk, prescribe through ordinary clinical processes, and sign the plan; staff route and file within their role.
- **Research integrity:** four original evaluation domains preserved. Clinical exceptions have distinct fields; investigator must predefine research mapping and align the changed workflow with the protocol before implementation. Patient forms are not research consent.
- **Privacy:** blank forms only; no PHI collected online, no storage or network submission code. Chart identifiers remain on clinical pages; audit worksheet uses approved IDs and no identified free text. No source contact details or signatures reproduced.
- **MARP:** rendered with @marp-team/marp-core. Editable slides.md and theme.css supplied. Public HTML has no runtime dependency or external script.
- **Desktop/mobile:** all 26 slides checked at 1440x1000 and 390x844. No detected content overflow or horizontal mobile overflow. Representative desktop, mobile, and printed slides inspected visually.
- **Navigation:** next, Home, End, hash navigation, and references dialog checked. Nine citations in the reference panel. All local links resolve. Horizontal touch navigation implemented; vertical scrolling retained on mobile.
- **Accessibility:** language, semantic headings, labeled controls, slide chooser, focus states, live status, skip link, dialog, keyboard handling, reduced-motion styles, and no-JavaScript reading fallback included.
- **Print:** final presentation PDF has exactly 26 pages. Checklist PDF has exactly three Letter pages; audit PDF has one Letter page. All four form pages inspected visually. Browser-print HTML versions independently produce three and one pages. Scenario answers are expanded in the presentation PDF.
- **Repository:** new catalog entry, landing card with form/PDF links, canonical metadata and JSON-LD, and both sitemap entries. JSON and XML parsed successfully; targeted git diff whitespace check passed. Existing unrelated work was preserved.
- **Publish validation:** repository Jest checks passed (14 suites, 150 tests); `npm run build` in landing-page passed, including TypeScript and static export. Sitemap and SEO generators ran successfully. Library backlink is integrated into the presentation toolbar to avoid overlap with slide navigation. Publication authorized by the user through the publish-openmfm-presentation skill; live verification is recorded in the publishing chat and Git history.

Machine-readable browser checks: qa-results.json.

## Regeneration

For authoring only, install `@marp-team/marp-core` and run `node build.cjs`. The build also supports the session-local renderer at `../../tmp/preeclampsia-tools/node_modules`. Run `build_forms.py` with ReportLab to regenerate the blank PDFs and printable HTML. Headless browser verification/PDF export is in `verify.cjs` and requires Puppeteer and a compatible Chrome executable. The finished presentation and forms do not require these authoring tools.
