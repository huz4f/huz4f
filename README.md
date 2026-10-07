# huz4f.com

Personal engineering portfolio, technical blog, and visual arts gallery for **Huzaif**. Built with [Hugo](https://gohugo.io/) and PaperMod, tuned to maintain a strict **100/100 Google Lighthouse** standard across Performance, Accessibility, Best Practices, and SEO/AEO.

---

## 🌟 Zero-Tolerance Quality Standards

Every build and commit must pass automated quality gates:
1. **Performance (100)**: Sub-second LCP, **0.000 CLS**, asset budgets (< 500 KB images, < 300 KB CSS/JS).
2. **Accessibility (100)**: WCAG 2.1 AAA contrast, strict single `<h1>` per page, sequential heading progression, descriptive image alt text.
3. **Best Practices (100)**: Clean CSP, secure attributes (`rel="noopener"` on external links), modern web standards.
4. **SEO & AEO (100)**: Rich Schema.org entity graph (`@graph`) anchored to `@id: "https://huz4f.com/#person"`, AI Answer Engine directives in `robots.txt` (`GPTBot`, `ClaudeBot`, `PerplexityBot`), XML sitemap, canonical links, and social OpenGraph tags.

---

## 🛠 Local Setup & Development

### 1. Prerequisites
- **Hugo Extended** (>= 0.120)
- **Python 3** (for verification engine & image optimization)
- Optional: `Pillow` (`pip install Pillow`) for image optimization

### 2. Configure Git Hooks (Mandatory)
Activate the automated pre-commit and pre-push quality gates:
```bash
./scripts/setup-hooks.sh
```

### 3. Local Development Server
```bash
hugo server -D
```
Open `http://localhost:1313`.

---

## 🧪 Verification & Optimization Engine

Before committing or pushing any changes, run the audit suite:

```bash
# Verify site (validates markdown, HTML DOM, headings, dead links, schemas, asset budgets)
python3 scripts/verify_site.py --strict
```

### Image Optimization Pipeline
If you add new photos or illustrations:
```bash
python3 scripts/optimize_images.py
```
This script automatically compresses images to meet the 500 KB budget and synchronizes intrinsic `width` and `height` dimensions in `static/photos/photos.json`.

---

## 🤖 AI Agent & Developer Guidelines

All AI pair-programming agents (Gemini, Claude, Cursor, Windsurf, Copilot) follow the strict standards defined in [`AGENTS.md`](./AGENTS.md).
