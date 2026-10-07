# GitHub Copilot Instructions for huz4f.com

Follow all development, SEO, AEO, accessibility, and quality standards documented in [AGENTS.md](../AGENTS.md):

1. **Mandatory Verification**: Every proposed modification must pass `python3 scripts/verify_site.py`.
2. **Strict Heading Hierarchy**: Never use `# ` (`h1`) in markdown content. Start with `## ` (`h2`) and never skip levels (`##` -> `###` -> `####`).
3. **Mandatory Descriptions & Alt Text**: All published markdown files (`draft: false`) must have a frontmatter `description` (50–160 chars). All markdown images `![Alt text](path)` must contain descriptive alt text.
4. **Structured Data (AEO)**: All pages must preserve the Schema.org JSON-LD graph anchored to `https://huz4f.com/#person`.
5. **Layout Shift Prevention (0.000 CLS)**: All images and photo gallery items must have intrinsic width and height defined in `static/photos/photos.json` or image markup.
6. **Crawler Directives**: Preserve AI crawler directives in `static/robots.txt` for GPTBot, ClaudeBot, PerplexityBot, etc.
