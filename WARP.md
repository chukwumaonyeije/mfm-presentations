# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a repository of standalone, keyboard-navigable HTML presentation decks focused on Maternal-Fetal Medicine (MFM) clinical topics. Each presentation is a self-contained HTML file with embedded CSS and JavaScript, designed for oral teaching with high-contrast, minimal text slides.

**Key characteristics:**
- No build process or package dependencies (pure HTML/CSS/JS)
- Each presentation is completely standalone (no external dependencies)
- Designed for clinical teaching to OB residents, fellows, and MFM providers
- Focus on "one point per slide" teaching methodology
- Medical content follows ACOG and SMFM guidelines

## Repository Structure

```
mfm-presentations/
├── [Topic Name]/
│   └── [topic-name].html    # Self-contained presentation
├── decks/                    # (currently empty, potential future location)
├── microsites/               # Interactive, multi-section web experiences
│   └── [microsite-name]/
│       ├── index.html
│       ├── css/
│       ├── js/
│       ├── images/
│       └── assets/
├── shared/                   # (currently empty, reserved for future shared assets)
│   ├── css/
│   ├── images/
│   └── js/
├── index.html                # Main presentations and microsites gallery
└── README.md
```

## Architecture

### Presentation HTML Structure

Each presentation follows this pattern:

1. **Header Section**: Complete `<style>` block with CSS custom properties for theming
   - Dark theme with medical-grade readability
   - CSS variables for colors: `--bg`, `--panel`, `--fg`, `--accent`, `--accent2`, `--ok`, `--warn`
   - Responsive grid layouts (`.cols-2`, `.cols-3`)
   - Card-based content organization

2. **Deck Container**: `.deck` → `.topbar` + `.progress` + `.slides`
   - Top bar shows title, slide counter, and keyboard shortcuts
   - Progress bar tracks position through deck
   - Slides container holds all presentation slides

3. **Individual Slides**: `<section class="slide">` elements
   - Only one slide has `.active` class at a time
   - Three-row grid: header, content, footer
   - Content uses card-based layouts for organization

4. **Navigation Script**: Inline `<script>` at end of file
   - Keyboard navigation: Arrow keys, Space, Home, End
   - Click/tap navigation: left third of screen = previous, rest = next
   - Auto-updates slide counter and progress bar

### Content Design Patterns

- **Teaching emphasis**: Use `.em` (accent color) for key clinical terms
- **Danger/warning**: Use `.danger` (red) and `.warn` (yellow) for critical info
- **Cards**: `.card` with `.k` (label) + content for structured information
- **Callouts**: `.callout` for important clinical pearls or warnings
- **Lists**: Concise bullet points, typically 3-5 per card
- **SVG diagrams**: Inline SVG for medical illustrations (e.g., Doppler waveforms)

## Working with This Repository

### Creating a New Presentation

1. Copy an existing presentation HTML file as a template
2. Update the `<title>` and `.title` content in the top bar
3. Update total slide count (search for `id="tot"`)
4. Replace slide content while maintaining the structural patterns
5. Adjust CSS custom properties if different color emphasis is needed
6. Test keyboard navigation (Arrow keys, Space, Home, End)

### Viewing Presentations

Open any HTML file directly in a web browser. No server or build step required.

**Keyboard shortcuts:**
- `→` or `Space` or `PageDown`: Next slide
- `←` or `PageUp`: Previous slide
- `Home`: First slide
- `End`: Last slide

### Medical Content Guidelines

When editing medical content:
- Follow ACOG Practice Bulletins and SMFM Consult Series recommendations
- Include evidence source citations in footer notes (e.g., "SMFM Consult #52")
- Use precise gestational age notation (e.g., "35 weeks", "34 0/7 weeks")
- Balance evidence-based recommendations with "local protocols" acknowledgment
- Maintain clinical nuance (avoid oversimplified "always/never" statements)

### Code Style Conventions

**CSS:**
- Use CSS custom properties for all colors (already defined in `:root`)
- Maintain mobile-responsive design (existing styles support this)
- Keep print styles functional (`@media print`)

**HTML:**
- Use semantic HTML5 elements
- Maintain ARIA attributes for accessibility
- Keep inline styles minimal (prefer CSS classes)

**JavaScript:**
- Navigation logic is self-contained and consistent across presentations
- Avoid external dependencies
- Keep it simple and fast

## File Naming

- Presentation folders: Title case with spaces (e.g., "IUGR and Abnormal Doppler")
- HTML files: Match folder name or use kebab-case for longer titles
- Keep names clinically descriptive

## Testing

Since there's no test suite, manual testing checklist:
1. Open HTML file in browser (Chrome, Firefox, Safari, Edge)
2. Test all keyboard navigation shortcuts
3. Test click/tap navigation (left vs right side)
4. Verify slide counter updates correctly
5. Check progress bar animation
6. Test print layout (`Ctrl/Cmd + P`)
7. Review medical content accuracy against source guidelines

## Common Patterns

### Adding a new slide

```html
<section class="slide">
  <div>
    <div class="h2">Slide Title</div>
    <div class="sub">Subtitle or context</div>
  </div>
  <div class="grid cols-2">
    <div class="card">
      <div class="k">Section Label</div>
      <ul>
        <li>Point one</li>
        <li>Point two with <span class="em">emphasis</span></li>
      </ul>
    </div>
    <div class="card">
      <div class="k">Another Section</div>
      <ul>
        <li>More content</li>
      </ul>
    </div>
  </div>
  <div class="footer">
    <span>Point: Key takeaway</span>
    <span class="note">Reference or note</span>
  </div>
</section>
```

### Adding a callout box

```html
<div class="callout">
  <div class="h">Heading</div>
  <div class="t">Important clinical point or teaching pearl.</div>
</div>
```

### Color-coded emphasis

- Use `.em` for standard clinical emphasis (cyan/blue)
- Use `.danger` for high-risk findings (red)
- Use `.ok` for reassuring findings (green)
- Use `.warn` for caution items (yellow)

## Adding Infographics to Presentations

When the user provides an infographic (PNG or JPEG) for a presentation:

1. **Save the Image File**
   - Location: Save to the appropriate deck folder (e.g., `decks/[topic-name]/`)
   - Naming: Use descriptive naming like `[topic]-infographic.png` or `.jpg`
   - Example: `decks/external-cephalic-version-breech/breech-infographic.png`

2. **Update index.html Card**
   - Add `has-infographic` class to the card `<div>` element
   - Add the infographic badge before other tags:
     ```html
     <span class="infographic-badge">Infographic Available</span>
     ```
   - Wrap the buttons in a button group:
     ```html
     <div class="button-group">
       <a href="path/to/presentation.html" class="btn">View Presentation</a>
       <a href="path/to/infographic.png" target="_blank" class="btn btn-infographic">View Infographic</a>
     </div>
     ```

3. **Complete Example Structure**
   ```html
   <div class="card has-infographic">
     <h2>Title</h2>
     <p>Description</p>
     <div>
       <span class="infographic-badge">Infographic Available</span>
       <span class="tag">Tag1</span>
       <span class="tag">Tag2</span>
     </div>
     <div class="button-group">
       <a href="decks/topic/presentation.html" class="btn">View Presentation</a>
       <a href="decks/topic/infographic.png" target="_blank" class="btn btn-infographic">View Infographic</a>
     </div>
   </div>
   ```

4. **Commit and Push**
   - Stage both the image file and index.html
   - Commit with descriptive message
   - Include co-author attribution: `Co-Authored-By: Warp <agent@warp.dev>`
   - Push to GitHub

## GitHub Pages Deployment

This repository is deployed to GitHub Pages using a custom GitHub Actions workflow (not Jekyll).

### Critical Files for Deployment

1. **`.nojekyll`** (empty file at root)
   - **Purpose**: Tells GitHub Pages to skip Jekyll processing
   - **Why it matters**: Without this, Jekyll would:
     - Strip CDN links (like Reveal.js from jsdelivr.net)
     - Ignore files/folders starting with underscores
     - Process liquid template syntax `{{ }}` incorrectly
   - **Never delete this file**

2. **`.github/workflows/deploy.yml`** (GitHub Actions workflow)
   - **Purpose**: Controls how the site is built and deployed
   - **Key feature**: `cancel-in-progress: true` prevents deployment queue backups
   - **Triggers**: Runs automatically on every push to `main` branch

### Deployment Settings

**GitHub Repository Settings** (https://github.com/chukwumaonyeije/mfm-presentations/settings/pages):
- **Source**: Must be set to **"GitHub Actions"** (not "Deploy from a branch")
- **Branch**: Main (this is where the workflow reads from)
- **Custom Domain**: None (uses default github.io URL)

### Troubleshooting Deployment Issues

**Problem**: Deployments stuck in "queued" status
- **Cause**: GitHub Pages concurrency limits (only one deployment at a time)
- **Solution**: The workflow's `cancel-in-progress: true` handles this automatically
- **Manual fix**: Cancel stuck workflows at https://github.com/chukwumaonyeije/mfm-presentations/actions

**Problem**: Pages not updating after push
- **Check**: Visit Actions tab to see if workflow completed successfully
- **Check**: Verify the workflow file exists at `.github/workflows/deploy.yml`
- **Check**: Ensure Pages source is set to "GitHub Actions" in repository settings

**Problem**: 404 errors or missing files
- **Check**: Verify `.nojekyll` file exists at repository root
- **Check**: File paths in index.html match actual file locations (case-sensitive)
- **Check**: CDN links are not being stripped by Jekyll (should be prevented by `.nojekyll`)

### Testing Deployments Locally

Since there's no build step:
1. Open `index.html` directly in a browser
2. Test all presentation links work
3. Verify infographic links open correctly
4. Check that external CDN resources load (Reveal.js, etc.)

### Deployment Workflow

The typical deployment process:
1. Make changes locally (add presentations, update index.html, etc.)
2. Commit with descriptive message + co-author attribution
3. Push to `main` branch
4. GitHub Actions automatically deploys (takes ~1-2 minutes)
5. Site updates at https://chukwumaonyeije.github.io/mfm-presentations/

**No manual deployment steps required** - the workflow handles everything.

## Presentation Ordering in index.html

**IMPORTANT**: When adding new presentations or updating existing ones:

1. **New Presentations**: Always add the card for a new presentation at the **very top** of the `<div class="presentations">` section in index.html (immediately after the opening tag)
2. **Amended Presentations**: When significantly updating an existing presentation, move its card to the **very top** of the presentations list
3. **Rationale**: This ensures the most recent and relevant content appears on the first page of results, making it immediately visible to users

**Implementation**:
- Place new/updated presentation cards at line ~320-325 (right after `<div class="presentations">`)
- Remove any duplicate entries if moving an existing presentation to the top
- Maintain consistent formatting and card structure

## Microsites

Microsites are a new content type that complements presentations. While presentations are linear, slide-based learning experiences, microsites are interactive, multi-section web experiences designed for deeper exploration of topics.

### Key Differences from Presentations

- **Presentations**: Linear (slides), one point per slide, keyboard/click navigation, oral teaching, single HTML file
- **Microsites**: Non-linear (sections), rich multi-paragraph content, tabbed/menu navigation, self-guided learning, multiple files, dual-audience support (patients + clinicians)

---

## 📘 Complete Guide: Creating and Deploying Microsites

### Step 1: Planning Your Microsite

Before creating a microsite, determine:

1. **Topic and Scope**: What clinical topic needs deep, multi-page exploration?
2. **Target Audiences**: Will it serve patients only, clinicians only, or both?
3. **Content Structure**: What sections/pages are needed? (e.g., Overview, Safety, FAQ, Clinician Toolkit)
4. **Interactive Elements**: What tools will be included? (e.g., calculators, decision aids, documentation templates)

**Example Structure (VKDB Microsite)**:
- Patient-facing page: Why it matters, Safety, Myths, FAQ, Printable handout
- Clinician page: Talk tracks, Documentation templates, Evidence responses

---

### Step 2: Create the Microsite Directory Structure

```bash
microsites/
└── [topic-name]/              # Use kebab-case (e.g., vitamin-k-deficiency-bleeding)
    ├── index.html             # Main entry point (patient-facing or general)
    ├── clinicians.html        # Optional: Clinician-specific content
    ├── assets/
    │   └── style.css          # All styles (inline or external)
    ├── images/                # Optional: Topic-specific images
    └── js/                    # Optional: Interactive scripts
```

**Create the folder**:
```bash
mkdir microsites\your-topic-name
mkdir microsites\your-topic-name\assets
```

---

### Step 3: Build the HTML Files

#### A. Patient-Facing Page (`index.html`)

**Key Components**:
1. **Header with Navigation**
   - Brand/logo area
   - Navigation menu with:
     - `← All Presentations` link (to `../../index.html`)
     - Section anchors (`#why`, `#safety`, `#myths`, `#faq`)
     - Link to clinician page (if applicable)

2. **Hero Section**
   - Clear value proposition
   - Key takeaways in callout boxes
   - Call-to-action buttons

3. **Content Sections**
   - Use semantic `<section id="section-name">` elements
   - Anchor-linked from navigation
   - Card-based layouts for readability

4. **Footer**
   - Medical disclaimer
   - Links back to main site

**Example Structure**:
```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Your Topic - Patient Guide</title>
  <link rel="stylesheet" href="assets/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container">
      <div class="brand">Topic Name</div>
      <nav>
        <a href="../../index.html">← All Presentations</a>
        <a href="#why">Why it matters</a>
        <a href="#safety">Safety</a>
        <a href="clinicians.html" class="nav-cta">Clinicians</a>
      </nav>
    </div>
  </header>
  
  <main>
    <section class="hero">
      <h1>Main Headline</h1>
      <p class="lead">Key message for patients</p>
    </section>
    
    <section id="why">
      <h2>Why This Matters</h2>
      <!-- Content -->
    </section>
  </main>
  
  <footer>
    <p>Medical disclaimer and attribution</p>
  </footer>
</body>
</html>
```

#### B. Clinician Page (`clinicians.html`)

**Key Components**:
1. **Navigation**
   - Link back to patient page: `<a href="index.html">Parent page</a>`
   - Link back to main site: `<a href="../../index.html">← All Presentations</a>`

2. **Clinician-Specific Content**
   - Talk tracks (30-second, 3-minute versions)
   - Common myths with evidence-based responses
   - Copy-paste documentation templates
   - Reference links and citations

3. **Interactive Elements**
   - Accordion sections for Q&A
   - Code blocks for copy-paste templates
   - Copy buttons for quick use

---

### Step 4: Style the Microsite

**Create `assets/style.css`** using the repository's standard color scheme:

```css
:root {
  --bg: #07111c;
  --panel: #0b1c2c;
  --fg: #f4f7fb;
  --muted: #b7c4d6;
  --accent: #35d0ff;
  --accent2: #ff4d6d;
  --line: #16324a;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Inter', ui-sans-serif, system-ui, sans-serif;
  background: var(--bg);
  color: var(--fg);
  line-height: 1.6;
}

/* Add your microsite-specific styles */
```

**Design Principles**:
- Maintain dark theme consistency with main site
- Use card-based layouts for content organization
- Ensure mobile responsiveness (media queries)
- Include accessibility features (ARIA labels, focus states)

---

### Step 5: Add Navigation to Main Index

**Edit the main `index.html` file** to add your microsite to the "Interactive Microsites" section:

```html
<!-- Find the "Interactive Microsites" section (around line 1205) -->
<div style="margin-top: 64px; margin-bottom: 48px;">
  <h2>🌐 Interactive Microsites</h2>
  
  <!-- Add your new microsite card -->
  <div class="card" style="border: 2px solid var(--accent); background: linear-gradient(180deg, rgba(53,208,255,.08), rgba(53,208,255,.02));">
    <h2>Your Topic Name - Interactive Microsite</h2>
    <p>Comprehensive description of what the microsite covers, target audience, and key features.</p>
    <div>
      <span class="tag" style="background: rgba(53,208,255,.15); border-color: rgba(53,208,255,.4);">🌐 Microsite</span>
      <span class="tag">Topic Tag 1</span>
      <span class="tag">Topic Tag 2</span>
    </div>
    <div class="button-group">
      <a href="microsites/your-topic-name/index.html" class="btn" style="background: var(--accent);">👨‍👩‍👧 For Parents</a>
      <a href="microsites/your-topic-name/clinicians.html" class="btn" style="background: #ff4d6d;">👨‍⚕️ For Clinicians</a>
    </div>
  </div>
</div>
```

**Important**: Place the new microsite card **after** existing microsites but **before** the `<div class="pagination">` section.

---

### Step 6: Test Locally

Before committing, test all functionality:

```bash
# Open main landing page
start index.html

# Test navigation:
# 1. Scroll to "Interactive Microsites" section
# 2. Click "For Parents" button → Should open your patient page
# 3. Click "For Clinicians" button → Should open your clinician page
# 4. Click "← All Presentations" → Should return to main index
# 5. Click "Parent page" (from clinician) → Should go to patient page
```

**Testing Checklist**:
- ✅ All navigation links work
- ✅ Section anchors scroll correctly
- ✅ Back navigation returns to main index
- ✅ Mobile responsiveness (resize browser)
- ✅ All buttons and interactive elements function
- ✅ Medical content is accurate
- ✅ No console errors (F12 developer tools)

---

### Step 7: Commit and Push to GitHub

**Stage all files**:
```bash
# Add microsite files
git add microsites/your-topic-name/

# Add updated main index
git add index.html
```

**Commit with descriptive message**:
```bash
git commit -m "Add [Topic Name] interactive microsite with patient and clinician toolkit

- Create patient-facing educational content with FAQ and myth-busting
- Add clinician toolkit with talk tracks and documentation templates
- Integrate navigation links to/from main presentations index
- Include responsive design and accessibility features

Co-Authored-By: Warp <agent@warp.dev>"
```

**Push to GitHub**:
```bash
git push origin main
```

---

### Step 8: Verify Deployment

**Automatic Deployment via GitHub Actions**:
1. Push triggers the workflow (`.github/workflows/deploy.yml`)
2. Wait 1-2 minutes for deployment
3. Visit: `https://chukwumaonyeije.github.io/mfm-presentations/`
4. Scroll to "Interactive Microsites" section
5. Click your new microsite buttons to verify

**Check Deployment Status**:
- Visit: https://github.com/chukwumaonyeije/mfm-presentations/actions
- Look for green checkmark on latest workflow run
- If red X, click to see error logs

**Common Issues**:
- **404 errors**: Check file paths are correct (case-sensitive)
- **Styles not loading**: Verify `assets/style.css` path in HTML
- **Navigation broken**: Confirm `../../index.html` relative path

---

## 📋 Quick Reference: Microsite Checklist

### Planning Phase
- [ ] Define topic and scope
- [ ] Identify target audiences (patient/clinician/both)
- [ ] Outline content sections
- [ ] Determine interactive features needed

### Build Phase
- [ ] Create directory: `microsites/[topic-name]/`
- [ ] Create `index.html` (patient page)
- [ ] Create `clinicians.html` (if needed)
- [ ] Create `assets/style.css`
- [ ] Add navigation with back links to main index
- [ ] Implement section anchors and smooth scrolling

### Integration Phase
- [ ] Add microsite card to main `index.html`
- [ ] Use proper styling (border, gradient background)
- [ ] Add 🌐 Microsite badge
- [ ] Include topic-specific tags
- [ ] Add "For Parents" and "For Clinicians" buttons

### Testing Phase
- [ ] Test all navigation links locally
- [ ] Verify mobile responsiveness
- [ ] Check section anchor scrolling
- [ ] Validate medical content accuracy
- [ ] Test in multiple browsers (Chrome, Firefox, Safari, Edge)

### Deployment Phase
- [ ] Stage all files (`git add`)
- [ ] Commit with descriptive message + co-author
- [ ] Push to GitHub (`git push origin main`)
- [ ] Verify deployment in Actions tab
- [ ] Test live site at github.io URL

---

## 🎨 Design Patterns for Microsites

### Navigation Bar
```html
<nav class="nav" aria-label="Primary navigation">
  <a href="../../index.html">← All Presentations</a>
  <a href="#section1">Section 1</a>
  <a href="#section2">Section 2</a>
  <a href="clinicians.html" class="nav-cta">Clinicians</a>
</nav>
```

### Hero Section
```html
<section class="hero">
  <div class="container hero-grid">
    <div>
      <h1>Main Headline</h1>
      <p class="lead">Compelling description</p>
      <div class="hero-actions">
        <a class="button primary" href="#cta">Primary CTA</a>
        <a class="button" href="#learn">Secondary CTA</a>
      </div>
    </div>
    <aside class="hero-card">
      <h2>At a glance</h2>
      <ul class="checklist">
        <li><span aria-hidden="true">✓</span> Key point 1</li>
        <li><span aria-hidden="true">✓</span> Key point 2</li>
      </ul>
    </aside>
  </div>
</section>
```

### Content Cards
```html
<div class="card">
  <h3>Card Title</h3>
  <p>Card content with detailed information.</p>
  <ul class="bullets">
    <li>List item 1</li>
    <li>List item 2</li>
  </ul>
</div>
```

### Accordion (for FAQ/Myths)
```html
<div class="accordion" data-accordion>
  <button class="accordion-item" aria-expanded="false">
    <span class="accordion-q">Question or claim</span>
    <span class="accordion-icon" aria-hidden="true">+</span>
  </button>
  <div class="accordion-panel" hidden>
    <p><strong>Response:</strong> Evidence-based answer.</p>
  </div>
</div>
```

### Copy-Paste Code Blocks (for clinicians)
```html
<div class="card">
  <h3>Documentation Template</h3>
  <pre class="codeblock" aria-label="Template">Template text here</pre>
  <button class="button" type="button" data-copy="0">Copy</button>
</div>
```

---

## 💡 Best Practices

### Content
- **Patient-facing**: Use plain language, avoid medical jargon, focus on "what this means for you"
- **Clinician-facing**: Include evidence levels, citation sources, copy-paste templates
- **Dual-audience**: Maintain consistent terminology but adjust depth/complexity

### Navigation
- **Always include**: Back link to main index on every page
- **Internal linking**: Use anchor links for long pages (`#section-id`)
- **Breadcrumbs**: Consider adding for complex microsites

### Accessibility
- Use semantic HTML (`<nav>`, `<main>`, `<section>`, `<article>`)
- Include ARIA labels for screen readers
- Ensure keyboard navigation works (Tab, Enter, arrows)
- Maintain color contrast ratios (WCAG AA minimum)

### Mobile Optimization
- Use responsive grid layouts (CSS Grid or Flexbox)
- Test on actual devices or browser dev tools
- Ensure touch targets are at least 44x44px
- Stack content vertically on narrow screens

### Performance
- Inline critical CSS or use single external stylesheet
- Optimize images (compress, use appropriate formats)
- Minimize JavaScript (vanilla JS preferred over frameworks)
- Avoid external dependencies where possible

---

## 🔗 Example: VKDB Microsite Structure

Reference the existing VKDB microsite as a template:

```
microsites/vitamin-k-deficiency-bleeding/
├── index.html              # Patient education page
│   ├── Hero: "Say yes to Vitamin K"
│   ├── Section: Why newborns need it
│   ├── Section: Safety information
│   ├── Section: Common myths
│   ├── Section: FAQ
│   └── Section: Printable handout
│
├── clinicians.html         # Clinician toolkit
│   ├── Hero: "Make evidence easy to deliver"
│   ├── Section: Talk tracks (60s and 3-min versions)
│   ├── Section: Myth responses
│   ├── Section: Documentation templates
│   └── Section: References
│
└── assets/
    └── style.css           # Shared styling
```

**File locations**:
- Patient page: `microsites/vitamin-k-deficiency-bleeding/index.html`
- Clinician page: `microsites/vitamin-k-deficiency-bleeding/clinicians.html`
- Styles: `microsites/vitamin-k-deficiency-bleeding/assets/style.css`

## Notes

- The `shared/` directory is currently empty but reserved for future modular components (CSS, JS, images)
- The `decks/` directory is empty; presentations currently live in topic-named folders
- The `microsites/` directory contains interactive, multi-section educational content
- No package.json or build system by design—presentations and microsites are deployment-ready as-is
- Presentations are optimized for 16:9 or 16:10 displays (typical conference projectors)
- Microsites are fully responsive and work on all modern devices
- **Deployment is automated via GitHub Actions** - see "GitHub Pages Deployment" section above
