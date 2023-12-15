from googletrans import Translator
from PIL import Image 
import pytesseract  
import pathlib

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"