from googletrans import Translator
from PIL import Image 
import pytesseract  
import pathlib

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = ""
# ans = input("Do you want the photos to be translated into Persian?(y/n): ")

for path in pathlib.Path("Persian_picture").iterdir():
    if path.is_file():
        img = path 
        text += pytesseract.image_to_string(Image.open(img), lang="fas")
        text += 50 * "_"
        
print(text)