# K-Site-Public – Minimal Setup Guide x_X

K-Site-Public converts a GitHub repo into a static site of viewer pages and folder indexes.

No GUI. No config hell. Just structure at the end of fully-automated pipeline.

---

## 🔧 SETUP

1. Clone this repo.
2. Edit `/config/settings.yaml`:  
   `site_base_path: /yourprojectname/` ← must match your GitHub Pages subpath  
   Example: for `user.github.io/myrepo` → set `/myrepo/`
3. Push to `main` = safe your config file.

That’s it. GitHub Actions builds + deploys the site to GitHub Pages.

---

## 🗂 STRUCTURE

- `/content/` → your input files  
- `/docs/` → auto-built static site  
- `/docs/download/` → copied raw files  
- `/src/templates/` → Jinja2 templates  
- `/k-site.py` → the builder script

---

## 📁 FILE TYPES SUPPORTED

- `.md` → rendered as styled markdown  
- `.py`, `.txt` → rendered as preformatted text/code block  
- `.json` → rendered as prettified JSON (inside `<pre>`)  
- `.csv` → rendered as an HTML table  
- `.jpg`, `.png` → displayed inline (image passthrough)  
- others → ignored or copied to `/download` if allowed

_Rendering is automatic — no need to tag files or configure behavior. K-Site infers it from extension._

---

## 🧭 NAVIGATION

Each viewer/index page includes:  
- **Home** → always points to `{{ site_base_path }}` (config-driven)  
- **Back** → browser history fallback  

No manual routing. Fully config-based.

---

## 🚀 HOW TO BUILD

Just push → GitHub Action runs  
→ Site deploys at GitHub Pages URL

Done.

---

## 📑 Site Contents

<!-- auto-generated TOC will be inserted here by build_readme_toc.py -->
(Will list all files and folders as links, like Table of Content)

---

🛠️ Built with **K-Site** — a zero-GUI, automation-first static site generator.  
→ Want your docs turned into a site like this? [Contact me on LinkedIn](https://www.linkedin.com/in/taras-khamardiuk)

— *Kay*
