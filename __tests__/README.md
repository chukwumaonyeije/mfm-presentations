# Presentation Tests

Unit tests for the presentation slide navigation system.

## Setup

Install dependencies:

```bash
npm install
```

## Running Tests

Run all tests:
```bash
npm test
```

Run tests in watch mode:
```bash
npm run test:watch
```

## Test Coverage

The test suite covers:

1. **show() function** - Displays the correct slide based on the provided index
   - Shows specific slides by index
   - Clamps indices to valid range
   - Updates progress bar and counter
   - Sets proper aria-hidden attributes for accessibility

2. **next() function** - Advances to the subsequent slide
   - Moves forward one slide at a time
   - Prevents advancing beyond the last slide

3. **prev() function** - Navigates to the previous slide
   - Moves backward one slide at a time
   - Prevents navigating before the first slide

4. **Home key navigation** - Displays the first slide when Home key is pressed
   - Works from any slide position
   - Safe when already on first slide

5. **End key navigation** - Displays the last slide when End key is pressed
   - Works from any slide position
   - Safe when already on last slide

6. **Edge cases**
   - Single slide presentations
   - Empty presentations

## Architecture

The presentation logic has been extracted into `shared/presentation.js` as a reusable module that:
- Can be tested in isolation with jsdom
- Auto-initializes in browser contexts
- Exports the `createPresentation` factory function for testing
