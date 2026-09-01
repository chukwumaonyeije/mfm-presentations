const fs = require('fs');
const path = require('path');
const { TextEncoder, TextDecoder } = require('util');

global.TextEncoder = TextEncoder;
global.TextDecoder = TextDecoder;

const { JSDOM } = require('jsdom');

const html = fs.readFileSync(
  path.join(__dirname, '..', 'microsites', 'recurrent-pregnancy-loss-history', 'index.html'),
  'utf8'
);

function loadTool() {
  return new JSDOM(html, {
    runScripts: 'dangerously',
    url: 'https://openmfm.org/microsites/recurrent-pregnancy-loss-history/index.html',
    beforeParse(window) {
      window.scrollTo = jest.fn();
      window.confirm = jest.fn(() => true);
    },
  });
}

describe('Pregnancy After Loss Visit History Builder', () => {
  test('starts with two editable loss records and can add another', () => {
    const dom = loadTool();
    const { document } = dom.window;

    expect(document.querySelectorAll('.loss')).toHaveLength(2);
    document.getElementById('addLoss').click();
    expect(document.querySelectorAll('.loss')).toHaveLength(3);
    expect(document.querySelectorAll('.lossnum')[2].textContent).toBe('3');
  });

  test('builds a patient-entered summary and relevant discussion prompts', () => {
    const dom = loadTool();
    const { document } = dom.window;

    document.getElementById('name').value = 'AB';
    const firstLoss = document.querySelector('.loss');
    firstLoss.querySelector('[data-k="ga"]').value = '18 weeks';
    firstLoss.querySelector('[data-k="pattern"]').value = 'Painless cervical opening';
    document.getElementById('symptoms').value = 'Light bleeding today';

    for (let i = 0; i < 4; i += 1) document.getElementById('nextBtn').click();

    expect(document.querySelector('[data-step="5"]').classList.contains('active')).toBe(true);
    expect(document.getElementById('summary').textContent).toContain('Name/initials: AB');
    expect(document.getElementById('summary').textContent).toContain('Gestational age: 18 weeks');
    expect(document.getElementById('flags').textContent).toContain('cervical-insufficiency');
    expect(document.getElementById('flags').textContent).toContain('current symptoms');
  });

  test('contains explicit privacy and non-diagnostic language', () => {
    const dom = loadTool();
    const text = dom.window.document.body.textContent;

    expect(text).toContain('Nothing is sent to OpenMFM');
    expect(text).toContain('not a diagnosis');
    expect(text).toContain('does not store or transmit your answers');
  });
});
