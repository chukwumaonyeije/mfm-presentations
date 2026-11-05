# Pregnancy insulin initiation calculator

Version: **2.0.0**. Clinical validation confirmed by Chukwuma Onyeije, MD, on November 4, 2026. Source review: November 4, 2026.

## Where it lives

The original Firebase site was a single HTML file with inline CSS and JavaScript. This replacement is a standalone static microsite in the existing OpenMFM repository. It needs no Firebase project, API key, database, npm install, or external runtime dependency.

- `index.html`: clinical scope, inputs, results, references.
- `calculator.js`: pure calculation and validation, shared by browser and tests.
- `app.js`: form interaction, result invalidation, copy and print.
- `styles.css`: responsive dark OpenMFM layout and print styles.
- `../../__tests__/insulin-calculator.test.js`: independent numeric examples, boundary and interaction tests.

From the repository root run `python -m http.server 8765`, then open `http://localhost:8765/microsites/insulin-calculator/index.html`.
Run `npm test -- --runInBand --runTestsByPath __tests__/insulin-calculator.test.js`.

## Clinical model and limitations

Scope: clinician review of full basal–bolus initiation in insulin-naïve GDM, not treatment selection, patient self-dosing, or titration. The software does not assess glucose patterns or determine treatment eligibility; the scope acknowledgement is not a clinical screening algorithm.

The recovered app used trimester factors 0.7/0.8/0.9 units/kg/day, a 50/50 basal–bolus split, and a 33/33/34 meal split. The replacement retains the factors but makes the following assumptions explicit:

1. Current maternal weight, not prepregnancy or ideal weight; pounds × 0.45359237 converts to kg.
2. First band 1w0d–13w6d, second 14w0d–27w6d, third 28w0d–42w0d. No extra late-gestation increase.
3. Round the total only after full-precision multiplication, to 1 or 0.5 units (halfway upward). Basal gets the nearest half of the integer increments, with a spare increment assigned to basal. Split the remaining increments evenly over three meals, assigning remainders to breakfast then lunch. This allocation is arithmetic, not individualized meal dosing.
4. Weight support 30–200 kg and gestational support 1w0d–42w0d are software limits, not clinical safety thresholds. Values outside these limits are rejected.
5. No insulin preparation, basal injection frequency, correction factor, insulin-to-carbohydrate ratio, titration algorithm, or insulin-on-board calculation is selected.

The original age field did not affect dosing and has been removed. Original HTML min/max attributes were not enforced by a form submission. Decimal-week boundaries were inconsistent, results could become stale, and intermediate rounding produced inconsistent sums. These are corrected here.

## Evidence and sign-off

- ADA 2026, section 15: https://doi.org/10.2337/dc26-S015 . Supports individualized insulin care, monitoring, and frequent adjustment; it does **not** validate this exact algorithm or mandate 50/50 allocation.
- MEMS Practical Guide to Insulin Therapy in Type 2 Diabetes Mellitus, 2nd edition (2024), pregnancy section: https://mems.my/wp-content/uploads/2024/11/Practical-Guide-to-Insulin-Therapy-in-Type-2-Diabetes-Mellitus_2nd-Edition-2024-1.pdf . Search-indexed pregnancy table lists 0.7/0.8/0.9 by trimester. Full PDF retrieval timed out during source review; the clinical reviewer should inspect the full section and its applicability to insulin-naïve GDM.

The owner, Chukwuma Onyeije, MD, confirmed this version is validated and authorized publication on November 4, 2026. This approval covers the presented model and scope. Software tests independently verify the arithmetic and interface; they are not a clinical outcomes study. Subsequent protocol changes require renewed clinician review.

Screenshot example, 36w0d and 195 lb: exact weight 88.45051215 kg; raw daily estimate 79.605460935 units. Whole-unit allocation: total 80, basal 40, meals 14/13/13. Half-unit allocation: total 79.5, basal 40, meals 13.5/13/13.

## Publishing and future maintenance

Entries are included in the Next.js homepage feed, static interactive directory, and legacy library. This change alone does not publish the site. The repository's Vercel build copies the static site alongside the exported Next.js homepage. The intended path is `/microsites/insulin-calculator/index.html`.

Release 2.0.0 is indexable and included in both sitemaps. Deploy only the reviewed changes, preserving unrelated working-tree edits. Firebase remains unchanged; an old-site redirect would require separate Firebase access.

Future dosing changes belong in `calculator.js` and must update the independent expected-value tests and clinical documentation together. Test browser interaction, mobile layout, print output, and copy behavior as well as arithmetic before release.

No input values are transmitted or written to local/session storage. Copying is an explicit user action; printing uses the browser print dialog. Hosting may still retain ordinary access logs.
