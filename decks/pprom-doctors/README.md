# PPROM: Clinical Management Update

Evidence-based clinical presentation on Preterm Premature Rupture of Membranes (PPROM) for healthcare providers, built with Reveal.js.

## Files

- **index.html** - Main Reveal.js presentation (27 slides)
- **theme.css** - Custom clinical theme with color-coded content boxes
- **pprom-doctors.html** - Original scroll-based presentation (archived)

## Running the Presentation

### Option 1: Using a Local Web Server (Recommended)

#### Python 3
```bash
python -m http.server 8000
```

#### Python 2
```bash
python -m SimpleHTTPServer 8000
```

#### Node.js (using npx)
```bash
npx http-server -p 8000
```

#### PHP
```bash
php -S localhost:8000
```

Then open: `http://localhost:8000`

### Option 2: Direct File Access

Open `index.html` directly in your browser. Note: Some features may work better with a web server.

## Navigation

### Keyboard
- `→` / `Space` / `Page Down`: Next slide
- `←` / `Page Up`: Previous slide
- `Home`: First slide
- `End`: Last slide
- `Esc` / `O`: Overview mode (see all slides)
- `F`: Fullscreen mode
- `S`: Speaker notes (if available)
- `B` / `.`: Pause (blackout)

### Mouse/Touch
- Click navigation arrows (bottom right)
- Swipe left/right on touch devices

### Other Features
- Progress bar at bottom shows position in presentation
- Slide counter (current/total) in bottom right
- Fragment animations reveal content progressively

## Content Structure

### Learning Objectives (27 slides)
1. **Epidemiology & Pathophysiology** - Understanding PPROM fundamentals
2. **Diagnosis** - Clinical criteria and ancillary testing
3. **Management by GA** - Gestational age-specific protocols
4. **Evidence-Based Interventions** - Antibiotics, steroids, magnesium sulfate
5. **Maternal & Fetal Risks** - Comprehensive risk counseling
6. **Areas of Controversy** - Current debates and evolving practices
7. **Clinical Pearls & Summary** - Key takeaways for practice

### Color-Coded Content

- **Blue boxes** - Standard clinical content
- **Green boxes** - Evidence-based recommendations (Level A)
- **Red boxes** - Warnings and critical contraindications
- **Yellow boxes** - Consensus recommendations (Level C)
- **Evidence levels** - Color-coded badges (A/B/C)

## Features

✅ **Progressive Content Reveal**: Fragment animations for step-by-step learning  
✅ **Responsive Design**: Desktop, tablet, and mobile optimized  
✅ **Evidence Levels**: ACOG-style evidence grading (Level A/B/C)  
✅ **Clinical Protocols**: Formatted medication dosing and regimens  
✅ **Timeline Visualization**: GA-specific management overview  
✅ **Accessibility**: WCAG compliant with keyboard navigation  
✅ **Print Support**: Optimized for PDF export/printing  

## Exporting to PDF

1. Add `?print-pdf` to the URL: `http://localhost:8000/?print-pdf`
2. Open browser Print dialog (Ctrl/Cmd + P)
3. Set destination to "Save as PDF"
4. Set margins to "None"
5. Enable "Background graphics"
6. Save the PDF

## Customization

### Changing Colors

Edit CSS variables in `theme.css`:

```css
:root {
    --primary-color: #4A90E2;
    --success-color: #2ECC71;
    --warning-color: #E74C3C;
    --caution-color: #F1C40F;
}
```

### Changing Transitions

In `index.html`, modify the Reveal.js initialization:

```javascript
transition: 'slide', // Options: none/fade/slide/convex/concave/zoom
transitionSpeed: 'default', // Options: default/fast/slow
```

## Target Audience

- Maternal-Fetal Medicine specialists
- Obstetricians
- OB/GYN residents and fellows
- Labor & delivery nurses
- Perinatal healthcare providers

## Evidence Sources

- ACOG Practice Bulletin No. 217 (2020)
- ACOG Committee Opinions
- PPROMT Trial (Morris et al., Lancet 2016)
- NICHD MFMU Network studies

## Browser Compatibility

- Chrome/Edge: Full support ✅
- Firefox: Full support ✅
- Safari: Full support ✅
- Mobile browsers: Full support ✅

## Credits

- **Framework**: [Reveal.js](https://revealjs.com/) v5.0.4
- **Content**: Evidence-based PPROM clinical management
- **Design**: Clinical education theme with color-coded evidence levels

## License

Content is for educational purposes. Reveal.js is licensed under MIT.
