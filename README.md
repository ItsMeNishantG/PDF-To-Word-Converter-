# PDF-To-Word-Converter-

PDF To Word Converter Using Python 

A lightweight, efficient Python utility to **convert PDF documents into fully editable Microsoft Word (`.docx`) files**. This tool automatically extracts layouts, text, fonts, images, and tables from digital PDFs and reconstructs them seamlessly into Word format using the `pdf2docx` library.

## 🚀 Quick Start

### 1. Installation
Install the required dependency via `pip`:
```bash
pip install pdf2docx
```

### 2. Usage
1. Place the PDF file you wish to convert into your project directory.
2. Update the `pdf_file` path in the script to match your filename.
3. Run the script:

```python
from pdf2docx import Converter

# 1. Define file paths
pdf_file = "sample.pdf"
docx_file = "output.docx"

# 2. Initialize the converter
cv = Converter(pdf_file)

# 3. Convert all pages of the PDF to Word (start=0, end=None parses everything)
cv.convert(docx_file, start=0, end=None)

# 4. Close the converter instance
cv.close()

print(f"Conversion complete! Saved as {docx_file}")
```

---

## ⚙️ Advanced Usage

### Convert Specific Pages
If you only need a portion of your document, you can target specific pages or ranges to save time and memory.

* **Target a specific range:**
  ```python
  # Converts from page 2 up to page 5 (Note: 0-indexed)
  cv.convert(docx_file, start=1, end=5)
  ```

* **Target isolated pages:**
  ```python
  # Converts only page 1, page 3, and page 8
  cv.convert(docx_file, pages=[0, 2, 7])
  ```

---

## 📄 Supported PDF Types

* **Supported ✅**
  * **Native/Digital PDFs:** Documents generated directly out of software like Microsoft Word, Google Docs, Adobe InDesign, or exported from web browsers. Text, structural elements, and tables will be fully editable in the resulting Word document.
  
* **Not Fully Supported ❌**
  * **Scanned PDFs & Images:** Documents created via physical paper scanners or camera photographs. Because there is no underlying digital text layer, the converter will paste the pages as static, uneditable images inside the Word file instead of generating text fonts.

---

## ⚠️ Important Cautions & Limitations

### 1. Complex Visual Layouts
* **The Issue:** Highly intricate graphic designs, dense multi-column scientific templates, overlapping shapes, or complex floating elements might experience slight formatting shifts or alignment errors during translation.
* **The Fix:** Review the output document in Microsoft Word to manually adjust margins or shapes if a visual element shifts out of bounds.

### 2. Tabular Data Boundaries
* **The Issue:** While `pdf2docx` is outstanding at rebuilding standard grids, custom tables lacking explicit borders or containing deeply nested cells might occasionally split into separate paragraphs or broken lines.

### 3. File Permissions
* **The Issue:** If a PDF is restricted, encrypted, or password-protected, the script will throw an authentication error and fail to open.
* **The Fix:** Ensure all target files are unlocked or decrypted before initiating conversion.

---

## 🛠️ Requirements
* Python 3.8 or higher
* `pdf2docx` package

---

## 📜 License
This project is open-source software. It is completely free and available for personal use.
