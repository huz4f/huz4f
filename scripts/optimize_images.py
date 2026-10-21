#!/usr/bin/env python3
"""
optimize_images.py — Professional High-Fidelity Photo & Asset Pipeline for huz4f.com

Key Capabilities:
1. Discovers all photos in static/photos/ (including new, unregistered files).
2. Auto-converts Apple HEIC/HEIF photos to high-fidelity sRGB JPEGs, preserving Display P3 color calibration.
3. Maximizes image quality: preserves up to 2400-2600px resolution, uses progressive Lanczos resampling,
   and adaptively searches for the highest possible visual quality (85-92+) that complies with the 500 KB budget.
4. Auto-synchronizes static/photos/photos.json with intrinsic dimensions to maintain 0.000 CLS and 100% Performance.
"""

import os
import sys
import json
import io
import subprocess
from pathlib import Path

try:
    from PIL import Image, ImageCms
except ImportError:
    print("PIL (Pillow) is required for image optimization. Run: pip install Pillow")
    sys.exit(1)

ROOT_DIR = Path(__file__).resolve().parent.parent
MAX_IMAGE_KB = 500
SUPPORTED_EXTS = (".jpg", ".jpeg", ".png", ".webp", ".heic", ".avif")


def is_heic_file(file_path: Path) -> bool:
    """Check if file is HEIC/HEIF (either by extension or internal magic bytes)."""
    if file_path.suffix.lower() in (".heic", ".heif"):
        return True
    try:
        with open(file_path, "rb") as f:
            header = f.read(32)
            if b"ftypheic" in header or b"ftypmif1" in header or b"ftypmsf1" in header or b"ftyphevc" in header:
                return True
    except Exception:
        pass
    return False


def convert_heic_to_srgb_jpeg(file_path: Path) -> Path:
    """Converts HEIC file to high-fidelity sRGB JPEG using macOS sips & Pillow."""
    print(f"🔄 Converting Apple HEIC photo {file_path.name} to sRGB JPEG...")
    target_path = file_path.with_suffix(".jpg")
    temp_tiff = file_path.with_suffix(".tmp.tiff")

    try:
        subprocess.run(
            ["sips", "-s", "format", "tiff", str(file_path), "--out", str(temp_tiff)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        img = Image.open(temp_tiff)

        # Color calibration: Convert Display P3 to standard sRGB if present
        icc = img.info.get("icc_profile")
        if icc:
            try:
                input_profile = ImageCms.ImageCmsProfile(io.BytesIO(icc))
                srgb_profile = ImageCms.createProfile("sRGB")
                img = ImageCms.profileToProfile(img, input_profile, srgb_profile, outputMode="RGB")
            except Exception:
                pass

        img.save(target_path, "JPEG", quality=92, optimize=True)
        if temp_tiff.exists():
            temp_tiff.unlink()
        if file_path.suffix.lower() in (".heic", ".heif") and file_path != target_path:
            file_path.unlink()
        print(f"  ✔ Converted to high-fidelity JPEG: {target_path.name}")
        return target_path
    except Exception as e:
        print(f"  ✖ Failed to convert HEIC {file_path.name}: {e}")
        if temp_tiff.exists():
            temp_tiff.unlink()
        return file_path


def optimize_single_photo(img_path: Path) -> tuple[int, int]:
    """Optimizes an image to highest possible quality within MAX_IMAGE_KB budget."""
    if is_heic_file(img_path):
        img_path = convert_heic_to_srgb_jpeg(img_path)

    try:
        img = Image.open(img_path)
    except Exception as e:
        print(f"  ⚠️ Could not open {img_path.name}: {e}")
        return 0, 0

    # Color profile check
    icc = img.info.get("icc_profile")
    if icc and img.mode == "RGB":
        try:
            input_profile = ImageCms.ImageCmsProfile(io.BytesIO(icc))
            srgb_profile = ImageCms.createProfile("sRGB")
            img = ImageCms.profileToProfile(img, input_profile, srgb_profile, outputMode="RGB")
        except Exception:
            pass

    size_kb = img_path.stat().st_size / 1024
    w, h = img.size

    # If already within budget and standard format, preserve original pixels
    if size_kb <= MAX_IMAGE_KB and max(w, h) <= 2600:
        return w, h

    print(f"Optimizing {img_path.name} ({size_kb:.1f} KB, {w}x{h}) for maximum visual fidelity...")

    # Max resolution target: 2400px (crystal sharp on 4K/Retina)
    if max(w, h) > 2400:
        ratio = 2400 / max(w, h)
        w, h = int(w * ratio), int(h * ratio)
        img = img.resize((w, h), Image.Resampling.LANCZOS)

    ext = img_path.suffix.lower()
    if ext in (".jpg", ".jpeg"):
        # Adaptive quality search: find highest quality (up to 92) that meets budget
        best_quality = 90
        fitted = False
        for test_q in (92, 90, 88, 86, 84, 82, 80, 78, 76):
            buffer = io.BytesIO()
            img.save(buffer, "JPEG", quality=test_q, optimize=True)
            if buffer.tell() / 1024 <= MAX_IMAGE_KB:
                best_quality = test_q
                fitted = True
                break

        # If still exceeding budget, progressively downscale while keeping high quality (82)
        if not fitted:
            best_quality = 82
            while max(w, h) > 1000:
                scale_ratio = 0.95
                w, h = int(w * scale_ratio), int(h * scale_ratio)
                img = img.resize((w, h), Image.Resampling.LANCZOS)
                buffer = io.BytesIO()
                img.save(buffer, "JPEG", quality=best_quality, optimize=True)
                if buffer.tell() / 1024 <= MAX_IMAGE_KB:
                    break

        img.save(img_path, "JPEG", quality=best_quality, optimize=True)
    elif ext == ".webp":
        img.save(img_path, "WEBP", quality=90, method=6)

    new_size_kb = img_path.stat().st_size / 1024
    print(f"  ✔ {img_path.name}: {size_kb:.1f} KB -> {new_size_kb:.1f} KB (resolution: {w}x{h})")
    return w, h


def optimize_photos():
    photos_dir = ROOT_DIR / "static" / "photos"
    photos_json_path = photos_dir / "photos.json"

    meta_data = {}
    if photos_json_path.exists():
        with open(photos_json_path, "r", encoding="utf-8") as f:
            try:
                meta_data = json.load(f)
            except Exception:
                meta_data = {}

    updated_meta = False

    # Scan static/photos/ for all supported image assets (including unindexed ones)
    found_files = []
    for item in sorted(photos_dir.iterdir()):
        if item.is_file() and item.suffix.lower() in SUPPORTED_EXTS and item.name != "photos.json":
            found_files.append(item)

    for img_path in found_files:
        w, h = optimize_single_photo(img_path)
        if w <= 0 or h <= 0:
            continue

        filename = img_path.name
        if filename not in meta_data:
            # Auto-register new photo in photos.json
            name_stem = img_path.stem.replace("-", " ").replace("_", " ").title()
            meta_data[filename] = {
                "title": name_stem,
                "description": "",
                "album": "1",
                "width": w,
                "height": h,
            }
            updated_meta = True
            print(f"  ✨ Auto-registered new photo in photos.json: {filename} ({w}x{h})")
        else:
            meta = meta_data[filename]
            if meta.get("width") != w or meta.get("height") != h:
                meta["width"] = w
                meta["height"] = h
                updated_meta = True

    # Sort keys numerically (1.jpg, 2.jpg ... 46.jpg)
    def sort_key(name: str):
        stem = name.split(".")[0]
        return (0, int(stem)) if stem.isdigit() else (1, name)

    sorted_meta = {k: meta_data[k] for k in sorted(meta_data.keys(), key=sort_key)}

    if updated_meta or sorted_meta != meta_data:
        with open(photos_json_path, "w", encoding="utf-8") as f:
            json.dump(sorted_meta, f, indent=2)
        print("✔ Synchronized static/photos/photos.json with latest dimensions and photos.")


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
    print("   HUZ4F.COM — HIGH-FIDELITY IMAGE PIPELINE")
    print("=" * 60)
    optimize_photos()
    scan_and_report()


if __name__ == "__main__":
    main()
