# GDM rebuild: evidence and quality review

Updated October 28, 2026 following approval of the 32-slide outline.

## Educational and clinical review

- Expanded the former 13-slide patient presentation into 32 focused slides.
- Preserved the original clinical topics, added the supplied one-step diagnostic pathway and early/overt-diabetes distinction, and separated laboratory diagnostic thresholds from home treatment goals.
- Corrected unsupported prevalence, insulin-production, medication-use, breastfeeding-effect, and 10-year diabetes-risk figures. Removed fixed ultrasound schedules, the “placenta ages faster” explanation, and categorical CGM claims.
- Distinguished ADA/ACOG's insulin preference from SMFM's metformin alternative, reaffirmed in 2024. Removed the unrelated SMFM Consult Series #58 reference.
- Included individualized surveillance, delivery windows, the 4,500-g cesarean discussion threshold, postpartum medication reassessment, 4–12-week OGTT, and ongoing screening.
- Added a hypoglycemia action sequence and shared-decision questions. Prescribing examples in the supplied text were not converted into self-dosing instructions.
- Linked 11 evidence sources at the relevant slides and in the full bibliography. Checked ADA 2026 diagnostic/management guidance, SMFM's published statement, ACOG surveillance guidance, screening-update bibliographic details, primary trial reports, and CDC hypoglycemia guidance. ACOG Practice Bulletin 190 full text is paywalled; its established delivery recommendations are retained with attribution, without claiming new 2026 ACOG guidance.
- The pasted evidence's orphan numerical citations were replaced by traceable references.

## Browser verification

Headless Chromium 156, with Playwright:

- All 32 slides checked at 1440×900, 768×1024, 390×844, and 320×640.
- No horizontal page overflow, including when optional clinical details are open.
- Keyboard arrows, Home/End, boundary buttons, direct slide hashes, and the slide selector passed.
- Sources search, Escape closing, and focus restoration passed. Explicit Escape handling avoids the search input consuming the key.
- Read-all mode and no-JavaScript fallback expose all 32 slides.
- Unique element IDs, inactive slide hiding, and absence of browser JavaScript errors checked.
- Reduced-motion CSS and semantic headings, table headers, labeled controls, progress and live status included.
- Desktop and phone screenshots visually inspected; mobile title spacing corrected.

## Print review

- Landscape A4 output contains 33 pages: 31 content slides and two pages of readable references.
- Optional clinical notes expand for printing. Every slide appears even from slide mode.
- Fixed navigation and dialogs are omitted; light print styling and linked references included.
- Diagnostic table/footer pagination corrected; no nearly empty overflow pages remain.
- Diagnostic and reference pages visually inspected. Browser-generated PDF is a temporary QA artifact, not a separately published download.

## Integration

- Original presentation URL preserved.
- Featured catalog metadata and static library feature updated; homepage featured audience derived from the entry's audience tag.
- Existing video/infographic links retained and labeled as earlier versions; these assets were not clinically updated in this work.
- Sitemap and SEO scripts executed with zero reported missing presentation files. The self-contained deck supplies its own metadata and integrated library link.
- Landing-page TypeScript check and Next.js production build passed. The build required network access for its existing Google Fonts dependencies. Existing unrelated working-tree changes are excluded from the GDM commit.
