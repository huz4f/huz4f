#!/usr/bin/env python3
"""
verify_site.py — Automated SEO, AEO, Performance & Accessibility Verification Engine
Designed for huz4f.com (Hugo + PaperMod)

Audits:
1. Markdown Content Linting (Frontmatter, Heading hierarchy, Alt text, Local asset existence)
2. Photo Metadata & Asset Integrity (dimensions, file existence, CLS prevention)
3. Clean Hugo Build Execution (--gc --minify --cleanDestinationDir)
4. Generated HTML DOM & Link Audit:
   - Single <h1> per page
   - Sequential heading levels (no skips)
   - Meta description, title, canonical URL, OpenGraph tags
   - Valid Schema.org JSON-LD Graph (Person, WebSite, BlogPosting, SoftwareApplication, ImageGallery)
   - Image <img> alt attributes, dimensions, and file existence on disk
   - Zero broken internal links (dead link detection)
   - Accessibility (<html lang>) and mobile viewport (<meta name="viewport">)
   - External link security (rel="noopener" on target="_blank")
5. Robots.txt (AI Answer Engine bot directives: GPTBot, ClaudeBot, PerplexityBot)
6. Sitemap.xml (validity, URL schemas)
7. Performance Asset Budgets (image/CSS/JS file size limits)

Exit code 0 on complete pass, 1 on any violation.
"""

import sys
import os
import glob
import json
import re
import subprocess
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser

ROOT_DIR = Path(__file__).resolve().parent.parent

# Color output helpers
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"


class AuditReport:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed_checks = 0

    def add_error(self, category: str, message: str, file_path: str = ""):
        prefix = f"[{file_path}] " if file_path else ""
        self.errors.append(f"{BOLD}{category}:{RESET} {prefix}{message}")

    def add_warning(self, category: str, message: str, file_path: str = ""):
        prefix = f"[{file_path}] " if file_path else ""
        self.warnings.append(f"{BOLD}{category}:{RESET} {prefix}{message}")

    def pass_check(self, count: int = 1):
        self.passed_checks += count

    def print_summary(self, strict: bool = False):
        print(f"\n{BOLD}═══════════════════════════════════════════════════════════════{RESET}")
        print(f"{BOLD}                AUDIT RESULTS & VERIFICATION                  {RESET}")
        print(f"{BOLD}═══════════════════════════════════════════════════════════════{RESET}")

        if self.warnings:
            print(f"\n{YELLOW}{BOLD}⚠ Warnings ({len(self.warnings)}):{RESET}")
            for w in self.warnings:
                print(f"  {YELLOW}•{RESET} {w}")

        has_failed = bool(self.errors) or (strict and bool(self.warnings))

        if self.errors:
            print(f"\n{RED}{BOLD}✖ Errors ({len(self.errors)}):{RESET}")
            for e in self.errors:
                print(f"  {RED}•{RESET} {e}")

        if has_failed:
            print(f"\n{RED}{BOLD}FAILED:{RESET} Verification checks failed. Resolve issues before committing/deploying.")
            return False
        else:
            print(f"\n{GREEN}{BOLD}✔ ALL CHECKS PASSED:{RESET} {self.passed_checks} verifications succeeded.")
            print(f"{GREEN}Site is 100% compliant with SEO, AEO, Accessibility & Performance standards!{RESET}\n")
            return True


# ----------------------------------------------------------------------
# 1. MARKDOWN CONTENT LINTER
# ----------------------------------------------------------------------
def check_markdown_content(report: AuditReport, verbose: bool = False):
    print(f"\n{BLUE}{BOLD}[1/7] Auditing Markdown Content Files (content/)...{RESET}")
    content_dir = ROOT_DIR / "content"
    md_files = sorted(content_dir.glob("**/*.md"))

    for md_path in md_files:
        rel_path = str(md_path.relative_to(ROOT_DIR))
        text = md_path.read_text(encoding="utf-8", errors="replace")

        # Parse frontmatter
        fm_text = ""
        body_text = text
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                fm_text = parts[1]
                body_text = parts[2]

        is_draft = bool(re.search(r"^\s*draft:\s*true", fm_text, re.MULTILINE | re.IGNORECASE))

        # Check title
        has_title = bool(re.search(r"^\s*title:\s*.+", fm_text, re.MULTILINE))
        if not has_title:
            report.add_error("Content/Frontmatter", "Missing 'title' in frontmatter", rel_path)
        else:
            report.pass_check()

        # Check description (mandatory for published posts)
        desc_match = re.search(r"^\s*description:\s*[\"']?(.*?)[\"']?\s*$", fm_text, re.MULTILINE)
        if not is_draft:
            if not desc_match or not desc_match.group(1).strip():
                report.add_error("SEO/Description", "Published page is missing 'description' in frontmatter (critical for SEO/AEO)", rel_path)
            else:
                desc = desc_match.group(1).strip()
                if len(desc) < 20:
                    report.add_warning("SEO/Description", f"Description is very short ({len(desc)} chars). Aim for 50-160 chars.", rel_path)
                report.pass_check()

        # Check for Heading 1 '# ' inside markdown body (theme handles page h1)
        body_lines = body_text.splitlines()
        for idx, line in enumerate(body_lines, start=1):
            s = line.strip()
            if s.startswith("# ") and not s.startswith("##"):
                report.add_error("A11y/SEO Headings", f"Line {idx}: Found '# ' (h1) in markdown body. Use '##' (h2) instead; page title is already h1.", rel_path)

        # Check for heading level skips in markdown body
        current_level = 1  # starts after page h1
        for idx, line in enumerate(body_lines, start=1):
            s = line.strip()
            if s.startswith("#"):
                m = re.match(r"^(#+)\s", s)
                if m:
                    level = len(m.group(1))
                    if level > current_level + 1:
                        report.add_error("A11y/SEO Headings", f"Line {idx}: Heading level skipped from h{current_level} to h{level} (cannot skip levels).", rel_path)
                    current_level = level

        # Check images for alt text and existence
        for idx, line in enumerate(body_lines, start=1):
            empty_alts = re.findall(r"!\[\s*\]\(([^\)]+)\)", line)
            if empty_alts:
                report.add_error("A11y/Images", f"Line {idx}: Image missing alt text '{empty_alts[0]}'. All images must have descriptive alt text.", rel_path)
            else:
                img_matches = re.findall(r"!\[([^\]]+)\]\(([^\)]+)\)", line)
                for alt, src in img_matches:
                    report.pass_check()
                    if not src.startswith(("http://", "https://", "data:")):
                        clean_src = src.split("?")[0].split("#")[0].lstrip("/")
                        exists = (
                            (ROOT_DIR / "static" / clean_src).exists()
                            or (ROOT_DIR / "assets" / clean_src).exists()
                            or (md_path.parent / clean_src).exists()
                        )
                        if not exists:
                            report.add_error("Content/Asset", f"Line {idx}: Referenced local image does not exist: '{src}'", rel_path)
                        else:
                            report.pass_check()


# ----------------------------------------------------------------------
# 2. PHOTO GALLERY METADATA INTEGRITY
# ----------------------------------------------------------------------
def check_photo_metadata(report: AuditReport):
    print(f"\n{BLUE}{BOLD}[2/7] Auditing Visual Arts & Photo Gallery Metadata...{RESET}")
    photos_json_path = ROOT_DIR / "static" / "photos" / "photos.json"
    if not photos_json_path.exists():
        report.add_error("Performance/Gallery", "static/photos/photos.json not found")
        return

    try:
        with open(photos_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        report.add_error("Performance/Gallery", f"Invalid JSON in photos.json: {e}")
        return

    photos_dir = ROOT_DIR / "static" / "photos"
    for filename, meta in data.items():
        img_file = photos_dir / filename
        if not img_file.exists():
            report.add_error("Gallery/Asset", f"Referenced photo file does not exist: {filename}")

        w = meta.get("width")
        h = meta.get("height")
        if not isinstance(w, int) or w <= 0 or not isinstance(h, int) or h <= 0:
            report.add_error("Performance/CLS", f"Photo {filename} missing valid intrinsic width/height (needed for 0.000 CLS)")
        else:
            report.pass_check()


# ----------------------------------------------------------------------
# 3. HUGO BUILD EXECUTION
# ----------------------------------------------------------------------
def run_hugo_build(report: AuditReport):
    print(f"\n{BLUE}{BOLD}[3/7] Building Site with Hugo Extended (--gc --minify --cleanDestinationDir)...{RESET}")
    try:
        proc = subprocess.run(
            ["hugo", "--gc", "--minify", "--cleanDestinationDir"],
            cwd=str(ROOT_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if proc.returncode != 0:
            report.add_error("Hugo/Build", f"Hugo build failed (code {proc.returncode}):\n{proc.stderr}")
        else:
            print(f"  {GREEN}✔ Hugo build succeeded cleanly.{RESET}")
            report.pass_check()
    except FileNotFoundError:
        report.add_error("Hugo/Build", "hugo command not found in PATH")


# ----------------------------------------------------------------------
# 4. GENERATED HTML AUDIT (DOM, Headings, Schemas, Images, Links, A11y)
# ----------------------------------------------------------------------
class HTMLDOMAuditor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_redirect = False
        self.title = None
        self.in_title = False
        self.html_lang = None
        self.has_viewport = False
        self.metas = {}
        self.canonical = None
        self.h1_count = 0
        self.headings = []
        self.images = []
        self.links = []
        self.json_ld_scripts = []
        self.in_ldjson = False
        self.cur_ldjson = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        tag_lower = tag.lower()

        if tag_lower == "html":
            self.html_lang = attrs_dict.get("lang")
        elif tag_lower == "title":
            self.in_title = True
        elif tag_lower == "meta":
            http_equiv = attrs_dict.get("http-equiv", "").lower()
            if http_equiv == "refresh":
                self.is_redirect = True
            if attrs_dict.get("name", "").lower() == "viewport":
                self.has_viewport = True
            name = attrs_dict.get("name") or attrs_dict.get("property")
            content = attrs_dict.get("content")
            if name and content:
                self.metas[name.lower()] = content
        elif tag_lower == "link":
            if attrs_dict.get("rel") == "canonical":
                self.canonical = attrs_dict.get("href")
        elif tag_lower in ("h1", "h2", "h3", "h4", "h5", "h6"):
            lvl = int(tag_lower[1])
            self.headings.append(lvl)
            if lvl == 1:
                self.h1_count += 1
        elif tag_lower == "a":
            href = attrs_dict.get("href")
            rel = attrs_dict.get("rel", "")
            target = attrs_dict.get("target", "")
            if href:
                self.links.append((href, rel, target))
        elif tag_lower == "script" and attrs_dict.get("type") == "application/ld+json":
            self.in_ldjson = True
            self.cur_ldjson = []
        elif tag_lower == "img":
            self.images.append(attrs_dict)

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower == "title":
            self.in_title = False
        elif tag_lower == "script" and self.in_ldjson:
            self.in_ldjson = False
            self.json_ld_scripts.append("".join(self.cur_ldjson))

    def handle_data(self, data):
        if self.in_title:
            self.title = (self.title or "") + data
        elif self.in_ldjson:
            self.cur_ldjson.append(data)


def audit_html_pages(report: AuditReport):
    print(f"\n{BLUE}{BOLD}[4/7] Auditing Generated HTML Pages (public/)...{RESET}")
    public_dir = ROOT_DIR / "public"
    if not public_dir.exists():
        report.add_error("Public", "public/ directory does not exist. Run Hugo build first.")
        return

    html_files = sorted(public_dir.glob("**/*.html"))
    all_public_files = set(str(p.relative_to(public_dir)) for p in public_dir.glob("**/*") if p.is_file())

    for html_file in html_files:
        rel_path = str(html_file.relative_to(ROOT_DIR))
        content = html_file.read_text(encoding="utf-8", errors="replace")

        auditor = HTMLDOMAuditor()
        auditor.feed(content)

        # Skip redirect alias stubs
        if auditor.is_redirect:
            report.pass_check()
            continue

        is_404 = "404.html" in rel_path

        # 1. Language attribute
        if not auditor.html_lang:
            report.add_error("A11y/Language", "Page missing 'lang' attribute on <html> tag", rel_path)
        else:
            report.pass_check()

        # 2. Viewport tag
        if not is_404:
            if not auditor.has_viewport:
                report.add_error("A11y/Mobile", "Page missing <meta name='viewport'> tag", rel_path)
            else:
                report.pass_check()

        # 3. Check title
        if not auditor.title or not auditor.title.strip():
            report.add_error("SEO/Title", "Page missing <title> tag", rel_path)
        else:
            report.pass_check()

        # 4. Check meta description
        if not is_404:
            desc = auditor.metas.get("description")
            if not desc or not desc.strip():
                report.add_error("SEO/Meta", "Page missing <meta name='description'>", rel_path)
            else:
                report.pass_check()

        # 5. Check canonical
        if not auditor.canonical:
            report.add_error("SEO/Canonical", "Page missing <link rel='canonical'>", rel_path)
        else:
            report.pass_check()

        # 6. Check OpenGraph tags
        if not is_404:
            for og_prop in ("og:title", "og:description"):
                if og_prop not in auditor.metas:
                    report.add_warning("SEO/Social", f"Page missing meta property '{og_prop}'", rel_path)
                else:
                    report.pass_check()

        # 7. Check Headings Hierarchy
        if not is_404:
            if auditor.h1_count == 0:
                report.add_error("A11y/SEO Headings", "Page has no <h1> heading tag", rel_path)
            elif auditor.h1_count > 1:
                report.add_error("A11y/SEO Headings", f"Page has {auditor.h1_count} <h1> headings! Strictly 1 <h1> per page allowed.", rel_path)
            else:
                report.pass_check()

            # Check heading progression skips
            for i in range(len(auditor.headings) - 1):
                cur_lvl = auditor.headings[i]
                nxt_lvl = auditor.headings[i + 1]
                if nxt_lvl > cur_lvl + 1:
                    report.add_error("A11y/SEO Headings", f"Heading level skipped in DOM: h{cur_lvl} directly followed by h{nxt_lvl}.", rel_path)
                else:
                    report.pass_check()

        # 8. Check Images (alt and file existence on disk)
        for img in auditor.images:
            src = img.get("src")
            if "alt" not in img:
                report.add_error("A11y/Images", f"<img> tag missing 'alt' attribute: {src}", rel_path)
            elif not img["alt"] and not img.get("role") == "presentation":
                report.add_warning("A11y/Images", f"<img> tag has empty alt='': {src}", rel_path)
            else:
                report.pass_check()

            if src and not src.startswith(("http://", "https://", "data:")):
                clean_src = src.split("?")[0].lstrip("/")
                if clean_src not in all_public_files:
                    report.add_error("Asset/Missing", f"Image asset not found on disk: '{src}'", rel_path)
                else:
                    report.pass_check()

        # 9. Check Links (Dead link detector & Security)
        for href, rel, target in auditor.links:
            if not href:
                continue
            if href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "#")):
                if target == "_blank":
                    rel_lower = rel.lower()
                    if "noopener" not in rel_lower and "noreferrer" not in rel_lower:
                        report.add_error("Security/ExternalLink", f"External link target='_blank' missing rel='noopener': {href}", rel_path)
                    else:
                        report.pass_check()
                continue

            clean_url = href.split("#")[0].split("?")[0].lstrip("/")
            if not clean_url:
                continue

            candidates = [
                clean_url,
                clean_url + "/index.html" if not clean_url.endswith("/") else clean_url + "index.html",
                clean_url.rstrip("/") + ".html",
            ]
            if not any(c in all_public_files for c in candidates):
                report.add_error("BrokenLink/404", f"Internal link target does not exist: '{href}'", rel_path)
            else:
                report.pass_check()

        # 10. Check Schema.org JSON-LD (AEO)
        if not auditor.json_ld_scripts:
            report.add_error("AEO/Schema", "Page missing Schema.org JSON-LD script", rel_path)
        else:
            for s_idx, raw_json in enumerate(auditor.json_ld_scripts):
                try:
                    ld_data = json.loads(raw_json)
                    context = ld_data.get("@context", "")
                    if "schema.org" not in str(context):
                        report.add_error("AEO/Schema", f"Schema #{s_idx} missing valid @context schema.org", rel_path)

                    graph = ld_data.get("@graph", [ld_data])
                    types = [item.get("@type") for item in graph if isinstance(item, dict)]

                    # Homepage must have Person and WebSite
                    if rel_path == "public/index.html":
                        if "Person" not in types or "WebSite" not in types:
                            report.add_error("AEO/Schema", f"Homepage schema graph missing Person or WebSite types. Found: {types}", rel_path)

                    # Blogs must have BlogPosting
                    elif "blogs/" in rel_path and not rel_path.endswith("blogs/index.html"):
                        if "BlogPosting" not in types:
                            report.add_error("AEO/Schema", f"Blog post schema missing BlogPosting type. Found: {types}", rel_path)

                    # Projects must have SoftwareApplication or CreativeWork
                    elif "projects/" in rel_path and not rel_path.endswith("projects/index.html"):
                        if not any(t in types for t in ("SoftwareApplication", "CreativeWork")):
                            report.add_error("AEO/Schema", f"Project post schema missing SoftwareApplication/CreativeWork type. Found: {types}", rel_path)

                    report.pass_check()
                except Exception as e:
                    report.add_error("AEO/Schema", f"Invalid JSON in Schema.org script #{s_idx}: {e}", rel_path)


# ----------------------------------------------------------------------
# 5. ROBOTS.TXT & SITEMAP VERIFICATION
# ----------------------------------------------------------------------
def check_robots_and_sitemap(report: AuditReport):
    print(f"\n{BLUE}{BOLD}[5/7] Auditing Robots.txt and Sitemap.xml (AI & Crawler Directives)...{RESET}")
    robots_path = ROOT_DIR / "public" / "robots.txt"
    if not robots_path.exists():
        report.add_error("SEO/Robots", "public/robots.txt not found")
    else:
        text = robots_path.read_text(encoding="utf-8")
        ai_bots = ["GPTBot", "ClaudeBot", "PerplexityBot"]
        for bot in ai_bots:
            if bot.lower() not in text.lower():
                report.add_error("AEO/Robots", f"robots.txt missing AI Answer Engine directive for: {bot}")
            else:
                report.pass_check()

        if "sitemap: https://huz4f.com/sitemap.xml" not in text.lower():
            report.add_error("SEO/Robots", "robots.txt missing 'Sitemap: https://huz4f.com/sitemap.xml'")
        else:
            report.pass_check()

    sitemap_path = ROOT_DIR / "public" / "sitemap.xml"
    if not sitemap_path.exists():
        report.add_error("SEO/Sitemap", "public/sitemap.xml not found")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            urls = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
            if len(urls) < 10:
                report.add_warning("SEO/Sitemap", f"sitemap.xml only contains {len(urls)} URLs. Expected at least 10.")
            else:
                report.pass_check()
        except Exception as e:
            report.add_error("SEO/Sitemap", f"Invalid XML in sitemap.xml: {e}")


# ----------------------------------------------------------------------
# 6. PERFORMANCE & ASSET BUDGET AUDIT
# ----------------------------------------------------------------------
def check_asset_budgets(report: AuditReport):
    print(f"\n{BLUE}{BOLD}[6/7] Auditing Asset Budgets (Image weights, CSS/JS bloat)...{RESET}")
    MAX_IMAGE_KB = 500
    MAX_CSS_KB = 300
    MAX_JS_KB = 300

    public_dir = ROOT_DIR / "public"
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
        for img_path in public_dir.glob(f"**/{ext}"):
            size_kb = img_path.stat().st_size / 1024
            rel_path = str(img_path.relative_to(ROOT_DIR))
            if size_kb > MAX_IMAGE_KB:
                report.add_warning("Performance/AssetSize", f"Image {img_path.name} is {size_kb:.1f} KB (budget: {MAX_IMAGE_KB} KB)", rel_path)
            else:
                report.pass_check()

    for css_path in public_dir.glob("**/*.css"):
        size_kb = css_path.stat().st_size / 1024
        if size_kb > MAX_CSS_KB:
            report.add_error("Performance/CSS", f"CSS {css_path.name} is {size_kb:.1f} KB (budget: {MAX_CSS_KB} KB)")
        else:
            report.pass_check()

    for js_path in public_dir.glob("**/*.js"):
        size_kb = js_path.stat().st_size / 1024
        if size_kb > MAX_JS_KB:
            report.add_error("Performance/JS", f"JS {js_path.name} is {size_kb:.1f} KB (budget: {MAX_JS_KB} KB)")
        else:
            report.pass_check()


# ----------------------------------------------------------------------
# 7. MAIN RUNNER
# ----------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Audit site for SEO, AEO, Performance & Accessibility")
    parser.add_argument("--no-build", action="store_true", help="Skip Hugo build command and audit existing public/")
    parser.add_argument("--strict", action="store_true", help="Strict mode: treat warnings as fatal errors")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    print(f"\n{BOLD}================================================================{RESET}")
    print(f"{BOLD}         HUZ4F.COM — QUALITY, SEO & AEO VERIFICATION            {RESET}")
    print(f"{BOLD}================================================================{RESET}")

    report = AuditReport()

    # 1. Markdown content
    check_markdown_content(report, verbose=args.verbose)

    # 2. Photos metadata
    check_photo_metadata(report)

    # 3. Hugo build
    if not args.no_build:
        run_hugo_build(report)

    # 4. Generated HTML audit
    audit_html_pages(report)

    # 5. Robots and Sitemap
    check_robots_and_sitemap(report)

    # 6. Performance asset budgets
    check_asset_budgets(report)

    # Summary
    success = report.print_summary(strict=args.strict)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
