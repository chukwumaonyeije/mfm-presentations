/**
 * Unit tests for presentation slide navigation
 */

const { createPresentation } = require('../shared/presentation');

describe('Presentation Navigation', () => {
  let container;
  let presentation;
  let keydownHandler;

  beforeEach(() => {
    // Set up DOM structure
    document.body.innerHTML = `
      <div id="deck">
        <div id="bar"></div>
        <div id="counter">
          <span id="idx">1</span>
          <span>/</span>
          <span id="tot">0</span>
        </div>
        <section class="slide"></section>
        <section class="slide"></section>
        <section class="slide"></section>
        <section class="slide"></section>
        <section class="slide"></section>
      </div>
    `;

    presentation = createPresentation('section.slide');
    
    // Set up keyboard event listener for tests
    keydownHandler = (e) => {
      const key = e.key;
      if (key === 'ArrowRight' || key === ' ' || key === 'PageDown') { e.preventDefault(); presentation.next(); }
      if (key === 'ArrowLeft' || key === 'PageUp') { e.preventDefault(); presentation.prev(); }
      if (key === 'Home') { e.preventDefault(); presentation.show(0); }
      if (key === 'End') { e.preventDefault(); presentation.show(presentation.getTotalSlides() - 1); }
    };
    document.addEventListener('keydown', keydownHandler);
  });

  afterEach(() => {
    document.removeEventListener('keydown', keydownHandler);
    document.body.innerHTML = '';
  });

  describe('show() function', () => {
    test('displays the correct slide based on the provided index', () => {
      // Test showing slide at index 2 (third slide)
      presentation.show(2);
      
      const slides = document.querySelectorAll('section.slide');
      expect(slides[2].classList.contains('active')).toBe(true);
      expect(slides[0].classList.contains('active')).toBe(false);
      expect(slides[1].classList.contains('active')).toBe(false);
      expect(slides[3].classList.contains('active')).toBe(false);
      expect(slides[4].classList.contains('active')).toBe(false);
      
      expect(presentation.getCurrentIndex()).toBe(2);
      expect(document.getElementById('idx').textContent).toBe('3');
    });

    test('shows first slide when index is 0', () => {
      presentation.show(0);
      
      const slides = document.querySelectorAll('section.slide');
      expect(slides[0].classList.contains('active')).toBe(true);
      expect(presentation.getCurrentIndex()).toBe(0);
      expect(document.getElementById('idx').textContent).toBe('1');
    });

    test('shows last slide when index is total-1', () => {
      presentation.show(4);
      
      const slides = document.querySelectorAll('section.slide');
      expect(slides[4].classList.contains('active')).toBe(true);
      expect(presentation.getCurrentIndex()).toBe(4);
      expect(document.getElementById('idx').textContent).toBe('5');
    });

    test('clamps index to valid range (negative)', () => {
      presentation.show(-5);
      
      expect(presentation.getCurrentIndex()).toBe(0);
      const slides = document.querySelectorAll('section.slide');
      expect(slides[0].classList.contains('active')).toBe(true);
    });

    test('clamps index to valid range (too large)', () => {
      presentation.show(100);
      
      expect(presentation.getCurrentIndex()).toBe(4);
      const slides = document.querySelectorAll('section.slide');
      expect(slides[4].classList.contains('active')).toBe(true);
    });

    test('updates progress bar correctly', () => {
      presentation.show(2);
      
      const bar = document.getElementById('bar');
      expect(bar.style.width).toBe('60.0%'); // (2+1)/5 * 100 = 60%
    });

    test('sets aria-hidden attributes correctly', () => {
      presentation.show(2);
      
      const slides = document.querySelectorAll('section.slide');
      expect(slides[2].getAttribute('aria-hidden')).toBe('false');
      expect(slides[0].getAttribute('aria-hidden')).toBe('true');
      expect(slides[1].getAttribute('aria-hidden')).toBe('true');
      expect(slides[3].getAttribute('aria-hidden')).toBe('true');
      expect(slides[4].getAttribute('aria-hidden')).toBe('true');
    });
  });

  describe('next() function', () => {
    test('advances to the subsequent slide', () => {
      presentation.show(0);
      expect(presentation.getCurrentIndex()).toBe(0);
      
      presentation.next();
      expect(presentation.getCurrentIndex()).toBe(1);
      
      const slides = document.querySelectorAll('section.slide');
      expect(slides[1].classList.contains('active')).toBe(true);
      expect(document.getElementById('idx').textContent).toBe('2');
    });

    test('advances through multiple slides', () => {
      presentation.show(0);
      
      presentation.next();
      presentation.next();
      presentation.next();
      
      expect(presentation.getCurrentIndex()).toBe(3);
      const slides = document.querySelectorAll('section.slide');
      expect(slides[3].classList.contains('active')).toBe(true);
    });

    test('does not advance beyond last slide', () => {
      presentation.show(4); // Last slide
      expect(presentation.getCurrentIndex()).toBe(4);
      
      presentation.next();
      expect(presentation.getCurrentIndex()).toBe(4);
      
      const slides = document.querySelectorAll('section.slide');
      expect(slides[4].classList.contains('active')).toBe(true);
    });
  });

  describe('prev() function', () => {
    test('navigates to the previous slide', () => {
      presentation.show(3);
      expect(presentation.getCurrentIndex()).toBe(3);
      
      presentation.prev();
      expect(presentation.getCurrentIndex()).toBe(2);
      
      const slides = document.querySelectorAll('section.slide');
      expect(slides[2].classList.contains('active')).toBe(true);
      expect(document.getElementById('idx').textContent).toBe('3');
    });

    test('navigates back through multiple slides', () => {
      presentation.show(4);
      
      presentation.prev();
      presentation.prev();
      presentation.prev();
      
      expect(presentation.getCurrentIndex()).toBe(1);
      const slides = document.querySelectorAll('section.slide');
      expect(slides[1].classList.contains('active')).toBe(true);
    });

    test('does not navigate before first slide', () => {
      presentation.show(0); // First slide
      expect(presentation.getCurrentIndex()).toBe(0);
      
      presentation.prev();
      expect(presentation.getCurrentIndex()).toBe(0);
      
      const slides = document.querySelectorAll('section.slide');
      expect(slides[0].classList.contains('active')).toBe(true);
    });
  });

  describe('Keyboard navigation - Home key', () => {
    test('pressing "Home" key displays the first slide', () => {
      presentation.show(3);
      expect(presentation.getCurrentIndex()).toBe(3);
      
      // Simulate Home key press
      const event = new KeyboardEvent('keydown', { key: 'Home' });
      document.dispatchEvent(event);
      
      expect(presentation.getCurrentIndex()).toBe(0);
      const slides = document.querySelectorAll('section.slide');
      expect(slides[0].classList.contains('active')).toBe(true);
      expect(document.getElementById('idx').textContent).toBe('1');
    });

    test('Home key works from last slide', () => {
      presentation.show(4);
      
      const event = new KeyboardEvent('keydown', { key: 'Home' });
      document.dispatchEvent(event);
      
      expect(presentation.getCurrentIndex()).toBe(0);
    });

    test('Home key works when already on first slide', () => {
      presentation.show(0);
      
      const event = new KeyboardEvent('keydown', { key: 'Home' });
      document.dispatchEvent(event);
      
      expect(presentation.getCurrentIndex()).toBe(0);
      const slides = document.querySelectorAll('section.slide');
      expect(slides[0].classList.contains('active')).toBe(true);
    });
  });

  describe('Keyboard navigation - End key', () => {
    test('pressing "End" key displays the last slide', () => {
      presentation.show(1);
      expect(presentation.getCurrentIndex()).toBe(1);
      
      // Simulate End key press
      const event = new KeyboardEvent('keydown', { key: 'End' });
      document.dispatchEvent(event);
      
      expect(presentation.getCurrentIndex()).toBe(4);
      const slides = document.querySelectorAll('section.slide');
      expect(slides[4].classList.contains('active')).toBe(true);
      expect(document.getElementById('idx').textContent).toBe('5');
    });

    test('End key works from first slide', () => {
      presentation.show(0);
      
      const event = new KeyboardEvent('keydown', { key: 'End' });
      document.dispatchEvent(event);
      
      expect(presentation.getCurrentIndex()).toBe(4);
    });

    test('End key works when already on last slide', () => {
      presentation.show(4);
      
      const event = new KeyboardEvent('keydown', { key: 'End' });
      document.dispatchEvent(event);
      
      expect(presentation.getCurrentIndex()).toBe(4);
      const slides = document.querySelectorAll('section.slide');
      expect(slides[4].classList.contains('active')).toBe(true);
    });
  });

  describe('Edge cases', () => {
    test('handles single slide presentation', () => {
      document.body.innerHTML = `
        <div id="deck">
          <div id="bar"></div>
          <div id="counter">
            <span id="idx">1</span>
            <span>/</span>
            <span id="tot">0</span>
          </div>
          <section class="slide"></section>
        </div>
      `;

      const singleSlidePresentation = createPresentation('section.slide');
      
      expect(singleSlidePresentation.getTotalSlides()).toBe(1);
      
      singleSlidePresentation.next();
      expect(singleSlidePresentation.getCurrentIndex()).toBe(0);
      
      singleSlidePresentation.prev();
      expect(singleSlidePresentation.getCurrentIndex()).toBe(0);
    });

    test('handles empty presentation gracefully', () => {
      document.body.innerHTML = `
        <div id="deck">
          <div id="bar"></div>
          <div id="counter">
            <span id="idx">1</span>
            <span>/</span>
            <span id="tot">0</span>
          </div>
        </div>
      `;

      const emptyPresentation = createPresentation('section.slide');
      
      expect(emptyPresentation.getTotalSlides()).toBe(0);
      
      // Should not throw errors
      expect(() => emptyPresentation.show(0)).not.toThrow();
      expect(() => emptyPresentation.next()).not.toThrow();
      expect(() => emptyPresentation.prev()).not.toThrow();
    });
  });
});
