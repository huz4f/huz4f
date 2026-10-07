---
trigger: always_on
description: Mandatory SEO, AEO, accessibility, performance and quality gate requirements for huz4f.com
---

# Quality, SEO & AEO Inviolable Directives

When writing content, modifying templates, editing CSS, or adding assets to this repository:

1. **Mandatory Verification**: Always run `python3 scripts/verify_site.py` and verify all checks pass before concluding work or proposing a commit.
2. **Strict Heading Hierarchy**:
   - Never place `# ` (`h1`) in markdown content; the page title is already the `<h1>`.
   - Never skip heading levels (e.g., `##` directly to `####` is forbidden).
3. **Mandatory Descriptions & Alt Text**:
   - Every published markdown document (`draft: false`) must have a frontmatter `description` (50–160 chars).
   - Every markdown image `![Alt text](path)` must have non-empty, descriptive alt text.
4. **Structured Data (AEO)**:
   - Ensure all pages preserve Schema.org JSON-LD `@graph` linked to `https://huz4f.com/#person`.
5. **No Layout Shifts (0.000 CLS)**:
   - Always define intrinsic `width` and `height` for image assets and in `static/photos/photos.json`.
6. **AI Bot Crawler Directives**:
   - Maintain permissions for `GPTBot`, `ClaudeBot`, `PerplexityBot` in `static/robots.txt`.
