# MFM Presentations & Clinical Consultations

A repository of high-quality, evidence-based educational presentations for Maternal-Fetal Medicine (MFM) clinicians and patients. These presentations are designed for teaching, consultation, and shared decision-making in obstetric care.

## 🎯 Purpose

This repository serves as a curated collection of clinical presentations covering complex MFM topics, including:
- Fetal growth restriction (FGR) and abnormal Doppler studies
- Preeclampsia management
- IUGR surveillance and delivery timing
- Evidence-based approaches to high-risk obstetric conditions
- Interactive microsites with dual-audience content (patients and clinicians)

## 🌐 Interactive Microsites

Comprehensive, multi-page educational resources designed for both patients and clinicians, featuring interactive content, documentation templates, and evidence-based counseling tools.

### Vitamin K Deficiency Bleeding (VKDB)
**Path:** `microsites/vitamin-k-deficiency-bleeding/`

**Summary:** Dual-audience microsite covering neonatal Vitamin K prophylaxis with separate interfaces for parents and clinicians.

**Patient-Facing Content:**
- Why newborns need Vitamin K
- Safety information and what to expect
- Common myths and evidence-based responses
- FAQ and printable handouts

**Clinician Toolkit:**
- 60-second counseling script
- Evidence framing for common social media claims
- Documentation templates for informed consent/refusal
- Safety-netting and follow-up guidance

**Target Audience:** Parents, pediatricians, family medicine, OB providers, nursing staff

## 📚 Available Presentations

### 1. FGR + Absent End-Diastolic Flow at 35 Weeks
**Path:** `decks/fgr-ua-aedv-35w/`

**Summary:** Clinical approach to late-preterm FGR with absent umbilical artery end-diastolic velocity (AEDV) - the placental insufficiency phenotype.

**Key Topics:**
- Definition and diagnosis of FGR with AEDV
- Pathophysiology of placental insufficiency
- Delivery timing at 35 weeks
- Counseling and management strategies

**Target Audience:** OB residents, fellows, MFM specialists

### 2. IUGR and Doppler
**Path:** `decks/iugr-and-doppler/`

**Summary:** Comprehensive overview of intrauterine growth restriction and the role of Doppler velocimetry in diagnosis and management.

### 3. Preeclampsia
**Path:** `decks/preeclampsia/`

**Summary:** Evidence-based management of preeclampsia in pregnancy.

## 🎨 Design Philosophy

These presentations follow a **high-contrast, minimal-text** design:
- One teaching point per slide
- Dark mode for reduced eye strain during long presentations
- Clean, modern UI with accessible color contrast
- Keyboard-driven navigation for smooth presenting
- Print-friendly CSS for handouts

## 🚀 Usage

### Main Landing Page

Start at `index.html` to browse all presentations and microsites:
- Search functionality to find topics by keyword
- Categorized presentations with badges (video, infographic, PDF available)
- Direct links to interactive microsites
- Pagination for easy browsing

### Viewing Presentations

1. **Local viewing:**
   ```bash
   # Open the main landing page
   open index.html
   
   # Or open any specific presentation
   open decks/fgr-ua-aedv-35w/index.html
   
   # Or open a microsite
   open microsites/vitamin-k-deficiency-bleeding/index.html
   ```

2. **Serve with a local server:**
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Then visit http://localhost:8000/
   ```

### Navigation

- **Main page → Presentations:** Click any presentation card
- **Main page → Microsites:** Scroll to "Interactive Microsites" section
- **Microsite → Main page:** Click "← All Presentations" in the navigation bar
- **Patient ↔ Clinician views:** Use navigation links within microsites

### Navigation Controls

- **Next slide:** `→`, `Space`, `PageDown`, or click right side
- **Previous slide:** `←`, `PageUp`, or click left side
- **First slide:** `Home`
- **Last slide:** `End`

### Presenting Tips

- Use full-screen mode (F11) for clean presentation
- Practice keyboard navigation before presenting
- Each slide is designed to be discussed for 1-3 minutes
- Print feature available via browser print dialog

## 🧪 Testing

This repository includes a comprehensive test suite for the presentation navigation system.

### Running Tests

```bash
# Install dependencies
npm install

# Run tests
npm test

# Run tests in watch mode
npm run test:watch
```

### Test Coverage

The test suite validates:
- ✅ Slide navigation (show, next, prev)
- ✅ Keyboard controls (Home, End, arrows)
- ✅ Progress bar updates
- ✅ Accessibility attributes (aria-hidden)
- ✅ Edge cases (empty/single slide presentations)

See `__tests__/README.md` for detailed testing documentation.

## 🏗️ Project Structure

```
mfm-presentations/
├── index.html                      # Main landing page with search and navigation
├── decks/                          # Individual presentation decks (70+ topics)
│   ├── fgr-ua-aedv-35w/           # FGR with AEDV at 35 weeks
│   ├── iugr-and-doppler/          # IUGR and Doppler overview
│   ├── preeclampsia/              # Preeclampsia management
│   └── ...                        # Many more clinical presentations
├── microsites/                     # Interactive multi-page microsites
│   └── vitamin-k-deficiency-bleeding/
│       ├── index.html             # Patient-facing content
│       ├── clinicians.html        # Clinician toolkit
│       └── assets/                # Microsite-specific styles
├── shared/                         # Shared assets and utilities
│   ├── css/                       # Shared stylesheets
│   ├── images/                    # Shared images
│   ├── js/                        # Shared JavaScript
│   └── presentation.js            # Core presentation logic
├── __tests__/                      # Test suite
│   ├── presentation.test.js       # Unit tests
│   └── README.md                  # Testing documentation
├── package.json                    # Dependencies and scripts
├── jest.config.js                 # Test configuration
└── README.md                       # This file
```

## 🔧 Technical Details

- **Framework:** Pure HTML/CSS/JavaScript (no build step required)
- **Testing:** Jest with jsdom
- **Styling:** Custom CSS with CSS variables for theming
- **Accessibility:** ARIA attributes, keyboard navigation, semantic HTML
- **Responsive:** Adapts to different screen sizes

## 📖 Educational Use

### For Educators

These presentations are designed for:
- Grand rounds and case conferences
- Resident and fellow teaching sessions
- Journal clubs and evidence reviews
- Patient consultation aids

### For Learners

Each presentation:
- Cites current evidence and guidelines (ACOG, SMFM)
- Breaks complex topics into digestible concepts
- Emphasizes practical clinical decision-making
- Includes "one teaching point per slide" for retention

### For Patients

Presentation style allows for:
- Visual aids during consultation
- Shared decision-making discussions
- Print-outs for patient education
- Clear explanation of complex medical concepts

## 🤝 Contributing

This is an educational resource. If you'd like to:
- Report an error or suggest improvements
- Add a new presentation deck
- Update content based on new guidelines

Please open an issue or submit a pull request.

## ⚖️ Disclaimer

**Important:** These presentations are educational tools and do not constitute medical advice. Clinical decisions should be individualized based on:
- Current evidence and guidelines
- Local protocols and resources
- Individual patient circumstances
- Provider clinical judgment

Always consult current ACOG, SMFM, and institutional guidelines for patient care.

## 📝 License

These educational materials are provided for clinical education and consultation purposes.

## 👨‍⚕️ Author

Created by a Maternal-Fetal Medicine specialist for education and clinical consultation.

---

**For questions or feedback**, please open an issue on this repository.
