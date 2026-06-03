# portfolio-website

**Repository:** [github.com/EnithV/portfolio-website](https://github.com/EnithV/portfolio-website)  
**Live site:** https://enithv.github.io/portfolio-website/

Modern portfolio built with **Bootstrap 5**, focused on **Full-Stack Java Developer** roles. Bilingual: English (`index.html`) and Spanish (`index-es.html`).

---

## Features

- Sticky navigation with smooth scroll and active section highlight
- Full-screen hero with profile photo and CTAs
- Skill cards (Java Full-Stack featured)
- Career highlights with LinkedIn link (no duplicate CV)
- GV logo with transparent background
- Project grid with filter (All · Full-Stack · Data & AI), including NASA APOD, Weather App, and practice exercises
- Challenge / Solution blocks per project
- Contact section (Email link, no phone shown)
- Responsive, accessible layout (skip link, focus states, semantic HTML)
- Typography: [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans)

---

## Structure

```
portfolio-website/
├── index.html          # English
├── index-es.html       # Spanish
├── css/styles.css      # Custom theme on top of Bootstrap
├── js/main.js          # Scroll, nav, project filters
├── img/logo-icon.png   # GV logo, true transparency (from LogoT.png)
├── img/favicon.png     # 32×32 favicon
├── scripts/process-logo.mjs  # Regenerate icons if LogoT.png changes
├── CV-EGicela_Vargas.pdf  # Downloadable CV (About section)
├── Foto_Port.png       # Profile photo (hero)
├── .nojekyll           # GitHub Pages (skip Jekyll)
└── README.md
```

---

## Local preview

Open `index.html` in the browser, or use any static server:

```bash
cd portfolio-website
npx serve .
```

---

## Project card thumbnails

When adding or updating a project in `index.html` / `index-es.html`:

1. Prefer **Pexels** direct URLs (`images.pexels.com/.../pexels-photo-....jpeg?auto=compress&cs=tinysrgb&w=600`) — same pattern as Weather App. Unsplash links often return **404** or fail on GitHub Pages (blank white image).
2. **Verify** the URL returns `HTTP 200` before committing (e.g. `curl -I <url>`).
3. Use the **same** `src` in EN and ES; only change `alt` text per language.

---

## GitHub Pages

1. Push this folder to [EnithV/portfolio-website](https://github.com/EnithV/portfolio-website).
2. **Settings → Pages →** branch `main`, folder `/ (root)`.
3. Site URL: https://enithv.github.io/portfolio-website/

---

## Related projects

| Project | Repository | Live demo |
|---------|------------|-----------|
| **NASA APOD** | [NASA_APOD](https://github.com/EnithV/NASA_APOD) | [enithv.github.io/NASA_APOD](https://enithv.github.io/NASA_APOD/) |
| **Weather App** | [WeatherApp](https://github.com/EnithV/WeatherApp) | [weatherapp-6yp3.onrender.com](https://weatherapp-6yp3.onrender.com/) |
| **Practice exercises** | [Excercises_practice](https://github.com/EnithV/Excercises_practice) | [enithv.github.io/Excercises_practice](https://enithv.github.io/Excercises_practice/) |

---

## Author

**Gicela Vargas** — Full-Stack Java Developer · Civil Engineer · Data & AI
