// tailwind.config.js
module.exports = {
  content: [
    './index.html',                // Make sure Tailwind processes your HTML
    './src/**/*.{vue,js,ts,jsx,tsx}', // Make sure Tailwind processes your Vue components
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
