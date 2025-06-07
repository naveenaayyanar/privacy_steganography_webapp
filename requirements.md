`requirements.md`
```
# Stega_Naveena Project - Requirements & Setup Guide

## Overview
Stega_Naveena is a web application designed with utmost focus on privacy and innovation, enabling users to hide and extract secret text messages within many file types using steganography. The frontend implements a clean, elegant UI following the Default Design Guidelines for modern developer-focused interfaces: light backgrounds, bold typography, spacious layouts, and minimal design with intuitive interactivity.

---

## Project Dependencies and Purpose

| Package   | Minimum Version | Purpose                                                      |
|-----------|-----------------|--------------------------------------------------------------|
| **Flask** | 2.0             | Python web framework powering backend API, routing, and template rendering |
| **Pillow**| 9.0             | Image processing library enabling steganography in images (PNG, JPEG)      |
| **Werkzeug**| 2.0           | Utility library Flask depends on; used here for secure filename handling    |

### Dependency Description
- **Flask**: Core of the backend, handles serving UI and API endpoints for file uploads, hiding and extracting messages.
- **Pillow**: Supports image manipulation required for encoding/decoding hidden text in image files.
- **Werkzeug**: Provides secure management of uploaded filenames to prevent server file path issues.

---

## Step-by-Step Setup Instructions

### 1. Clone or Obtain the Project Files
Get the project folder including:
- `app.py` (Flask backend server)
- `templates/index.html` (Frontend HTML following strict design guidelines)
- `requirements.txt`

### 2. Create and Activate Python Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

From project root (where `requirements.txt` is located):

```bash
pip install -r requirements.txt
```
*If no `requirements.txt`, manually install with:*
```bash
pip install flask pillow werkzeug
```

### 4. Run the Flask Application

Start the Flask development server:

```bash
python app.py
```

By default, the app listens on:

```
http://127.0.0.1:5000/
```

### 5. Browser Usage

- Navigate to the URL above in a modern web browser.
- Use the **Hide Text in File** section to upload supported files and embed secret messages.
- Use the **Extract Text from File** section to upload steganography-enabled files and retrieve hidden messages.
- The interface features a minimal, elegant design with clear spacing and smooth interactivity consistent with the Default Design Guidelines.

---

## UI Design Principles (from Default Design Guidelines)

- **Visual Style:**
  - Light, white backgrounds with ample whitespace.
  - Bold, elegant fonts (Poppins, weights 600-900).
  - Neutral gray (#6b7280) body text for readability.
  - Cards with subtle shadows and rounded corners (~0.75rem).
  - Minimal lines or borders; whitespace used to separate sections.
  - Simple, line-based or monochrome icons for clarity.

- **Layout:**
  - Responsive full-width layout with centered container (max width ~1200px).
  - Vertical stacking with consistent padding (e.g. top-bottom 4-6rem).
  - Grid layout for side-by-side cards on desktop, stacked on mobile.

- **Header & Navigation:**
  - Sticky top nav with left-aligned logo and right-aligned nav links.
  - Hover and focus states with smooth transitions.

- **Hero Section:**
  - Large, bold headline (~56px size).
  - Subtext explaining value proposition succinctly.
  - Large black call-to-action button with white text and subtle shadows.

- **Interactivity:**
  - Hover and active states for buttons and cards with smooth transitions.
  - Minimal and semantic HTML5 markup for accessibility.
  - Unobtrusive, lightweight JavaScript for form submission and feedback.

