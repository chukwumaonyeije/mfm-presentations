module.exports = {
  testEnvironment: 'jsdom',
  testMatch: ['**/__tests__/**/*.test.js'],
  collectCoverageFrom: [
    'shared/**/*.js',
    '!**/__tests__/**'
  ]
};
