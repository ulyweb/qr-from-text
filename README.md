# QR Web App

A fast, offline-capable, and fully client-side QR code generator and scanner. Built as a single-file static web application, it requires no build steps, no backend servers, and respects your privacy by processing everything directly in your browser.

Perfect for hosting on GitHub Pages or dropping onto any static file server.

## ✨ Features

### Generation & Customization
* **Text to QR:** Instantly convert text, URLs, or data into high-quality QR codes.
* **Format Support:** Export as `PNG` (raster) or `SVG` (vector) for print and design workflows.
* **Payload Templates:** Quickly generate formatted codes for Wi-Fi networks, vCards (contacts), mailto links, and geographic coordinates.
* **Visual Customization:** Change foreground and background colors, adjust margins and scale, and overlay a custom center logo (PNG mode).
* **Batch Mode:** Paste a list of items (one per line) to generate dozens of QR codes at once and download them in a single `.zip` file.

### Decoding & Scanning
* **Camera Scanner:** Scan QR codes directly using your device's webcam or smartphone camera.
* **Image Upload:** Extract QR code data from uploaded images.

### Productivity & Convenience
* **Local History Log:** Automatically saves your last 15 generated or decoded items to `localStorage` for quick retrieval.
* **Drag & Drop:** Drag a `.txt` file directly onto the text area to encode its contents.
* **Quick Actions:** One-click buttons to Download, Copy to Clipboard, or Share (via the native Web Share API on supported devices).
* **URL Prefill:** Use query parameters (e.g., `?text=Hello` or `?t=Hello`) to pre-fill the input and auto-generate a code.

### Tech & Privacy
* **Progressive Web App (PWA):** Installable to your home screen and works completely offline via an inline Service Worker.
* **Dark Mode:** Fully supports system themes with a manual toggle.
* **100% Client-Side:** No data ever leaves your device. All rendering, scanning, and zipping happens in the browser.

## 🚀 Quick Start

Since the entire application is contained within a single `index.html` file, deployment is effortless.

1. Clone or download this repository.
2. Upload `index.html` to any web host (e.g., GitHub Pages, Netlify, Vercel, or a standard Apache/Nginx server).
3. Open the URL in your browser.

## 📖 How to Use

**To Generate a QR Code:**
1. Paste your text into the main text area, or select a template from the dropdown.
2. Choose your preferred output (`PNG` or `SVG`), Error Correction level, and colors.
3. (Optional) If using PNG, click "Choose File" under "Center Logo" to add your branding.
4. Click **Generate QR**.
5. Click **Download**, **Copy image**, or **Share** to distribute your code.

**To Generate in Bulk:**
1. Check the **Batch Mode** box.
2. Paste your data into the text area, ensuring there is one item per line.
3. Click **Generate QR**.
4. Click **Download ZIP** to get an archive of all your QR codes.

**To Scan a QR Code:**
* **From Camera:** Click **Scan Camera**, grant camera permissions, and point your device at a QR code. The app will automatically read the data and populate the text field.
* **From Image:** Click **Upload QR Image** and select a photo containing a QR code from your device.

## 🛠️ Built With

* [Tailwind CSS](https://tailwindcss.com/) (via CDN) - For responsive, modern styling.
* [qrcode](https://www.npmjs.com/package/qrcode) (via CDN) - For generating canvas and SVG codes.
* [jsQR](https://github.com/cozmo/jsQR) (via CDN) - For decoding images and camera streams.
* [JSZip](https://stuk.github.io/jszip/) (via CDN) - For client-side batch archiving.
