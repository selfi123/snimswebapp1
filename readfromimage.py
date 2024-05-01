import cv2
import pytesseract

# Load the image
image = cv2.imread('static/.jpg')

# Define the region of interest (ROI) where the text is located
x, y, w, h = 100, 100, 300, 200  # Example coordinates and dimensions
roi = image[y:y+h, x:x+w]

# Perform OCR on the ROI
text = pytesseract.image_to_string(roi)

# Print the extracted text
print(text)
