# Type 1 Diabetes in Pregnancy - Reveal.js Presentation

A comprehensive patient education presentation about managing Type 1 Diabetes during pregnancy, built with Reveal.js.

## Files

- **index.html** - Main presentation file using Reveal.js framework
- **theme.css** - Custom styling and theme
- **type1_diabetes_pregnancy.html** - Original HTML slideshow (archived)

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

Then open your browser to: `http://localhost:8000`

### Option 2: Direct File Access

Simply open `index.html` directly in your browser. Note: Some features may not work properly without a web server.

## Navigation

- **Arrow Keys**: Navigate between slides
  - `→` / `Space`: Next slide
  - `←`: Previous slide
  - `Home`: First slide
  - `End`: Last slide

- **Touch Gestures**: Swipe left/right on mobile devices

- **Mouse**: Click navigation arrows at bottom-right

- **Overview Mode**: Press `Esc` or `O` to see all slides

- **Fullscreen**: Press `F` to enter fullscreen mode

- **Speaker View**: Press `S` to open speaker notes (if available)

## Features

✅ **Progressive Content Reveal**: Content appears incrementally using fragments  
✅ **Responsive Design**: Optimized for desktop, tablet, and mobile  
✅ **Progress Bar**: Visual indicator at bottom of screen  
✅ **Slide Counter**: Shows current slide number (e.g., "5/16")  
✅ **Keyboard Navigation**: Full keyboard support  
✅ **Touch Navigation**: Swipe gestures on mobile  
✅ **Accessibility**: WCAG compliant with focus indicators and semantic HTML  
✅ **Print Support**: Optimized for printing/PDF export  
✅ **High Contrast Mode**: Supports user preference for high contrast  
✅ **Reduced Motion**: Respects user preference for reduced motion

## Accessibility Features

- Semantic HTML structure with proper heading hierarchy
- ARIA labels on interactive elements
- Keyboard navigation support
- Focus indicators for all interactive elements
- High contrast mode support
- Reduced motion support for users with vestibular disorders
- Screen reader friendly content structure

## Customization

### Changing Colors

Edit the CSS variables in `theme.css`:

```css
:root {
    --primary-color: #4a9eff;
    --primary-dark: #357abd;
    --bg-dark: #1a1a2e;
    --success-color: #52b788;
    --warning-color: #ffb703;
}
```

### Changing Transitions

In `index.html`, modify the Reveal.js initialization:

```javascript
transition: 'slide', // Options: none/fade/slide/convex/concave/zoom
```

### Adding Speaker Notes

Add speaker notes to any slide:

```html
<section>
    <h2>Slide Title</h2>
    <p>Slide content...</p>
    
    <aside class="notes">
        These notes are only visible in speaker view (press 'S')
    </aside>
</section>
```

## Exporting to PDF

1. Add `?print-pdf` to the URL: `http://localhost:8000/?print-pdf`
2. Open the browser's Print dialog (Ctrl/Cmd + P)
3. Set destination to "Save as PDF"
4. Set margins to "None"
5. Enable "Background graphics"
6. Save the PDF

## Browser Compatibility

- Chrome/Edge: Full support ✅
- Firefox: Full support ✅
- Safari: Full support ✅
- Mobile browsers: Full support ✅

## Credits

- **Framework**: [Reveal.js](https://revealjs.com/) v5.0.4
- **Content**: Patient education material for Type 1 Diabetes in pregnancy
- **Design**: Custom medical education theme

## License

Content is for educational purposes. Reveal.js is licensed under MIT.
