/**
 * generate-sitemap.js
 * Reads index.html and extracts all presentation/microsite URLs,
 * then writes sitemap.xml to the project root.
 *
 * Usage:  node scripts/generate-sitemap.js
 * Or add to package.json scripts: "sitemap": "node scripts/generate-sitemap.js"
 *
 * UPDATE BASE_URL when you move to Vercel or a custom domain.
 */

const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://chukwumaonyeije.github.io/mfm-presentations';
const ROOT = path.join(__dirname, '..');
const indexHtml = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');

// Extract all href attributes pointing to decks/ or microsites/ HTML files
const hrefRegex = /href="((decks|microsites)\/[^"]+\.html)"/g;
const urls = new Set();
urls.add(''); // root URL

let match;
while ((match = hrefRegex.exec(indexHtml)) !== null) {
  // Skip external URLs (descript.com videos, etc.) and infographic images
  const href = match[1];
  if (!href.startsWith('http') && href.endsWith('.html')) {
    urls.add('/' + href);
  }
}

const today = new Date().toISOString().split('T')[0];

const entries = Array.from(urls)
  .sort()
  .map(url => {
    const isRoot = url === '';
    const priority = isRoot ? '1.0' : url.includes('microsites') ? '0.9' : '0.8';
    return `  <url>
    <loc>${BASE_URL}${isRoot ? '/' : url}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>${priority}</priority>
  </url>`;
  })
  .join('\n');

const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${entries}
</urlset>
`;

fs.writeFileSync(path.join(ROOT, 'sitemap.xml'), sitemap);
console.log(`✅  sitemap.xml generated with ${urls.size} URLs`);
console.log(`    Base URL: ${BASE_URL}`);
console.log(`    Tip: Update BASE_URL in this script when you move to Vercel/custom domain.`);
