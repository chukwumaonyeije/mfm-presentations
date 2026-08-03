const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync(__dirname + '/index.html', 'utf8');
const failures = [];
const warnings = [];

const sections = [...html.matchAll(/<section class="slide(?: active)?"[\s\S]*?<\/section>/g)].map(m => m[0]);
if (sections.length !== 20) failures.push(`Expected 20 slides; found ${sections.length}`);

const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(m => m[1]);
const duplicateIds = [...new Set(ids.filter((id, i) => ids.indexOf(id) !== i))];
if (duplicateIds.length) failures.push(`Duplicate IDs: ${duplicateIds.join(', ')}`);

const hrefTargets = [...html.matchAll(/href="#([^"]+)"/g)].map(m => m[1]);
const missingTargets = hrefTargets.filter(id => !ids.includes(id));
if (missingTargets.length) failures.push(`Missing internal targets: ${missingTargets.join(', ')}`);

const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) failures.push('Inline script not found');
else {
  try { new vm.Script(scriptMatch[1]); }
  catch (error) { failures.push(`JavaScript syntax: ${error.message}`); }
}

const visibleText = source => source
  .replace(/<[^>]*data-no-count[^>]*>[\s\S]*?<\/[^>]+>/g, ' ')
  .replace(/<svg[\s\S]*?<\/svg>/g, ' ')
  .replace(/<[^>]+>/g, ' ')
  .replace(/&(?:amp|lt|gt|quot|#\d+);/g, ' ')
  .replace(/\s+/g, ' ')
  .trim();

sections.forEach((section, i) => {
  const title = (section.match(/data-title="([^"]+)"/) || [,'Untitled'])[1];
  const text = visibleText(section);
  const words = text ? text.split(/\s+/).length : 0;
  if (words > 30) warnings.push(`Slide ${i + 1} (${title}) has ${words} visible words`);
  if (!/aria-labelledby="[^"]+"/.test(section)) failures.push(`Slide ${i + 1} lacks aria-labelledby`);
});

const requiredTokens = ['ArrowRight', 'touchstart', 'location.hash', '@media print', 'prefers-reduced-motion', 'data-open-refs'];
for (const token of requiredTokens) if (!html.includes(token)) failures.push(`Missing required feature token: ${token}`);

const externalLinks = [...html.matchAll(/href="(https:\/\/[^"#]+)"/g)].map(m => m[1]);
if (externalLinks.length < 12) failures.push(`Expected at least 12 source links; found ${externalLinks.length}`);

console.log(JSON.stringify({
  slides: sections.length,
  ids: ids.length,
  externalLinks: externalLinks.length,
  failures,
  warnings
}, null, 2));

process.exitCode = failures.length ? 1 : 0;
