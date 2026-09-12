#!/usr/bin/env python3
"""
High-Resolution Favicon & App Icon Generator for Huz4f.com
Generates classic, timeless, high-contrast icon assets for all platforms & devices:
- favicon.svg (Modern responsive/retina vector favicon)
- safari-pinned-tab.svg (Monochrome vector for macOS Safari pinned tabs)
- favicon-16x16.png (Standard desktop tab icon)
- favicon-32x32.png (High-DPI / Retina desktop tab icon)
- favicon.ico (Multi-resolution Windows / browser icon containing 16x16, 32x32, 48x48)
- apple-touch-icon.png (180x180 for iOS Safari home screen & bookmarks)
- android-chrome-192x192.png (192x192 for Android & PWA)
- android-chrome-512x512.png (512x512 for high-res splash & PWA)
"""

import os
import zlib
import struct
import math

def create_png(width, height, rgba_data):
    """
    Creates a standard, fully valid PNG file from raw RGBA byte buffer.
    Uses pure standard library (zlib + struct).
    rgba_data must be bytes of length width * height * 4.
    """
    def chunk(chunk_type, data):
        return (
            struct.pack(">I", len(data)) +
            chunk_type +
            data +
            struct.pack(">I", zlib.crc32(chunk_type + data) & 0xffffffff)
        )

    header = b"\x89PNG\r\n\x1a\n"
    # IHDR: width(4), height(4), bit_depth(1=8), color_type(1=6: RGBA),
    # compression(1=0), filter(1=0), interlace(1=0)
    ihdr_data = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    ihdr = chunk(b"IHDR", ihdr_data)

    # Scanlines with filter byte 0 (None)
    raw_scanlines = bytearray()
    row_bytes = width * 4
    for y in range(height):
        raw_scanlines.append(0)  # Filter type 0
        offset = y * row_bytes
        raw_scanlines.extend(rgba_data[offset:offset + row_bytes])

    compressed = zlib.compress(bytes(raw_scanlines), 9)
    idat = chunk(b"IDAT", compressed)
    iend = chunk(b"IEND", b"")

    return header + ihdr + idat + iend


def create_ico(png_list):
    """
    Creates a valid modern multi-image Windows/browser .ICO file containing PNG data frames.
    png_list: list of tuples: (width, height, png_bytes)
    """
    # ICONDIR: reserved (2), type (2 = 1 for icon), count (2)
    count = len(png_list)
    header = struct.pack("<HHH", 0, 1, count)

    entries = bytearray()
    images_data = bytearray()

    offset = 6 + (16 * count)

    for w, h, p_bytes in png_list:
        width_byte = 0 if w >= 256 else w
        height_byte = 0 if h >= 256 else h
        size = len(p_bytes)

        # ICONDIRENTRY:
        # width (1), height (1), colorCount (1), reserved (1),
        # planes (2), bpp (2), bytesInRes (4), imageOffset (4)
        entry = struct.pack(
            "<BBBBHHII",
            width_byte,
            height_byte,
            0,
            0,
            1,
            32,
            size,
            offset
        )
        entries.extend(entry)
        images_data.extend(p_bytes)
        offset += size

    return header + bytes(entries) + bytes(images_data)


def render_icon(size, full_bleed=False):
    """
    Renders the classic 'H' monogram icon at given size with supersampling.
    - size: integer width/height
    - full_bleed: If True, background fills the entire square (used for Apple Touch Icon & Android Chrome)
                  If False, renders an elegant squircle badge with transparent corners and edge border
    Returns bytes of RGBA pixel data (length size * size * 4).
    """
    # Supersampling factor: 4x for sizes <= 64, 2x for larger sizes
    ss = 4 if size <= 64 else 2
    sw = size * ss
    sh = size * ss

    # Colors
    # Background gradient: Dark obsidian #18181b to #09090b
    bg_top = (24, 24, 27)
    bg_bot = (9, 9, 11)
    
    # Border: Zinc-800 #27272a
    border_color = (39, 39, 42)
    # Highlight rim: subtle top reflection
    rim_color = (82, 82, 91)
    
    # Text/Mark: Pure crisp white #ffffff
    mark_color = (255, 255, 255)

    # Geometry on normalized [0, 1] grid
    if full_bleed:
        # Full bleed: covers whole canvas
        badge_left = 0.0
        badge_top = 0.0
        badge_right = 1.0
        badge_bottom = 1.0
        badge_radius = 0.0
    else:
        # Squircle badge with margin
        margin = 0.04
        badge_left = margin
        badge_top = margin
        badge_right = 1.0 - margin
        badge_bottom = 1.0 - margin
        badge_radius = 0.22  # Apple / modern squircle proportion

    # H monogram normalized coordinates [0, 1]
    # Pillar width: 0.125
    # Inner gap: 0.17
    # Total width: 2 * 0.125 + 0.17 = 0.42
    # Total height: 0.51
    h_w = 0.42
    h_h = 0.51
    h_left = (1.0 - h_w) / 2.0
    h_right = h_left + h_w
    h_top = (1.0 - h_h) / 2.0
    h_bottom = h_top + h_h

    pillar_w = 0.125
    crossbar_h = 0.125
    crossbar_top = (h_top + h_bottom - crossbar_h) / 2.0
    crossbar_bottom = crossbar_top + crossbar_h

    p1_left = h_left
    p1_right = h_left + pillar_w
    p2_left = h_right - pillar_w
    p2_right = h_right

    # Precompute sample buffer
    out = bytearray(size * size * 4)

    # Subpixel sampling offsets
    sub_offsets = [( (i + 0.5) / ss, (j + 0.5) / ss ) for j in range(ss) for i in range(ss)]
    total_samples = len(sub_offsets)

    bw_half = (badge_right - badge_left) / 2.0
    bh_half = (badge_bottom - badge_top) / 2.0
    bc_x = (badge_left + badge_right) / 2.0
    bc_y = (badge_top + badge_bottom) / 2.0
    br = badge_radius
    inner_w = bw_half - br
    inner_h = bh_half - br

    # Border thickness in normalized units
    border_t = max(0.018, 1.2 / size)

    for py in range(size):
        for px in range(size):
            accum_r = 0.0
            accum_g = 0.0
            accum_b = 0.0
            accum_a = 0.0

            for ox, oy in sub_offsets:
                nx = (px + ox) / size
                ny = (py + oy) / size

                # Test if inside badge
                if full_bleed:
                    in_badge = True
                    on_border = False
                    on_rim = False
                else:
                    dx = abs(nx - bc_x) - inner_w
                    dy = abs(ny - bc_y) - inner_h
                    dx = max(dx, 0.0)
                    dy = max(dy, 0.0)
                    dist = math.sqrt(dx * dx + dy * dy) - br

                    if dist <= 0.0:
                        in_badge = True
                        # Check border
                        if dist > -border_t:
                            on_border = True
                            on_rim = (ny < bc_y) and (dist > -border_t * 0.5)
                        else:
                            on_border = False
                            on_rim = False
                    else:
                        in_badge = False
                        on_border = False
                        on_rim = False

                if not in_badge:
                    continue

                # Test if inside letter 'H'
                in_h = False
                if h_top <= ny <= h_bottom:
                    if (p1_left <= nx <= p1_right) or (p2_left <= nx <= p2_right):
                        in_h = True
                    elif (crossbar_top <= ny <= crossbar_bottom) and (p1_right <= nx <= p2_left):
                        in_h = True

                if in_h:
                    accum_r += mark_color[0]
                    accum_g += mark_color[1]
                    accum_b += mark_color[2]
                    accum_a += 255.0
                elif on_rim:
                    accum_r += rim_color[0]
                    accum_g += rim_color[1]
                    accum_b += rim_color[2]
                    accum_a += 255.0
                elif on_border:
                    accum_r += border_color[0]
                    accum_g += border_color[1]
                    accum_b += border_color[2]
                    accum_a += 255.0
                else:
                    # Subtle vertical gradient for background
                    t = ny
                    r = bg_top[0] * (1.0 - t) + bg_bot[0] * t
                    g = bg_top[1] * (1.0 - t) + bg_bot[1] * t
                    b = bg_top[2] * (1.0 - t) + bg_bot[2] * t
                    accum_r += r
                    accum_g += g
                    accum_b += b
                    accum_a += 255.0

            r = int(round(accum_r / total_samples))
            g = int(round(accum_g / total_samples))
            b = int(round(accum_b / total_samples))
            a = int(round(accum_a / total_samples))

            idx = (py * size + px) * 4
            out[idx] = r
            out[idx + 1] = g
            out[idx + 2] = b
            out[idx + 3] = a

    return bytes(out)


def get_svg_content():
    """
    Returns the vector SVG string for favicon.svg.
    Optimized for modern retina displays and high contrast.
    """
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18181b"/>
      <stop offset="100%" stop-color="#09090b"/>
    </linearGradient>
    <linearGradient id="rim" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.02"/>
    </linearGradient>
  </defs>

  <!-- Modern Obsidian Squircle Base -->
  <rect x="20" y="20" width="472" height="472" rx="112" fill="url(#bg)"/>
  
  <!-- Subtle border definition for dark/light browser chrome -->
  <rect x="20" y="20" width="472" height="472" rx="112" fill="none" stroke="#27272a" stroke-width="8"/>
  <rect x="24" y="24" width="464" height="464" rx="108" fill="none" stroke="url(#rim)" stroke-width="2"/>

  <!-- Classic Timeless H Monogram -->
  <path d="M 148 126 L 212 126 L 212 224 L 300 224 L 300 126 L 364 126 L 364 386 L 300 386 L 300 288 L 212 288 L 212 386 L 148 386 Z" fill="#ffffff"/>
</svg>
"""


def get_safari_pinned_tab_svg():
    """
    Returns the strict Apple specification vector SVG for safari-pinned-tab.svg.
    Must contain 100% black vector path (#000000) on transparent background.
    """
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <path d="M 148 126 L 212 126 L 212 224 L 300 224 L 300 126 L 364 126 L 364 386 L 300 386 L 300 288 L 212 288 L 212 386 L 148 386 Z" fill="#000000"/>
</svg>
"""


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    favicons_dir = os.path.join(static_dir, "favicons")
    public_dir = os.path.join(base_dir, "public")
    public_favicons_dir = os.path.join(public_dir, "favicons")

    os.makedirs(favicons_dir, exist_ok=True)
    if os.path.exists(public_dir):
        os.makedirs(public_favicons_dir, exist_ok=True)

    print("Generating SVG icons...")
    svg_data = get_svg_content().encode("utf-8")
    safari_svg_data = get_safari_pinned_tab_svg().encode("utf-8")

    # Render PNGs
    print("Rendering 16x16 PNG...")
    png_16 = create_png(16, 16, render_icon(16, full_bleed=False))

    print("Rendering 32x32 PNG...")
    png_32 = create_png(32, 32, render_icon(32, full_bleed=False))

    print("Rendering 48x48 PNG for ICO...")
    png_48 = create_png(48, 48, render_icon(48, full_bleed=False))

    print("Rendering Apple Touch Icon 180x180 PNG...")
    png_180 = create_png(180, 180, render_icon(180, full_bleed=True))

    print("Rendering Android Chrome 192x192 PNG...")
    png_192 = create_png(192, 192, render_icon(192, full_bleed=True))

    print("Rendering Android Chrome 512x512 PNG...")
    png_512 = create_png(512, 512, render_icon(512, full_bleed=True))

    print("Creating multi-resolution favicon.ico (16x16, 32x32, 48x48)...")
    ico_data = create_ico([
        (16, 16, png_16),
        (32, 32, png_32),
        (48, 48, png_48)
    ])

    # Target destinations
    file_map = {
        "favicon.svg": svg_data,
        "safari-pinned-tab.svg": safari_svg_data,
        "favicon-16x16.png": png_16,
        "favicon-32x32.png": png_32,
        "apple-touch-icon.png": png_180,
        "android-chrome-192x192.png": png_192,
        "android-chrome-512x512.png": png_512,
        "favicon.ico": ico_data,
    }

    # Write to static/ and static/favicons/
    for filename, content in file_map.items():
        # In static/favicons/
        path1 = os.path.join(favicons_dir, filename)
        with open(path1, "wb") as f:
            f.write(content)
        print(f"Saved: {path1}")

        # In static/ (for root access like /favicon.ico and search crawlers)
        path2 = os.path.join(static_dir, filename)
        with open(path2, "wb") as f:
            f.write(content)
        print(f"Saved: {path2}")

        # In public/ if public exists
        if os.path.exists(public_dir):
            path3 = os.path.join(public_favicons_dir, filename)
            with open(path3, "wb") as f:
                f.write(content)
            path4 = os.path.join(public_dir, filename)
            with open(path4, "wb") as f:
                f.write(content)

    print("All favicon assets generated successfully!")

if __name__ == "__main__":
    main()
