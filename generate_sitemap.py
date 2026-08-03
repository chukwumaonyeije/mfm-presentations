import json
import os
from datetime import datetime

BASE_URL = "https://openmfm.org"

with open('landing-page/data/presentations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

presentations = data['presentations']
microsites = data['microsites']

urls = []

# Main pages
urls.append(('/', '1.0'))
urls.append(('/library', '0.9'))

# Presentations
for p in presentations:
    urls.append((f"/{p['href']}", '0.8'))

# Microsites (relative URLs only)
for m in microsites:
    if not m['href'].startswith('http'):
        urls.append((f"/{m['href']}", '0.7'))

today = datetime.now().strftime('%Y-%m-%d')

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for url, priority in urls:
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{BASE_URL}{url}</loc>')
    xml_lines.append(f'    <lastmod>{today}</lastmod>')
    xml_lines.append(f'    <changefreq>monthly</changefreq>')
    xml_lines.append(f'    <priority>{priority}</priority>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

xml_content = '\n'.join(xml_lines)

os.makedirs('landing-page/public', exist_ok=True)
output_path = 'landing-page/public/sitemap.xml'
with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(xml_content)
print(f"Generated {output_path} with {len(urls)} URLs.")

# Also keep root sitemap.xml in sync (canonical openmfm.org URLs)
root_output_path = 'sitemap.xml'
with open(root_output_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(xml_content)
print(f"Generated {root_output_path} with {len(urls)} URLs.")
