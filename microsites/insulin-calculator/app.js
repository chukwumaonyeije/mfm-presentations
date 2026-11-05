'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const form = $('calculator-form');
  let summary = '';
  let revision = 0;
  const fmt = n => Number.isInteger(n) ? String(n) : n.toFixed(1);
  function invalidate() {
    revision++;
    summary = '';
    $('results').hidden = true;
    $('copy-fallback').hidden = true;
    $('error').hidden = true;
    $('status').textContent = 'Inputs changed. Calculate again to review an updated estimate.';
  }
  form.addEventListener('input', invalidate);
  form.addEventListener('change', invalidate);
  $('unit').addEventListener('change', () => {
    $('weight').value = '';
    $('status').textContent = 'Weight unit changed. Enter the weight in the selected unit, then recalculate.';
  });
  form.addEventListener('reset', () => { invalidate(); $('status').textContent = 'Enter the parameters to see the estimate and dose allocation.'; });
  form.addEventListener('submit', event => {
    event.preventDefault();
    invalidate();
    try {
      const result = InsulinCalculator.calculate(Object.fromEntries(new FormData(form)));
      if (!$('scope').checked) throw new Error('Confirm the clinician scope before calculating.');
      const context = `${result.weeks} weeks + ${result.days} days · trimester ${result.trimester} · current weight ${result.weight} ${result.unit} (${result.kg.toFixed(2)} kg)`;
      const formula = `${result.kg.toFixed(2)} kg × ${result.factor} units/kg/day = ${result.rawTotal.toFixed(2)} units/day before dose rounding → ${fmt(result.total)} units/day. Increment: ${result.increment} unit(s). Full precision is used internally.`;
      $('context').textContent = context;
      $('formula').textContent = formula;
      for (const key of ['total', 'basal', 'bolus']) $(key).textContent = fmt(result[key]);
      ['breakfast', 'lunch', 'dinner'].forEach((key, i) => $(key).textContent = fmt(result.meals[i]));
      summary = `OpenMFM pregnancy insulin initiation estimate | ${result.version}\nCLINICIAN DECISION SUPPORT — reviewed by Chukwuma Onyeije, MD, November 4, 2026; not a prescription.\n${context}\n${formula}\nBasal total per day: ${fmt(result.basal)} units\nIllustrative meal allocation: breakfast ${fmt(result.meals[0])}, lunch ${fmt(result.meals[1])}, dinner ${fmt(result.meals[2])} units\nMealtime total: ${fmt(result.bolus)} units\nModel: 0.7/0.8/0.9 units/kg by trimester; current weight; approximately 50% basal, remaining dose approximately equal across meals.\nScope: clinician-reviewed full starting regimen in insulin-naive GDM. Not for existing insulin regimens, type 1/type 2 diabetes, correction doses, acute illness, intrapartum or postpartum care.\nChoose insulin preparation, timing, meal doses, monitoring and follow-up individually.\nSources: ADA 2026 https://doi.org/10.2337/dc26-S015 ; MEMS Practical Guide to Insulin Therapy, 2024. Source check: 2026-11-04.`;
      $('results').hidden = false;
      $('status').textContent = 'Estimate updated. Review the allocation and assumptions below.';
    } catch (error) {
      $('error').textContent = error.message;
      $('error').hidden = false;
      $('status').textContent = 'No current estimate. Correct the inputs and calculate again.';
    }
  });
  $('print').addEventListener('click', () => { if (summary) window.print(); });
  $('copy').addEventListener('click', async () => {
    if (!summary) return;
    const text = summary;
    const currentRevision = revision;
    try {
      await navigator.clipboard.writeText(text);
      if (currentRevision === revision) $('status').textContent = 'Review summary copied, including assumptions and clinical review status.';
    } catch {
      if (currentRevision !== revision) return;
      $('copy-fallback').value = text;
      $('copy-fallback').hidden = false;
      $('copy-fallback').focus();
      $('copy-fallback').select();
      $('status').textContent = 'Automatic copy is unavailable. Copy the selected summary below.';
    }
  });
})();
