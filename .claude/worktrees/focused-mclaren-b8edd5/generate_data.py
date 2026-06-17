import json
import os
from bs4 import BeautifulSoup

# Microsites defined manually
MICROSITES = [
    {
        "title": "Preeclampsia Screener",
        "href": "https://www.preeclampsia-screener.com/",
        "description": "Evidence-based risk calculator for aspirin prophylaxis.",
        "tags": ["Preeclampsia", "Risk Assessment", "Clinical Tool"]
    },
    {
        "title": "Vitamin K Deficiency Bleeding (VKDB)",
        "href": "microsites/vitamin-k-deficiency-bleeding/index.html",
        "description": "Dual-audience resource for parents and clinicians.",
        "tags": ["Newborn Care", "Prevention", "Clinician Toolkit"]
    },
    {
        "title": "GDM Screener",
        "href": "microsites/gdm-screener/index.html",
        "description": "Gestational diabetes screening timing per ACOG 2024.",
        "tags": ["Gestational Diabetes", "Screening Guidelines", "ACOG 2024"]
    },
    {
        "title": "HTN in Pregnancy Screener",
        "href": "microsites/htn-screener/index.html",
        "description": "Hypertension classification tool per ACOG PB #222.",
        "tags": ["Hypertension", "Diagnosis", "ACOG PB 222"]
    },
    {
        "title": "Fetal Growth Biometry Calculator",
        "href": "microsites/fetal-growth-calculator/index.html",
        "description": "INTERGROWTH-21st, Hadlock, and WHO standards.",
        "tags": ["Fetal Growth", "Biometry Calculator", "Sonographer Education"]
    },
    {
        "title": "FGRManager",
        "href": "microsites/FGRManager/landing.html",
        "description": "FGR surveillance and delivery timing per SMFM #52.",
        "tags": ["FGR", "Doppler Surveillance", "SMFM #52"]
    }
]

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Only parse the main presentations container, not microsites
presentations_container = soup.find('div', class_='presentations', id=lambda x: x != 'microsites-container')
cards = presentations_container.find_all('div', class_='card') if presentations_container else []

presentations = []
for card in cards:
    title_el = card.find(['h2', 'h3', 'strong'])
    title = title_el.get_text(strip=True) if title_el else ''

    link_el = card.find('a', class_='btn')
    href = link_el.get('href', '') if link_el else ''

    tag_els = card.find_all('span', class_='tag')
    tags = [t.get_text(strip=True) for t in tag_els if t.get_text(strip=True) not in ('🌐 Microsite', '🚧 In Development')]

    # Skip microsite cards and placeholder cards
    tag_texts = [t.get_text(strip=True) for t in tag_els]
    if '🌐 Microsite' in tag_texts or '🚧 In Development' in tag_texts:
        continue

    if title and href:
        presentations.append({'title': title, 'href': href, 'tags': tags})

output_data = {
    "presentations": presentations,
    "microsites": MICROSITES
}

os.makedirs('landing-page/data', exist_ok=True)

with open('landing-page/data/presentations.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=2)

print(f"Successfully generated landing-page/data/presentations.json")
print(f"{len(presentations)} presentations and {len(MICROSITES)} microsites saved.")
