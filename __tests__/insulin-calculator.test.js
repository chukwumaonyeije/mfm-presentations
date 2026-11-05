const fs = require('fs');
const path = require('path');
const { calculate } = require('../microsites/insulin-calculator/calculator');
const base = { weeks: 36, days: 0, weight: 195, unit: 'lb', increment: 1 };

test('original screenshot example, independently calculated and reconciled', () => {
  const r = calculate(base);
  expect(r.kg).toBeCloseTo(88.45051215, 8);
  expect(r.rawTotal).toBeCloseTo(79.605460935, 8);
  expect(r.total).toBe(80);
  expect(r.basal).toBe(40);
  expect(r.bolus).toBe(40);
  expect(r.meals).toEqual([14, 13, 13]);
  const half = calculate({ ...base, increment: 0.5 });
  expect(half.total).toBe(79.5);
  expect(half.basal).toBe(40);
  expect(half.meals).toEqual([13.5, 13, 13]);
});

test.each([[13,6,0.7],[14,0,0.8],[27,6,0.8],[28,0,0.9],[42,0,0.9]])('gestational boundary %iw%id uses %f', (weeks,days,factor) => {
  expect(calculate({ ...base, weeks, days }).factor).toBe(factor);
});

test.each([
  {weight:''},{weight:' '},{weight:-195},{weight:Infinity},{weight:'abc'},
  {weight:29.99,unit:'kg'},{weight:200.01,unit:'kg'},
  {weeks:0},{weeks:43},{weeks:13.6},{weeks:42,days:1},
  {days:7},{days:-1},{days:0.5},{days:''},{unit:'stones'},{increment:0.1}
])('reject invalid input %j', change => expect(() => calculate({...base,...change})).toThrow());

test('unit conversion produces identical doses', () => {
  const pounds = calculate(base);
  const kg = calculate({...base, weight:88.45051215, unit:'kg'});
  expect(kg.total).toBe(pounds.total);
  expect(kg.meals).toEqual(pounds.meals);
});

test('decimal floating point does not round exact halfway values downward', () => {
  expect(calculate({...base,weeks:12,weight:45,unit:'kg'}).total).toBe(32);
  expect(calculate({...base,weeks:12,weight:37.5,unit:'kg',increment:0.5}).total).toBe(26.5);
});

test('all weight bands retain exact dose sums and device increments', () => {
  for (const weeks of [1,14,28,42]) for (const increment of [0.5,1]) {
    for (let weight = 30; weight <= 200; weight += 0.25) {
      const r = calculate({...base,weeks,weight,unit:'kg',increment});
      expect(r.meals.reduce((a,b)=>a+b,0)).toBe(r.bolus);
      expect(r.basal+r.bolus).toBe(r.total);
      for (const dose of [r.basal,...r.meals]) {
        expect(Number.isInteger(dose/increment)).toBe(true);
        expect(dose).toBeGreaterThan(0);
      }
      expect(Math.abs(r.total-r.rawTotal)).toBeLessThanOrEqual(increment/2+1e-10);
    }
  }
});

describe('user interaction', () => {
  const dir = path.join(__dirname,'../microsites/insulin-calculator');
  const $ = id => document.getElementById(id);
  const submit = () => $('calculator-form').dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));
  beforeEach(() => {
    document.documentElement.innerHTML = fs.readFileSync(path.join(dir,'index.html'),'utf8');
    global.InsulinCalculator = {calculate};
    window.eval(fs.readFileSync(path.join(dir,'app.js'),'utf8'));
    $('weeks').value='36'; $('days').value='0'; $('weight').value='195'; $('scope').checked=true;
  });
  test('shows expected values and invalidates on edits', () => {
    submit(); expect($('results').hidden).toBe(false); expect($('total').textContent).toBe('80');
    $('weight').value='180'; $('weight').dispatchEvent(new Event('input',{bubbles:true}));
    expect($('results').hidden).toBe(true);
    submit(); expect($('results').hidden).toBe(false); expect($('total').textContent).toBe('73');
  });
  test('invalid submissions cannot leave an old result visible', () => {
    submit(); $('weeks').value='-2'; submit();
    expect($('results').hidden).toBe(true); expect($('error').hidden).toBe(false);
  });
  test('scope confirmation is required', () => {
    $('scope').checked=false; submit();
    expect($('results').hidden).toBe(true); expect($('error').textContent).toMatch(/scope/);
  });
  test('unit changes clear weight and stale outputs', () => {
    submit(); $('unit').value='kg'; $('unit').dispatchEvent(new Event('change',{bubbles:true}));
    expect($('weight').value).toBe(''); expect($('results').hidden).toBe(true);
  });
  test('reset clears results', () => {
    submit(); $('calculator-form').reset(); expect($('results').hidden).toBe(true);
  });
  test('copy fallback includes clinical review status and clinical context', async () => {
    submit(); $('copy').click(); await Promise.resolve();
    expect($('copy-fallback').hidden).toBe(false);
    expect($('copy-fallback').value).toMatch(/reviewed by Chukwuma Onyeije/);
    expect($('copy-fallback').value).toMatch(/36 weeks/);
    expect($('copy-fallback').value).toMatch(/not a prescription/);
  });
});
