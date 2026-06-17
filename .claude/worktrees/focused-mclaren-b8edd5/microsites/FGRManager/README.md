# FGRManager

## Overview
An interactive clinical decision-support tool for managing pregnancies complicated by **fetal growth restriction (FGR)**. Implements the delivery-timing thresholds and surveillance framework from **SMFM Consult Series #52** (2020), driven by umbilical artery (UA) Doppler category.

## Pages
- **`landing.html`** — Marketing/overview page with feature highlights, SMFM threshold table, workflow steps, use cases, and author info.
- **`index.html`** — The clinical tool itself: enter patient inputs and instantly receive a risk tier, delivery window, countdown, surveillance schedule, corticosteroid eligibility, and BPP flag.

## Features
- **SMFM #52 Delivery Thresholds** — All four UA Doppler tiers: REDF (30–32w), AEDF (33–34w), decreased diastolic flow (~37w), and severe FGR with normal UA (~37w). Normal UA EFW 3–10th → 38–39w.
- **Delivery Countdown Badge** — Calculates weeks/days remaining from current GA to the target delivery window; flags when at or past the window.
- **Surveillance Schedule** — Doppler-category–specific NST/BPP frequency, UA Doppler interval, growth scan cadence, and MCA/ductus venosus guidance.
- **Corticosteroid Eligibility** — Auto-detects standard (<34w) and late-preterm (34–36+6w) thresholds with betamethasone dosing note.
- **BPP Alert System** — Color-coded flags for BPP 6/10 (amber) and ≤4/10 (red) with contextual guidance.
- **Copy & Print Summary** — One-click clipboard export for EMR documentation; print-optimized CSS for clean clinical output.
- **Dark / Light Theme** — Persistent via `localStorage`.
- **Flexible GA Input** — Accepts `32.4`, `32+4`, or `32w4d` formats.

## Clinical Guidelines
Based on:
- **SMFM Consult Series #52 (2020):** Medically Indicated Late-Preterm and Early-Term Deliveries
- **ACOG Practice Bulletin #204:** Fetal Growth Restriction

## Usage
Open `landing.html` in any modern web browser to start at the overview page, then click **Launch FGRManager** to open the tool (`index.html`). No server or dependencies required — both pages are standalone HTML files with embedded CSS and JavaScript.

## Target Audience
- Maternal-Fetal Medicine specialists
- Obstetricians
- Labor & Delivery and antepartum nurses
- Medical students, residents, and fellows
- Quality assurance and peer-review teams

## Disclaimer
This tool is for educational and quality-assurance purposes only. It does NOT provide medical advice, diagnosis, or treatment recommendations. Delivery timing decisions must account for maternal indications (preeclampsia, HELLP, abruption), fetal anomalies, PPROM, local NICU capabilities, and individual patient values. All therapeutic decisions must be made by a qualified healthcare provider in the context of the individual patient.

## Created By
[DoctorsWhoCode.blog](https://doctorswhocode.blog/) — Dr. Chukwuma Onyeije, MD, Maternal-Fetal Medicine Specialist
