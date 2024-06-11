/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        gotham: ['Gotham', 'sans-serif'],
      },
      fontWeight: {
        light: 300,
        medium: 500,
        bold: 700,
        black: 900,
      },
      ackgroundImage: {
        'home-bg': "url('/src/img/glasto-poster3.png')",
      },
    },
  },
  plugins: [],
}