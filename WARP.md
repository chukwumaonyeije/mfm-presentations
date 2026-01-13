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
├── shared/                   # (currently empty, reserved for future shared assets)
│   ├── css/
│   ├── images/
│   └── js/
├── index.html                # (currently empty)
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

## Notes

- The `shared/` directory is currently empty but reserved for future modular components (CSS, JS, images)
- The `decks/` directory is empty; presentations currently live in topic-named folders
- No package.json or build system by design—presentations are deployment-ready as-is
- Presentations are optimized for 16:9 or 16:10 displays (typical conference projectors)
