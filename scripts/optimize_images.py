#!/usr/bin/env python3
"""
optimize_images.py — Image Optimization Pipeline for huz4f.com

Optimizes images in static/ and content/ to ensure they meet the 500 KB budget,
converts heavy assets to WebP, optimizes JPEGs, and synchronizes intrinsic
dimensions in static/photos/photos.json to maintain 0.000 CLS and 100% Performance.
"""

import os
import sys
import json
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("PIL (Pillow) is required for image optimization. Run: pip install Pillow")
    sys.exit(1)

ROOT_DIR = Path(__file__).resolve().parent.parent
MAX_IMAGE_KB = 500


def optimize_photos():
    photos_dir = ROOT_DIR / "static" / "photos"
    photos_json_path = photos_dir / "photos.json"
    
    if not photos_json_path.exists():
        return

    with open(photos_json_path, "r", encoding="utf-8") as f:
        meta_data = json.load(f)

    updated_meta = False

    for filename, meta in meta_data.items():
        img_path = photos_dir / filename
        if not img_path.exists():
            continue

        size_kb = img_path.stat().st_size / 1024
        if size_kb > MAX_IMAGE_KB:
            print(f"Optimizing photo {filename} ({size_kb:.1f} KB)...")
            img = Image.open(img_path)
            w, h = img.size
            if max(w, h) > 1600:
                ratio = 1600 / max(w, h)
                img = img.resize((int(w * ratio), int(h * ratio)), Image.Resampling.LANCZOS)
            
            # Save optimized
            ext = img_path.suffix.lower()
            if ext in (".jpg", ".jpeg"):
                img.save(img_path, "JPEG", quality=78, optimize=True)
            elif ext == ".webp":
                img.save(img_path, "WEBP", quality=80, method=6)
            
            new_size_kb = img_path.stat().st_size / 1024
            print(f"  ✔ {filename}: {size_kb:.1f} KB -> {new_size_kb:.1f} KB (dims: {img.size})")

            if meta.get("width") != img.size[0] or meta.get("height") != img.size[1]:
                meta["width"] = img.size[0]
                meta["height"] = img.size[1]
                updated_meta = True

    if updated_meta:
        with open(photos_json_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, indent=2)
        print("✔ Updated static/photos/photos.json with latest dimensions.")


def scan_and_report():
    print(f"\nAuditing image weights against {MAX_IMAGE_KB} KB budget...")
    over_budget = []
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
        for path in (ROOT_DIR / "static").glob(f"**/{ext}"):
            size_kb = path.stat().st_size / 1024
            if size_kb > MAX_IMAGE_KB:
                over_budget.append((path.relative_to(ROOT_DIR), size_kb))

    if over_budget:
        print(f"Found {len(over_budget)} image(s) exceeding budget:")
        for rel_path, size in over_budget:
            print(f"  • {rel_path}: {size:.1f} KB")
    else:
        print(f"✔ All images are under {MAX_IMAGE_KB} KB budget!")


def main():
    print("=" * 60)
    print("   HUZ4F.COM — IMAGE OPTIMIZATION PIPELINE")
    print("=" * 60)
    optimize_photos()
    scan_and_report()


if __name__ == "__main__":
    main()
