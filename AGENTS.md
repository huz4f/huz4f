# AGENTS.md — huz4f.com Development, SEO & AEO Guidelines

This document provides strict engineering, design, SEO, and AEO (Answer Engine Optimization) protocols for any AI agent or developer working in this repository.

---

## 1. Core Principles & Zero-Tolerance Standards

The website **huz4f.com** maintains a **100/100 Google Lighthouse** standard across:
1. **Performance** (100) — Sub-second LCP, 0.000 CLS, minimal payloads, WebP image pipeline.
2. **Accessibility** (100) — WCAG 2.1 AAA contrast, strict heading hierarchy, full keyboard/screen reader navigability.
3. **Best Practices** (100) — Clean CSP, secure attributes (`rel="noopener"`), modern Web APIs.
4. **SEO & AEO** (100) — Complete Schema.org entity graph (`@graph`), descriptive metadata, AI Answer Engine discovery directives.

**Any proposed change MUST pass the automated verification engine:**
```bash
python3 scripts/verify_site.py
```

---

## 2. Content & Markdown Protocol

### 2.1 Frontmatter Requirements
Every new or modified content file in `content/` (`Blogs/`, `Projects/`, `pages/`) must adhere to this frontmatter schema:

```yaml
---
title: "Descriptive Page Title"
description: "Clear, concise summary (50–160 characters) explaining the key value or topic. Essential for search engine snippets and AI answer synthesis."
date: 2026-10-08
tags: ["engineering", "architecture"]
author: "Huzaif"
draft: false
---
```

- **`description` is mandatory** for all published pages (`draft: false`).
- Do not use markdown syntax, links, or HTML inside frontmatter descriptions.

### 2.2 Heading Hierarchy (`h1` -> `h2` -> `h3`)
- **NEVER use `# ` (`h1`) inside markdown content or shortcodes.** The Hugo template (`single.html`) already renders the page title as the unique `<h1>`.
- Start top-level content sections with `## ` (`h2`).
- Subsections must use `### ` (`h3`), followed by `#### ` (`h4`).
- **Never skip heading levels.** For example, `##` followed directly by `####` violates WCAG accessibility and Lighthouse SEO audits.

### 2.3 Image Optimization & Accessibility
- **Descriptive Alt Text:** Every markdown image `![Alt text](path)` must contain a clear, descriptive alt text explaining the image content. Never commit empty alt text `![]()`.
- **Image Formats:** Prefer `.webp` for photographs and screenshots.
- **Asset Size Budget:** Individual images in content or static should be kept under 500 KB whenever possible.
- **Photo Gallery:** If adding images to `static/photos/`, you MUST record the file in `static/photos/photos.json` with intrinsic `width` and `height`:
  ```json
  "filename.jpg": {
    "title": "Title",
    "description": "Optional description",
    "album": "1",
    "width": 1200,
    "height": 800
  }
  ```
  Missing dimensions cause layout shift (CLS), breaking the 100 Performance score.

---

## 3. SEO & AEO (Answer Engine Optimization) Architecture

### 3.1 Schema.org Entity Graph
All structured data is managed in `layouts/partials/templates/schema_json.html`.
- Global identity is anchored to `@id: "https://huz4f.com/#person"`.
- Root page renders `Person` and `WebSite` with `SearchAction`.
- Blog posts render `BlogPosting` with `headline`, `author`, `datePublished`, and `publisher`.
- Project pages render `SoftwareApplication` or `CreativeWork`.
- Visual arts renders `ImageGallery`.
- If creating new layouts, never remove or bypass `schema_json.html`.

### 3.2 AI Answer Engine Directives (`static/robots.txt`)
`static/robots.txt` explicitly allows and directs modern AI crawlers:
- `GPTBot` (OpenAI / ChatGPT)
- `ClaudeBot` (Anthropic / Claude)
- `PerplexityBot` (Perplexity AI)
- `Applebot-Extended`
- `Google-Extended`
Always preserve these directives and the `Sitemap: https://huz4f.com/sitemap.xml` reference.

---

## 4. Accessibility & UI Styling

- **Color Contrast:** All text, badges, subtitles, and button labels must meet WCAG AAA (7:1) or AA (4.5:1) contrast against their respective backgrounds in both light and dark modes.
- **Special Pages:** The visual arts page uses `.page-full-black`. High contrast overrides exist in `assets/css/extended/custom.css` and must be preserved.
- **Modals & Lightboxes:** Hidden modal overlays must be inactive (`display: none !important;`) and inert to prevent invisible focus traps for screen readers.

---

## 5. Automated Quality Gates

The repository includes a 4-pillar automated safeguard system:
1. **Verification Engine:** `python3 scripts/verify_site.py` validates all markdown, JSON metadata, Hugo build, generated HTML DOM, Schema JSON-LD, robots.txt, sitemap, and asset sizes.
2. **Git Pre-Commit Hook:** `.githooks/pre-commit` automatically runs before every commit. Commits fail if any audit fails.
3. **GitHub Actions CI:** `.github/workflows/hugo.yml` runs verification on every pull request and push to `main` before deployment.
4. **Rules & Guidelines:** `AGENTS.md` and `GEMINI.md` inform all automated pair-programming sessions.

---

## 6. Verification Checklist Before Any Commit

Before committing any change, run:
```bash
python3 scripts/verify_site.py
```
Ensure output displays:
```
✔ ALL CHECKS PASSED: ... verifications succeeded.
Site is 100% compliant with SEO, AEO, Accessibility & Performance standards!
```
