# Microsites Guide

Microsites are standalone, feature-rich web experiences integrated into the mfm-presentations repository. Unlike presentations (which are linear, slide-based), microsites offer interactive, non-linear content exploration with multiple pages, navigation flows, and rich media integration.

## Directory Structure

```
microsites/
├── vitamin-k-deficiency-bleeding/
│   ├── index.html              # Main entry point
│   ├── css/
│   │   └── style.css           # Microsite-specific styles
│   ├── js/
│   │   └── script.js           # Microsite-specific scripts
│   ├── images/
│   │   └── [image files]
│   ├── assets/
│   │   └── [videos, PDFs, etc.]
│   └── README.md               # Microsite documentation
```

## Creating a New Microsite

### 1. Set Up Folder Structure

```bash
mkdir microsites/[microsite-name]
mkdir microsites/[microsite-name]/css
mkdir microsites/[microsite-name]/js
mkdir microsites/[microsite-name]/images
mkdir microsites/[microsite-name]/assets
```

### 2. Create `index.html`

Each microsite starts with a self-contained HTML file. Use this template as a starting point:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Microsite Title]</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="microsite-container">
        <header class="microsite-header">
            <h1>[Microsite Title]</h1>
            <p class="subtitle">[Brief Description]</p>
            <a href="../index.html" class="back-link">← Back to Presentations</a>
        </header>

        <nav class="microsite-nav">
            <ul>
                <li><a href="#section-1" class="nav-link active">Section 1</a></li>
                <li><a href="#section-2" class="nav-link">Section 2</a></li>
                <li><a href="#section-3" class="nav-link">Section 3</a></li>
            </ul>
        </nav>

        <main class="microsite-content">
            <section id="section-1" class="content-section active">
                <h2>Section 1</h2>
                <!-- Content goes here -->
            </section>

            <section id="section-2" class="content-section">
                <h2>Section 2</h2>
                <!-- Content goes here -->
            </section>

            <section id="section-3" class="content-section">
                <h2>Section 3</h2>
                <!-- Content goes here -->
            </section>
        </main>

        <footer class="microsite-footer">
            <p>&copy; 2026 MFM Educational Resources</p>
        </footer>
    </div>

    <script src="js/script.js"></script>
</body>
</html>
```

### 3. Create `css/style.css`

Use this as a base CSS template:

```css
:root {
    --bg: #1a1a1a;
    --panel: #2d2d2d;
    --fg: #e0e0e0;
    --accent: #00d4ff;
    --accent2: #ff6b9d;
    --ok: #00ff88;
    --warn: #ffb800;
    --border: #404040;
    --spacing-xs: 0.5rem;
    --spacing-sm: 1rem;
    --spacing-md: 1.5rem;
    --spacing-lg: 2rem;
    --spacing-xl: 3rem;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    background-color: var(--bg);
    color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    height: 100%;
}

.microsite-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--spacing-lg);
}

.microsite-header {
    margin-bottom: var(--spacing-xl);
    padding-bottom: var(--spacing-lg);
    border-bottom: 2px solid var(--border);
}

.microsite-header h1 {
    font-size: 2.5rem;
    margin-bottom: var(--spacing-sm);
    color: var(--accent);
}

.microsite-header .subtitle {
    font-size: 1.1rem;
    color: var(--fg);
    margin-bottom: var(--spacing-md);
    opacity: 0.8;
}

.back-link {
    display: inline-block;
    color: var(--accent);
    text-decoration: none;
    font-size: 0.95rem;
    padding: var(--spacing-xs) var(--spacing-sm);
    border: 1px solid var(--accent);
    border-radius: 4px;
    transition: all 0.2s ease;
}

.back-link:hover {
    background-color: var(--accent);
    color: var(--bg);
}

.microsite-nav {
    margin-bottom: var(--spacing-lg);
}

.microsite-nav ul {
    list-style: none;
    display: flex;
    gap: var(--spacing-md);
    flex-wrap: wrap;
}

.microsite-nav .nav-link {
    color: var(--fg);
    text-decoration: none;
    padding: var(--spacing-sm) var(--spacing-md);
    border-bottom: 2px solid transparent;
    transition: all 0.2s ease;
    cursor: pointer;
}

.microsite-nav .nav-link:hover,
.microsite-nav .nav-link.active {
    color: var(--accent);
    border-bottom-color: var(--accent);
}

.microsite-content {
    flex: 1;
    margin-bottom: var(--spacing-xl);
}

.content-section {
    display: none;
    animation: fadeIn 0.3s ease;
}

.content-section.active {
    display: block;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.content-section h2 {
    font-size: 2rem;
    margin-bottom: var(--spacing-lg);
    color: var(--accent);
}

.content-section p {
    margin-bottom: var(--spacing-md);
    font-size: 1rem;
    line-height: 1.8;
}

.content-section ul, .content-section ol {
    margin-left: var(--spacing-lg);
    margin-bottom: var(--spacing-md);
}

.content-section li {
    margin-bottom: var(--spacing-sm);
}

.card {
    background-color: var(--panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: var(--spacing-md);
    margin-bottom: var(--spacing-md);
}

.card h3 {
    color: var(--accent2);
    margin-bottom: var(--spacing-sm);
}

.card p {
    margin-bottom: 0;
}

.microsite-footer {
    padding-top: var(--spacing-lg);
    border-top: 2px solid var(--border);
    text-align: center;
    font-size: 0.9rem;
    opacity: 0.6;
}

@media (max-width: 768px) {
    .microsite-container {
        padding: var(--spacing-md);
    }

    .microsite-header h1 {
        font-size: 1.8rem;
    }

    .microsite-nav ul {
        flex-direction: column;
        gap: var(--spacing-sm);
    }

    .microsite-nav .nav-link {
        display: block;
        padding: var(--spacing-sm);
    }
}

@media print {
    .microsite-nav,
    .back-link {
        display: none;
    }

    .microsite-container {
        max-width: 100%;
    }
}
```

### 4. Create `js/script.js`

Use this as a base JavaScript template:

```javascript
// Smooth scrolling and section navigation
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.content-section');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links and sections
            navLinks.forEach(l => l.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Show corresponding section
            const sectionId = this.getAttribute('href').substring(1);
            const section = document.getElementById(sectionId);
            if (section) {
                section.classList.add('active');
                section.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Keyboard navigation (arrow keys)
    document.addEventListener('keydown', function(e) {
        const activeLink = document.querySelector('.nav-link.active');
        const links = Array.from(navLinks);
        const currentIndex = links.indexOf(activeLink);

        if (e.key === 'ArrowRight' && currentIndex < links.length - 1) {
            links[currentIndex + 1].click();
        } else if (e.key === 'ArrowLeft' && currentIndex > 0) {
            links[currentIndex - 1].click();
        }
    });

    // Home and End key navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Home') {
            navLinks[0].click();
        } else if (e.key === 'End') {
            navLinks[navLinks.length - 1].click();
        }
    });
});
```

### 5. Add Microsite to index.html

Add a microsite card to the main `index.html` presentations grid. Use this structure:

```html
<div class="card has-microsite">
    <h2>[Microsite Title]</h2>
    <p>[Description]</p>
    <div>
        <span class="microsite-badge">Interactive Microsite</span>
        <span class="tag">[Tag1]</span>
        <span class="tag">[Tag2]</span>
    </div>
    <div class="button-group">
        <a href="microsites/[microsite-name]/index.html" class="btn btn-microsite">Explore Microsite</a>
    </div>
</div>
```

### 6. Update CSS in index.html for Microsite Cards

Add this CSS to the `<style>` block in index.html (if not already present):

```css
.has-microsite {
    border: 2px solid var(--accent);
}

.microsite-badge {
    display: inline-block;
    background-color: var(--accent);
    color: var(--bg);
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-right: var(--spacing-sm);
}

.btn-microsite {
    background-color: var(--accent);
    color: var(--bg);
}

.btn-microsite:hover {
    background-color: var(--accent2);
}
```

## Microsite Naming Conventions

- **Folder names**: kebab-case (e.g., `vitamin-k-deficiency-bleeding`)
- **HTML files**: Use `index.html` for the main entry point
- **CSS/JS files**: Descriptive names (e.g., `style.css`, `script.js`)
- **Image files**: Descriptive kebab-case naming (e.g., `vitamin-k-pathway.png`)

## Best Practices

1. **Self-Contained**: Each microsite should be independent with no external CDN dependencies (except for fonts if needed)
2. **Responsive Design**: Test on mobile, tablet, and desktop viewports
3. **Navigation**: Implement clear, intuitive navigation between sections
4. **Performance**: Optimize images and minimize JavaScript
5. **Accessibility**: Use semantic HTML, ARIA labels, and sufficient color contrast
6. **Back Navigation**: Always include a "Back to Presentations" link
7. **Consistency**: Use the theme colors defined in CSS custom properties
8. **Documentation**: Create a README.md in each microsite folder explaining its content and structure

## Deployment

Microsites are deployed automatically via GitHub Actions (same as presentations):

1. Create the microsite folder structure with all HTML, CSS, and JS files
2. Add a card to `index.html` with the microsite link
3. Commit all changes with a descriptive message
4. Push to `main` branch
5. GitHub Actions deploys automatically

No special build steps required—microsites are served as-is.

## Example Microsite Structure

For the Vitamin K Deficiency Bleeding microsite:

```
microsites/vitamin-k-deficiency-bleeding/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── images/
│   ├── vitamin-k-pathway.png
│   ├── coagulation-cascade.png
│   └── vkdb-timeline.png
├── assets/
│   └── [any videos or PDFs]
└── README.md
```

## Troubleshooting

**Problem**: Microsite links in index.html return 404
- **Solution**: Verify folder path matches exactly (case-sensitive on Linux/GitHub)
- **Check**: Ensure `index.html` exists in the microsite folder

**Problem**: Styling looks off or differs from index.html
- **Solution**: Ensure CSS custom properties match the root theme colors
- **Check**: Use the provided CSS template as a base

**Problem**: Navigation between sections not working
- **Solution**: Check that nav links use correct `href="#section-id"` format
- **Check**: Verify sections have matching `id` attributes

## Adding Microsite Content

### Adding Images

1. Save images to `microsites/[name]/images/`
2. Reference in HTML: `<img src="images/filename.png" alt="Description">`
3. Optimize images for web (use PNG or WebP for diagrams, JPEG for photos)

### Adding Videos

1. Save videos to `microsites/[name]/assets/`
2. Use HTML5 video element:
   ```html
   <video controls width="100%" style="max-width: 600px;">
       <source src="assets/video.mp4" type="video/mp4">
       Your browser does not support the video tag.
   </video>
   ```

### Adding PDFs

1. Save PDFs to `microsites/[name]/assets/`
2. Link to them: `<a href="assets/document.pdf" target="_blank">Download PDF</a>`
