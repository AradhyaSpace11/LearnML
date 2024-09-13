import requests
from PIL import Image
from io import BytesIO
import pytesseract

# Function to download the image from a URL
def get_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Example image URL
image_url = 'https://m.media-amazon.com/images/I/81IYdOV0mVL.jpg'

# Download and open the image
image = get_image_from_url(image_url)

# Use Tesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(text)