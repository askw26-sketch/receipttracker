import pytesseract
from PIL import Image

def process_image(image_path):
    try:
        # Load the image from the provided path
        image = Image.open(image_path)
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)

# Example usage:
# result = process_image('path_to_image.jpg')
# print(result)
