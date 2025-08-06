import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"

images = convert_from_path("sample_scanned.pdf", poppler_path=poppler_path)

for i, img in enumerate(images):
    text = pytesseract.image_to_string(img)
    print(f"\n--- Page {i+1} ---\n")
    print(text)
