/** @jest-environment node */
// Regression tests for the published TOF quiz and deep-linked slide decks.
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');
const root = path.join(__dirname, '..');
const slug = 'tetralogy-of-fallot-prenatal-diagnosis';
function load(relative, hash = '') {
  const dom = new JSDOM(fs.readFileSync(path.join(root, relative), 'utf8'), {
    url: `https://openmfm.org/${relative}${hash}`,
    runScripts: 'dangerously',
    beforeParse(window) { window.scrollTo = () => {}; }
  });
  return dom;
}
describe('TOF quiz learning flow', () => {
  let dom, doc;
  beforeEach(() => { dom = load(`decks/${slug}/quiz.html`); doc = dom.window.document; });
  afterEach(() => dom.window.close());
  function complete(answers) {
    for (const index of answers) {
      doc.querySelectorAll('#answers button')[index].click();
      doc.getElementById('nextQuestion').click();
    }
  }
  test('does not skip unanswered questions; locks the first response and explains each option', () => {
    doc.getElementById('nextQuestion').click();
    expect(doc.getElementById('questionNumber').textContent).toBe('Question 1 of 6');
    const buttons = doc.querySelectorAll('#answers button');
    buttons[0].click();
    buttons[1].click();
    expect(doc.getElementById('liveScore').textContent).toBe('Score: 0 / 1 answered');
    expect([...buttons].every(b => b.disabled)).toBe(true);
    expect(doc.getElementById('feedback').hidden).toBe(false);
    expect(doc.getElementById('feedback').textContent).toContain('Answer B is correct');
    expect(doc.querySelectorAll('#feedback details li')).toHaveLength(3);
    expect(doc.activeElement.id).toBe('feedback');
    expect(doc.querySelector('#feedback a[href="index.html#slide-2"]')).not.toBeNull();
  });
  test('scores six correct answers, supplies complete review, and resets on retake', () => {
    complete([1, 3, 0, 2, 1, 3]);
    expect(doc.getElementById('finalScore').textContent).toBe('6 / 6 · 100%');
    expect(doc.getElementById('quizView').hidden).toBe(true);
    expect(doc.getElementById('results').hidden).toBe(false);
    expect(doc.querySelectorAll('#review details')).toHaveLength(6);
    expect(doc.querySelectorAll('#review li')).toHaveLength(24);
    expect(doc.activeElement.id).toBe('resultTitle');
    doc.getElementById('retakeButton').click();
    expect(doc.getElementById('liveScore').textContent).toBe('Score: 0 / 0 answered');
    expect(doc.getElementById('quizProgress').value).toBe(0);
    expect(doc.getElementById('results').hidden).toBe(true);
    expect(doc.querySelectorAll('#review details')).toHaveLength(0);
    expect([...doc.querySelectorAll('#answers button')].every(b => !b.disabled)).toBe(true);
  });
  test.each([
    [[0, 0, 1, 0, 0, 0], '0 / 6 · 0%'],
    [[1, 3, 0, 0, 0, 0], '3 / 6 · 50%']
  ])('calculates score correctly for mixed and missed answers', (answers, result) => {
    complete(answers);
    expect(doc.getElementById('finalScore').textContent).toBe(result);
  });
});
describe.each([
  ['avsd-tof-physiology-patient', 16],
  [slug, 26]
])('TOF deck %s', (deck, count) => {
  test('opens a deep link with exactly one visible slide; follows hash changes', () => {
    const dom = load(`decks/${deck}/index.html`, '#slide-3');
    const doc = dom.window.document;
    expect(doc.querySelectorAll('.slide')).toHaveLength(count);
    expect(doc.querySelectorAll('.slide:not([hidden])')).toHaveLength(1);
    expect(doc.querySelector('.slide:not([hidden])').id).toBe('slide-3');
    dom.window.location.hash = '#slide-5';
    dom.window.dispatchEvent(new dom.window.HashChangeEvent('hashchange'));
    expect(doc.querySelector('.slide:not([hidden])').id).toBe('slide-5');
    const selector = doc.getElementById('slideSelect');
    selector.value = '0';
    selector.dispatchEvent(new dom.window.Event('change'));
    expect(doc.getElementById('prev').disabled).toBe(true);
    expect(dom.window.location.hash).toBe('#slide-1');
    dom.window.close();
  });
  test('navigation shortcuts do not intercept focused controls', () => {
    const dom = load(`decks/${deck}/index.html`);
    const doc = dom.window.document;
    const select = doc.getElementById('slideSelect');
    select.dispatchEvent(new dom.window.KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    expect(doc.querySelector('.slide:not([hidden])').id).toBe('slide-1');
    doc.body.dispatchEvent(new dom.window.KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    expect(doc.querySelector('.slide:not([hidden])').id).toBe('slide-2');
    dom.window.close();
  });
});
