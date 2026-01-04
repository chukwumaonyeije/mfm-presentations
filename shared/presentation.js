/**
 * Presentation slide navigation system
 * Extracted for testing purposes
 */

function createPresentation(slideSelector = 'section.slide') {
  const slides = Array.from(document.querySelectorAll(slideSelector));
  const tot = slides.length;
  const idxEl = document.getElementById('idx');
  const totEl = document.getElementById('tot');
  const bar = document.getElementById('bar');
  
  if (totEl) totEl.textContent = tot;

  let i = 0;

  function show(n) {
    if (tot === 0) return; // Guard against empty presentation
    i = Math.max(0, Math.min(tot - 1, n));
    slides.forEach((s, k) => s.classList.toggle('active', k === i));
    if (idxEl) idxEl.textContent = (i + 1);
    if (bar) bar.style.width = ((i + 1) / tot * 100).toFixed(1) + '%';
    // Improve accessibility
    if (slides[i]) slides[i].setAttribute('aria-hidden', 'false');
    slides.forEach((s, k) => { if (k !== i) s.setAttribute('aria-hidden', 'true'); });
  }

  function next() { show(i + 1); }
  function prev() { show(i - 1); }
  function getCurrentIndex() { return i; }
  function getTotalSlides() { return tot; }

  return {
    show,
    next,
    prev,
    getCurrentIndex,
    getTotalSlides,
    slides
  };
}

// Auto-initialize if in browser context
if (typeof window !== 'undefined' && typeof document !== 'undefined') {
  document.addEventListener('DOMContentLoaded', () => {
    const presentation = createPresentation();
    
    document.addEventListener('keydown', (e) => {
      const key = e.key;
      if (key === 'ArrowRight' || key === ' ' || key === 'PageDown') { e.preventDefault(); presentation.next(); }
      if (key === 'ArrowLeft' || key === 'PageUp') { e.preventDefault(); presentation.prev(); }
      if (key === 'Home') { e.preventDefault(); presentation.show(0); }
      if (key === 'End') { e.preventDefault(); presentation.show(presentation.getTotalSlides() - 1); }
    });

    // Click / tap navigation zones
    document.addEventListener('click', (e) => {
      const x = e.clientX / window.innerWidth;
      if (x < 0.33) presentation.prev();
      else presentation.next();
    });

    // Init
    presentation.show(0);
  });
}

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { createPresentation };
}
