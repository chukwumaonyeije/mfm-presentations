# Vitamin K Deficiency Bleeding Microsite

## Overview

This microsite provides comprehensive, evidence-based educational content on Vitamin K Deficiency Bleeding (VKDB) for both parents and healthcare professionals. It features:

- **Patient-friendly content** explaining what VKDB is, why the vitamin K shot matters, and addressing common myths
- **Clinician resources** including pathophysiology, risk stratification, diagnostic criteria, and management protocols
- **Dual-view toggle** allowing seamless switching between patient and clinician perspectives
- **Interactive accordions** for myth-debunking and FAQ sections
- **Print-optimized layouts** for both digital and physical distribution

## Content Structure

### Patient-Facing Sections
1. **Hero Section** - Clear, compelling introduction to VKDB and the importance of prophylaxis
2. **Why Newborns Need Vitamin K** - Age-appropriate explanation of vitamin K physiology and risk factors
3. **Safety and What to Expect** - Practical information about the injection, aftercare, and alternatives
4. **Myths vs Facts** - Expandable accordion addressing common misconceptions with evidence-based responses
5. **FAQ** - Common parent questions about VKDB, warning signs, and information evaluation
6. **Printable Handout** - One-page summary for distribution in clinics and classes
7. **Resources & References** - Professional guidelines and citations

### Clinician-Only Sections (Accessible via Toggle)
- **Pathophysiology & Risk Stratification** - Vitamin K-dependent factors, neonatal vulnerability, clinical risk factors
- **Administration & Dosing** - ACOG & AAP recommendations, timing, routes, effectiveness data
- **Clinician FAQ** - Guidance on parental hesitancy, incidence/mortality data, diagnostic approach, management protocols
- **Key references** - Evidence base including AAP, ACOG, WHO, CDC guidelines and peer-reviewed literature

## Features

- **Dual-View Toggle**: Switch between patient-friendly and clinician-specific content with a single click
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Interactive Accordions**: Expandable myth/fact pairs and FAQ sections with keyboard accessibility
- **Persistent Preferences**: View preference (patient/clinician) saved in browser localStorage
- **Print-Optimized**: Generates clean print layouts for both digital and physical distribution
- **Consistent Styling**: Medical-grade UI with high contrast and accessibility focus
- **No External Dependencies**: Fully self-contained (fonts via Google Fonts CDN only)
- **Semantic HTML**: Proper heading hierarchy, ARIA labels, and accessibility support

## Technical Details

### Files

- `index.html` - Main content file with semantic HTML structure
- `css/style.css` - Theme-consistent styling with dark background and medical-grade readability
- `js/script.js` - Navigation logic with keyboard support
- `images/` - Directory for medical diagrams and illustrations
- `assets/` - Directory for videos or PDF documents

### Color Scheme

The microsite uses the standard MFM presentation theme:
- Background: `#1a1a1a` (dark)
- Foreground: `#e0e0e0` (light gray)
- Primary accent: `#00d4ff` (cyan)
- Secondary accent: `#ff6b9d` (pink)
- Positive: `#00ff88` (green)
- Warning: `#ffb800` (yellow)

### Navigation

Click on any section title in the top navigation menu to jump to that section. You can also use:
- **Right arrow key**: Next section
- **Left arrow key**: Previous section
- **Home key**: First section
- **End key**: Last section

## Medical Content Guidelines

### Evidence Base

Content is based on current recommendations from:
- American Academy of Pediatrics (AAP)
- American College of Obstetricians and Gynecologists (ACOG)
- World Health Organization (WHO)
- Centers for Disease Control and Prevention (CDC)

### Accuracy

Medical information has been reviewed for accuracy against current clinical practice guidelines. However, this is educational content and should not replace consultation with current clinical guidelines or institutional protocols.

## Usage

### Local Testing

1. Open `index.html` in any modern web browser (Chrome, Firefox, Safari, Edge)
2. No server or build tools required
3. Test navigation: Click menu items, use keyboard shortcuts
4. Test responsiveness: Resize browser window or use mobile emulation

### Deployment

The microsite deploys automatically as part of the mfm-presentations GitHub Pages workflow:
1. All files in this directory are included in the deployment
2. No special build steps needed
3. Accessible at: `https://chukwumaonyeije.github.io/mfm-presentations/microsites/vitamin-k-deficiency-bleeding/`

## Customization

### Adding Images

1. Save images to the `images/` directory
2. Reference in HTML: `<img src="images/filename.png" alt="Description">`
3. Examples: coagulation cascades, timeline diagrams, comparison tables

### Adding Videos

1. Save videos to the `assets/` directory
2. Use HTML5 video element:
   ```html
   <video controls width="100%" style="max-width: 600px;">
       <source src="assets/video.mp4" type="video/mp4">
       Your browser does not support the video tag.
   </video>
   ```

### Adding PDFs

1. Save PDFs to the `assets/` directory
2. Link to them:
   ```html
   <a href="assets/document.pdf" target="_blank">Download Handout</a>
   ```

## Accessibility

- Semantic HTML structure with proper heading hierarchy
- Sufficient color contrast for readability
- Keyboard navigation support for all interactive elements
- Responsive design for various screen sizes

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Future Enhancements

Potential improvements for future versions:
- Interactive coagulation cascade diagrams
- Video demonstrations of vitamin K prophylaxis techniques
- Interactive case studies with clinical decision-making
- PDF handout generation
- Comparison charts for different prophylaxis regimens

## Author

Created as part of the MFM Presentations GitHub project - an educational resource for maternal-fetal medicine providers.

## License

This content is part of the mfm-presentations repository. See the main repository for licensing information.

## Questions or Corrections

If you notice any inaccuracies or have suggestions for improvement, please open an issue or pull request in the main mfm-presentations repository.
