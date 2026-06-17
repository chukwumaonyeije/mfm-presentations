# 📘 Complete Guide: Creating and Deploying Microsites

**Repository:** mfm-presentations  
**Last Updated:** February 11, 2026

---

## What Are Microsites?

Microsites are interactive, multi-page educational resources designed for both patients and clinicians. Unlike presentations (which are linear, slide-based), microsites provide deep exploration of topics with rich content, documentation templates, and navigation between patient and clinician views.

### Key Differences

| Feature | Presentations | Microsites |
|---------|--------------|------------|
| Format | Linear slides | Non-linear sections |
| Content | One point per slide | Rich multi-paragraph content |
| Navigation | Keyboard/click arrows | Menu/tabbed navigation |
| Use Case | Oral teaching | Self-guided learning |
| Structure | Single HTML file | Multiple files and pages |
| Audience | Single audience | Dual-audience (patient + clinician) |

---

## Step-by-Step Creation Process

### Step 1: Planning Your Microsite

Before building, define:

1. **Topic and Scope**
   - What clinical topic needs deep, multi-page exploration?
   - Example: Vitamin K Deficiency Bleeding (VKDB)

2. **Target Audiences**
   - Patients only?
   - Clinicians only?
   - Both? (recommended for maximum utility)

3. **Content Structure**
   - What sections/pages are needed?
   - Example: Overview, Safety, FAQ, Clinician Toolkit

4. **Interactive Features**
   - Calculators, decision aids, documentation templates?
   - Copy-paste code blocks for clinicians?

**Example: VKDB Microsite Structure**
- **Patient page**: Why it matters, Safety, Myths, FAQ, Printable handout
- **Clinician page**: Talk tracks, Documentation templates, Evidence responses

---

### Step 2: Create Directory Structure

**Folder Organization:**

```
microsites/
└── [topic-name]/              # Use kebab-case
    ├── index.html             # Patient-facing entry point
    ├── clinicians.html        # Clinician-specific content
    ├── assets/
    │   └── style.css          # All styling
    ├── images/                # Optional: topic images
    └── js/                    # Optional: interactive scripts
```

**Commands (PowerShell/CMD):**

```powershell
# Create microsite folder
mkdir microsites\your-topic-name
mkdir microsites\your-topic-name\assets

# Navigate to folder
cd microsites\your-topic-name
```

---

### Step 3: Build HTML Files

#### A. Patient-Facing Page (`index.html`)

**Required Components:**

1. **Header with Navigation**
   ```html
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
   ```

2. **Hero Section**
   ```html
   <section class="hero">
     <div class="container hero-grid">
       <div>
         <h1>Main Headline</h1>
         <p class="lead">Compelling patient-friendly description</p>
         <div class="hero-actions">
           <a class="button primary" href="#myths">See common myths</a>
           <a class="button" href="#why">Learn what it prevents</a>
         </div>
       </div>
       <aside class="hero-card">
         <h2>At a glance</h2>
         <ul class="checklist">
           <li><span>✓</span> Key point 1</li>
           <li><span>✓</span> Key point 2</li>
         </ul>
       </aside>
     </div>
   </section>
   ```

3. **Content Sections**
   ```html
   <section id="why" class="section">
     <div class="container">
       <h2>Why This Matters</h2>
       <div class="grid-2">
         <div class="card">
           <h3>Card Title</h3>
           <p>Content explaining the topic in patient-friendly language.</p>
         </div>
       </div>
     </div>
   </section>
   ```

4. **Footer**
   ```html
   <footer>
     <p><strong>Medical disclaimer:</strong> This page is for education and does not replace medical advice.</p>
   </footer>
   ```

#### B. Clinician Page (`clinicians.html`)

**Required Components:**

1. **Navigation**
   ```html
   <nav>
     <a href="../../index.html">← All Presentations</a>
     <a href="index.html">Parent page</a>
     <a href="#talk">Talk track</a>
     <a href="#doc">Documentation</a>
   </nav>
   ```

2. **Talk Tracks**
   ```html
   <section id="talk">
     <h2>Talk Track</h2>
     <div class="card">
       <h3>60-second version (default)</h3>
       <p>"Your counseling script here..."</p>
     </div>
   </section>
   ```

3. **Documentation Templates**
   ```html
   <section id="doc">
     <h2>Documentation Templates (copy/paste)</h2>
     <div class="card">
       <h3>Standard counseling note</h3>
       <pre class="codeblock">Counseled parent(s) on...</pre>
       <button class="button" type="button">Copy</button>
     </div>
   </section>
   ```

---

### Step 4: Style the Microsite

**Create `assets/style.css`** using the standard color scheme:

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

* { 
  margin: 0; 
  padding: 0; 
  box-sizing: border-box; 
}

body {
  font-family: 'Inter', ui-sans-serif, system-ui, sans-serif;
  background: var(--bg);
  color: var(--fg);
  line-height: 1.6;
}

/* Card-based layouts */
.card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 24px;
}

/* Responsive grid */
.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}
```

**Design Principles:**
- ✅ Maintain dark theme consistency
- ✅ Use card-based layouts for content
- ✅ Ensure mobile responsiveness
- ✅ Include accessibility features (ARIA labels)

---

### Step 5: Add to Main Index

**Edit main `index.html`** (find "Interactive Microsites" section around line 1205):

```html
<!-- Add after existing microsites, before pagination -->
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
```

---

### Step 6: Test Locally

**Open in Browser:**

```powershell
# From repository root
start index.html
```

**Testing Checklist:**

- ✅ Scroll to "Interactive Microsites" section
- ✅ Click "For Parents" → opens patient page
- ✅ Click "For Clinicians" → opens clinician page
- ✅ Click "← All Presentations" → returns to main index
- ✅ Click "Parent page" (from clinician) → goes to patient page
- ✅ Section anchors scroll smoothly
- ✅ Mobile responsive (resize browser window)
- ✅ No console errors (F12 developer tools)
- ✅ Medical content is accurate

---

### Step 7: Commit and Push

**Stage Files:**

```powershell
# Add microsite files
git add microsites/your-topic-name/

# Add updated main index
git add index.html
```

**Commit with Descriptive Message:**

```powershell
git commit -m "Add [Topic Name] interactive microsite with patient and clinician toolkit

- Create patient-facing educational content with FAQ and myth-busting
- Add clinician toolkit with talk tracks and documentation templates
- Integrate navigation links to/from main presentations index
- Include responsive design and accessibility features

Co-Authored-By: Warp <agent@warp.dev>"
```

**Push to GitHub:**

```powershell
git push origin main
```

---

### Step 8: Verify Deployment

**Automatic Deployment Process:**

1. Push triggers GitHub Actions workflow (`.github/workflows/deploy.yml`)
2. Wait 1-2 minutes for deployment
3. Visit: https://chukwumaonyeije.github.io/mfm-presentations/
4. Scroll to "Interactive Microsites" section
5. Test both buttons (Parents and Clinicians)

**Check Deployment Status:**

- **Actions Tab:** https://github.com/chukwumaonyeije/mfm-presentations/actions
- **Green checkmark** = successful deployment
- **Red X** = error (click to see logs)

**Common Issues:**

| Problem | Cause | Solution |
|---------|-------|----------|
| 404 errors | File paths incorrect (case-sensitive) | Verify exact paths in HTML |
| Styles not loading | CSS path wrong in `<link>` tag | Check `assets/style.css` path |
| Navigation broken | Relative path incorrect | Confirm `../../index.html` |
| Deployment queued | GitHub Pages concurrency limit | Workflow auto-cancels in-progress |

---

## Quick Reference Checklist

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
- [ ] Test in multiple browsers

### Deployment Phase
- [ ] Stage all files (`git add`)
- [ ] Commit with descriptive message + co-author
- [ ] Push to GitHub (`git push origin main`)
- [ ] Verify deployment in Actions tab
- [ ] Test live site at github.io URL

---

## Design Patterns Reference

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
        <li><span>✓</span> Key point 1</li>
        <li><span>✓</span> Key point 2</li>
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

### Accordion (FAQ/Myths)
```html
<div class="accordion" data-accordion>
  <button class="accordion-item" aria-expanded="false">
    <span class="accordion-q">Question or claim</span>
    <span class="accordion-icon">+</span>
  </button>
  <div class="accordion-panel" hidden>
    <p><strong>Response:</strong> Evidence-based answer.</p>
  </div>
</div>
```

### Copy-Paste Code Blocks
```html
<div class="card">
  <h3>Documentation Template</h3>
  <pre class="codeblock" aria-label="Template">Template text here</pre>
  <button class="button" type="button" data-copy="0">Copy</button>
</div>
```

---

## Best Practices

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
- Minimize JavaScript (vanilla JS preferred)
- Avoid external dependencies where possible

---

## Example: VKDB Microsite

**Reference the existing VKDB microsite as a template:**

```
microsites/vitamin-k-deficiency-bleeding/
├── index.html              # Patient education
│   ├── Hero: "Say yes to Vitamin K"
│   ├── Section: Why newborns need it
│   ├── Section: Safety information
│   ├── Section: Common myths
│   ├── Section: FAQ
│   └── Section: Printable handout
│
├── clinicians.html         # Clinician toolkit
│   ├── Hero: "Make evidence easy to deliver"
│   ├── Section: Talk tracks (60s + 3-min)
│   ├── Section: Myth responses
│   ├── Section: Documentation templates
│   └── Section: References
│
└── assets/
    └── style.css           # Shared styling
```

**File Locations:**
- Patient: `microsites/vitamin-k-deficiency-bleeding/index.html`
- Clinician: `microsites/vitamin-k-deficiency-bleeding/clinicians.html`
- Styles: `microsites/vitamin-k-deficiency-bleeding/assets/style.css`

---

## Need Help?

**Resources:**
- **WARP.md**: Technical implementation details
- **README.md**: Repository overview
- **VKDB Microsite**: Reference implementation

**Questions?**
- Open an issue on the GitHub repository
- Review existing microsite code for examples
- Check GitHub Actions logs for deployment issues

---

**Last Updated:** February 11, 2026  
**Created with assistance from:** Warp AI
