import pytesseract
from PIL import Image

# Set the correct path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load an image (make sure this image is also in the same folder)
img = Image.open("wf.png")

# Run OCR
text = pytesseract.image_to_string(img)
print("Extracted text:")
print(text)
