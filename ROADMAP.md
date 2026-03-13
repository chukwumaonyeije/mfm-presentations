# OpenMFM.org — Project Roadmap

> **Site:** [openmfm.org](https://openmfm.org)  
> **Repo:** [github.com/chukwumaonyeije/mfm-presentations](https://github.com/chukwumaonyeije/mfm-presentations)  
> **Author:** Dr. Chukwuma Onyeije, MD — Maternal-Fetal Medicine Specialist  
> **Last Updated:** 2026-03-13

---

## ✅ Completed

### Foundation (Early 2025)
- Initial site scaffolding with `index.html` as the presentation library
- GitHub Pages deployment via GitHub Actions (`.github/workflows/`)
- PWA support: favicon, `site.webmanifest`, mobile-ready icons
- Search bar built into `index.html`
- Video link support on individual deck cards
- Infographic badge/button integration on deck cards
- Pagination (`Show More / Less`) for large card lists
- `WARP.md` documenting GitHub Pages deployment setup

### Content Build-Out (Ongoing)
- **82 evidence-based clinical presentations** across 12 categories:
  - Hypertension & Preeclampsia
  - Diabetes & Metabolic
  - Fetal Growth & Doppler
  - Fetal Cardiology
  - Genetics & Carrier Screening
  - Fetal Anomalies (incl. Vein of Galen Malformation)
  - Infectious Disease
  - Placenta & Obstetric Complications
  - Twin Pregnancy
  - Prenatal Screening & Counseling
  - Medical Conditions in Pregnancy
  - GYN / Women's Health
- **8 interactive clinical microsites:**
  - Preeclampsia Screener (preeclampsia-screener.com)
  - FGRManager (SMFM #52 delivery timing)
  - GDM Screener (ACOG 2024 PB #190)
  - HTN in Pregnancy Screener (ACOG PB #222)
  - Fetal Growth Biometry Calculator (INTERGROWTH-21st / Hadlock / WHO)
  - Vitamin K Deficiency Bleeding (VKDB) Microsite
  - Preterm Birth Risk Screener
  - Fetal Kick Count Microsite (+ mobile-optimized version)

### SEO & AI Optimization (Phase 1 — March 2026)
- Added `<meta>` SEO tags, Open Graph tags, and `<noscript>` fallback to `index.html`
- Created `sitemap.xml` listing all presentation URLs
- Created `robots.txt` explicitly welcoming all major AI crawlers (GPTBot, ClaudeBot, Google-Extended, PerplexityBot, etc.)
- Created `llms.txt` — LLM-optimized navigation index per the llms.txt standard
- Created `llms-full.txt` — extended content summary for AI/LLM ingestion
- Added author attribution and citation guidance for AI models

### Next.js Landing Page (Phase 2 — March 2026)
- Built `landing-page/` as a Next.js (App Router) project
- Modern branded landing page served at `openmfm.org/`
- Full searchable library with faceted tag filtering served at `openmfm.org/library`
- `presentations.json` as the single source of truth for all deck metadata (title, href, tags)
- SEO `<head>` metadata via Next.js `layout.tsx`

### Sitemap Automation & OG Image (Phase 3 — March 2026)
- `generate_sitemap.py` — generates `landing-page/public/sitemap.xml` and root `sitemap.xml` from `presentations.json`
- Branded Open Graph image (`og-image.png`) for social sharing
- Vercel build pipeline: `generate_sitemap.py` runs on every deploy, keeping sitemaps current

### Brand Design Upgrade (March 2026)
- Space Grotesk typeface for headings
- Animated ECG pulse line in the hero section
- Cinematic dark gradient background with radial glow
- Cyan accent color (`#22d3ee`) throughout; card glow effects
- Fixed Space Grotesk font weight to maximum allowed (700)

### OpenMFM.org Domain Launch (March 2026)
- Custom domain `openmfm.org` via Vercel DNS
- `www.openmfm.org` → `openmfm.org` permanent redirect (vercel.json)
- All canonical URLs migrated from `chukwumaonyeije.github.io/mfm-presentations/` to `openmfm.org`
- `llms.txt` and `llms-full.txt` updated to use `openmfm.org` as primary URL
- Security headers added: `X-Content-Type-Options`, `X-Frame-Options`, `X-XSS-Protection`, `Referrer-Policy`

### SEO Index Maintenance (March 2026)
- Added Vein of Galen Malformation and Preterm Birth Risk Screener to `presentations.json`, `llms.txt`, and `llms-full.txt`
- Updated presentation count: 82 presentations + 8 microsites
- `generate_sitemap.py` now writes canonical `openmfm.org` URLs to both sitemaps
- Removed stale `clubfoot_patient_consultation.html` (superseded by `-new` and `-old` versions)

---

## 🔜 Near-Term (High Priority)

### Google Search Console Setup
- Verify ownership of `openmfm.org` in [Google Search Console](https://search.google.com/search-console)
- Submit `https://openmfm.org/sitemap.xml` for indexing
- Monitor crawl errors and coverage report
- Request indexing for top priority pages if needed

### JSON-LD Structured Data on Deck Pages
- Add `<script type="application/ld+json">` to individual deck HTML files
- Use `MedicalWebPage` or `Article` schema from [Schema.org](https://schema.org)
- Key fields: `name`, `description`, `author`, `publisher`, `datePublished`, `url`, `about`
- Enables Google rich results for medical content

### Fix Canonical URLs on Individual Deck Pages
- Individual decks still have `og:url` pointing to `chukwumaonyeije.github.io/...`
- Update to `https://openmfm.org/decks/...` for correct canonical signaling
- Can be scripted across all ~81 HTML files

### New Deck Checklist / Automation
- Currently, adding a new deck requires manual updates to: `index.html`, `presentations.json`, `llms.txt`, `llms-full.txt`
- Create a script or checklist (`NEW_DECK.md`) to document the steps and prevent gaps
- Consider a `generate_data.py` → `presentations.json` pipeline driven by scanning the `decks/` folder

---

## 📋 Medium-Term

### Analytics
- Add [Plausible Analytics](https://plausible.io) (privacy-friendly) or Google Analytics 4 to `openmfm.org`
- Track top presentations, search queries, and referral sources
- Use data to prioritize new content

### Deck Backlinks to openmfm.org
- Each presentation deck currently has no link back to the main site
- Add a small branded footer or header bar on each deck: "Part of the OpenMFM Library — openmfm.org"
- Improves user navigation and internal linking for SEO

### Library UX Improvements
- Add category/section browsing (sidebar or tab nav) to `/library`
- "Recently Added" or "Recently Updated" badge/filter
- Keyboard shortcut for search focus

### Custom 404 Page
- Create a branded `404.html` / Next.js `not-found.tsx` page
- Link back to the library so users don't dead-end on broken links

### RSS / Atom Feed
- Publish an RSS feed at `openmfm.org/feed.xml` for new presentations
- Allows OB/GYN providers and educators to subscribe to content updates

---

## 🌟 Long-Term / Stretch Goals

### Structured Clinical Metadata
- Add SNOMED CT / ICD-10 codes to each presentation in `presentations.json`
- Enables integration with EHR systems and clinical decision support tools
- Improves medical AI retrieval accuracy

### Citation Generator
- Add a "Cite This" button on each deck page
- Output APA, AMA, and MLA citation formats for each presentation
- Supports academic use and proper attribution

### Multilingual Support
- Spanish translation of top patient education decks (preeclampsia, GDM, NIPT, etc.)
- High impact given the patient population in U.S. maternal-fetal medicine practices

### PDF / Print Export
- "Download as PDF" button on individual decks
- Useful for printing in-office patient handouts

### Contact / About Page
- Dedicated About page on `openmfm.org/about`
- Professional bio, institutional affiliation, DoctorsWhoCode.blog cross-link
- Contact form or email link for collaboration/feedback

### Social Sharing Integration
- Share buttons on deck pages (X/Twitter, LinkedIn, WhatsApp)
- Pre-filled share text optimized for each presentation topic

---

## 📁 Key Files Reference

| File | Purpose |
|------|---------|
| `index.html` | GitHub Pages library (legacy, still in use) |
| `landing-page/app/page.tsx` | Next.js homepage |
| `landing-page/app/layout.tsx` | Global SEO metadata |
| `landing-page/data/presentations.json` | **Source of truth** for all deck/microsite metadata |
| `generate_sitemap.py` | Generates both sitemaps from `presentations.json` |
| `sitemap.xml` | Root sitemap (openmfm.org canonical URLs) |
| `landing-page/public/sitemap.xml` | Same sitemap served via Vercel |
| `llms.txt` | LLM navigation index (AI crawlers) |
| `llms-full.txt` | Extended AI content summary |
| `robots.txt` | Crawler permissions incl. AI bots |
| `vercel.json` | Vercel build config, redirects, headers |

---

## 🔄 Maintenance Checklist (Every New Deck)

When adding a new presentation, update **all** of the following:

1. Add HTML file to `decks/<folder>/`
2. Add entry to `index.html` (for GitHub Pages library)
3. Add entry to `landing-page/data/presentations.json`
4. Add entry to `llms.txt` (in the correct category section)
5. Update `llms.txt` presentation count
6. Update `llms.txt` `Last Updated` date
7. Update `llms-full.txt` `Last Updated` date
8. Run `python generate_sitemap.py` to regenerate both sitemaps
9. Commit and push → Vercel auto-deploys
