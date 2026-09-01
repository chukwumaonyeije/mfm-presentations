const fs = require('fs');
const path = require('path');
const { TextEncoder, TextDecoder } = require('util');

global.TextEncoder = TextEncoder;
global.TextDecoder = TextDecoder;

const { JSDOM } = require('jsdom');

const html = fs.readFileSync(
  path.join(__dirname, '..', 'decks', 'pregnancy-after-recurrent-loss', 'index.html'),
  'utf8'
);

function loadDeck(hash = '') {
  return new JSDOM(html, {
    runScripts: 'dangerously',
    url: `https://openmfm.org/decks/pregnancy-after-recurrent-loss/index.html${hash}`,
  });
}

describe('Pregnancy After Recurrent Loss patient deck', () => {
  test('renders the approved 17-slide architecture', () => {
    const dom = loadDeck();
    const { document } = dom.window;

    expect(document.querySelectorAll('.slide')).toHaveLength(17);
    expect(document.getElementById('slide-1').classList.contains('active')).toBe(true);
    expect(document.getElementById('tot').textContent).toBe('17');
    expect(document.querySelectorAll('.outline-link')).toHaveLength(17);
  });

  test('supports button, keyboard, and hash navigation', () => {
    const dom = loadDeck('#slide-3');
    const { document } = dom.window;

    expect(document.getElementById('slide-3').classList.contains('active')).toBe(true);
    document.getElementById('nextBtn').click();
    expect(document.getElementById('slide-4').classList.contains('active')).toBe(true);

    document.dispatchEvent(new dom.window.KeyboardEvent('keydown', { key: 'End' }));
    expect(document.getElementById('slide-17').classList.contains('active')).toBe(true);
    expect(document.getElementById('nextBtn').disabled).toBe(true);
  });

  test('includes required patient safety, privacy, and evidence content', () => {
    const dom = loadDeck();
    const { document } = dom.window;
    const body = document.body.textContent;

    expect(body).toContain('Questions to ask your MFM specialist');
    expect(body).toContain('Educational disclaimer');
    expect(body).toContain('No patient information is collected');
    expect(body).toContain('Recurrent loss alone is not a reason to self-start');
    expect(body).toContain('Unexplained RPL alone does not automatically require every test or early delivery');
    expect(document.querySelectorAll('.panel-ref').length).toBeGreaterThanOrEqual(8);
  });

  test('links to the companion history builder', () => {
    const dom = loadDeck();
    const links = [...dom.window.document.querySelectorAll('a')].map(a => a.getAttribute('href'));

    expect(links).toContain('../../microsites/recurrent-pregnancy-loss-history/index.html');
  });
});
