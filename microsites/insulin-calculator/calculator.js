(function (root) {
  'use strict';
  const VERSION = '2.0.0';
  function number(value, label) {
    if (value === '' || value === null || value === undefined || typeof value === 'boolean' || (typeof value === 'string' && !value.trim())) throw new Error(`Enter ${label}.`);
    const n = Number(value);
    if (!Number.isFinite(n)) throw new Error(`Enter a finite number for ${label}.`);
    return n;
  }
  function calculate(input) {
    const weeks = number(input.weeks, 'completed weeks');
    const days = number(input.days, 'additional days');
    if (!Number.isInteger(weeks) || !Number.isInteger(days) || weeks < 1 || weeks > 42 || days < 0 || days > 6 || (weeks === 42 && days !== 0)) throw new Error('Use whole weeks and days between 1 week 0 days and 42 weeks 0 days.');
    const weight = number(input.weight, 'current weight');
    if (!['lb', 'kg'].includes(input.unit)) throw new Error('Select pounds or kilograms.');
    const kg = input.unit === 'lb' ? weight * 0.45359237 : weight;
    if (kg < 30 || kg > 200) throw new Error('This tool supports current weights of 30–200 kg (about 66.14–440.92 lb). Use an individualized calculation outside this range.');
    const increment = number(input.increment, 'dose increment');
    if (![0.5, 1].includes(increment)) throw new Error('Select a 0.5-unit or 1-unit increment.');
    const trimester = weeks < 14 ? 1 : weeks < 28 ? 2 : 3;
    const factor = [0, 0.7, 0.8, 0.9][trimester];
    const rawTotal = kg * factor;
    // Allocate integer dose increments so every displayed component sums exactly.
    const totalSteps = Math.round(rawTotal / increment + 1e-10);
    const basalSteps = Math.round(totalSteps / 2);
    const bolusSteps = totalSteps - basalSteps;
    const mealBase = Math.floor(bolusSteps / 3);
    const remainder = bolusSteps % 3;
    const meals = [0, 1, 2].map(i => (mealBase + (i < remainder ? 1 : 0)) * increment);
    return { version: VERSION, weeks, days, weight, unit: input.unit, kg, trimester, factor, increment, rawTotal,
      total: totalSteps * increment, basal: basalSteps * increment, bolus: bolusSteps * increment, meals };
  }
  const api = { calculate, VERSION };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.InsulinCalculator = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
