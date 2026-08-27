# 📷 Zero-Hassle Photo & Art Exhibition Directory

Welcome to your automated photo gallery directory!

## 🚀 How it works:
1. **Just drop any photo file** (`.jpg`, `.png`, `.webp`, or `.avif`) directly into this folder (`static/photos/`).
2. Hugo automatically detects the image file, generates its path (`/photos/filename`), and builds a clean title automatically!
3. **Optional Custom Metadata**: If you want to customize a photo's title, location, or camera details, open [`static/photos/photos.json`](file:///Users/huz4f/Dev/web/huz4f/static/photos/photos.json) and add your custom data:

```json
{
  "zara.jpg": {
    "title": "Zara",
    "location": "Visual Art Exhibition",
    "camera": "Art Frame"
  }
}
```

No code editing or ID setup required!
