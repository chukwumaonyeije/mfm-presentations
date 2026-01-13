# Fetal Growth Restriction - Reveal.js Presentation

Patient education presentation on fetal growth restriction, monitoring, and delivery planning.

## Files

- `index.html` - Main Reveal.js presentation
- `theme.css` - Custom styling and theme
- `fetal-growth-restriction-patient.html` - Original version (for reference)

## Running the Presentation

### Option 1: Direct File Access (Recommended)
Simply open `index.html` in any modern web browser:
- **Windows**: Double-click `index.html` or right-click → Open with → Browser
- **Mac**: Double-click `index.html` or right-click → Open With → Browser
- **Linux**: Open with your preferred browser

The presentation loads Reveal.js from CDN (requires internet connection).

### Option 2: Local Web Server
For best results, especially when working offline or with additional assets:

```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js http-server (install: npm install -g http-server)
http-server -p 8000

# Using PHP
php -S localhost:8000
```

Then navigate to: `http://localhost:8000/index.html`

## Navigation

### Keyboard Controls
- **→ / Space / Page Down**: Next slide
- **← / Page Up**: Previous slide
- **Home**: First slide
- **End**: Last slide
- **F**: Fullscreen mode
- **S**: Speaker notes (if enabled)
- **O / ESC**: Slide overview
- **?**: Show keyboard shortcuts

### Mouse/Touch Controls
- **Click right side**: Next slide
- **Click left side**: Previous slide
- **Swipe left**: Next slide (mobile)
- **Swipe right**: Previous slide (mobile)
- **Use on-screen arrows**: Navigate

## Features

### Progressive Content Reveal
Many slides use `.fragment` class to progressively reveal content. Press space/→ multiple times on a slide to see all content.

### Responsive Design
- Automatically adapts to screen size
- Mobile-friendly layouts
- Touch navigation support

### Accessibility Features
- ARIA labels on tables
- Semantic HTML structure
- Keyboard navigation
- Focus indicators
- High contrast mode support
- Reduced motion support

### Visual Elements
- Custom color scheme optimized for medical presentations
- Animated timeline
- Comparison grids
- Highlighted key points
- Icon-enhanced sections

## Customization

### Changing Colors
Edit `theme.css` CSS variables at the top:

```css
:root {
    --background-color: #1a1a2e;
    --text-color: #eeeeee;
    --primary-color: #4fc3f7;
    --secondary-color: #81c784;
    --highlight-color: #ffd54f;
    --accent-color: #2d4059;
}
```

### Transition Effects
In `index.html`, modify the Reveal.initialize() options:

```javascript
transition: 'slide', // none/fade/slide/convex/concave/zoom
transitionSpeed: 'default', // default/fast/slow
```

### Adding Slides
Insert new `<section>` elements within the `<div class="slides">` container:

```html
<section>
    <h2>Your Title</h2>
    <p>Your content</p>
</section>
```

## Browser Compatibility

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support
- Mobile browsers: Full support

## Printing/PDF Export

1. Add `?print-pdf` to the URL: `index.html?print-pdf`
2. Use browser print function (Ctrl/Cmd + P)
3. Set destination to "Save as PDF"
4. Recommended settings:
   - Layout: Landscape
   - Margins: None
   - Background graphics: Enabled

## Troubleshooting

**Slides not loading?**
- Check internet connection (Reveal.js loads from CDN)
- Verify `theme.css` is in the same directory as `index.html`

**Content not displaying correctly?**
- Clear browser cache
- Try a different browser
- Check console for errors (F12)

**Mobile navigation issues?**
- Enable touch navigation in Reveal options
- Try landscape orientation for better visibility

## Credits

- **Framework**: [Reveal.js](https://revealjs.com/) by Hakim El Hattab
- **Content**: MFM patient education materials
- **Theme**: Custom medical presentation theme

## License

Educational use - Patient education materials for maternal-fetal medicine.
