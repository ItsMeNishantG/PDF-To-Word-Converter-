from pdf2docx import Converter

# 1. Define the file paths
pdf_file = "sample.pdf"
docx_file = "output.docx"

# 2. Initialize the converter
cv = Converter(pdf_file)

# 3. Convert all pages of the PDF to Word
cv.convert(docx_file, start=0, end=None)

# 4. Close the converter to clear up memory
cv.close()

print(f"Conversion complete! Saved as {docx_file}")
