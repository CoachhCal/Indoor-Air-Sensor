// tailwind.config.js
module.exports = {
  content: [
    './index.html',                // Make sure Tailwind processes your HTML
    './src/**/*.{vue,js,ts,jsx,tsx}', // Make sure Tailwind processes your Vue components
  ],
  theme: {
    extend: {},
    screens: {
      'xs': '480px',       
      'sm': '640px',      
      'md': '800px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
  },
  plugins: [],
}
