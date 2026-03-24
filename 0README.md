# QR from Text

A tiny, client-only web app to convert any text into a QR code (PNG or SVG).  
Runs entirely in the browser. No server. Great for Windows/macOS/Linux/iOS/Android.

**Live:** https://ulyweb.github.io/qr-from-text

## Features
- Paste any text (URLs, JSON, Wi‑Fi strings, vCard, anything)
- PNG (canvas) or SVG (vector) output
- Download, copy-to-clipboard (image), and mobile Share support
- Error correction levels L/M/Q/H, adjustable margin and scale
- Foreground/background color control
- Remembers your preferences locally
- Works offline after first load (via browser cache)

## Usage
1. Open the app.
2. Paste your text and click **Generate QR**.
3. **Download** or **Copy image** or **Share…**.

Tip: Add `?text=YOUR_TEXT` to the URL for quick links.

## Development
Static only—no build or runtime needed. The app loads:
- **Tailwind (CDN)** for styling
- **qrcode (browser build via CDN)** for QR generation

If you prefer, you can pin specific CDN versions.

## License
MIT (for app code). QR library follows its own license via CDN.
