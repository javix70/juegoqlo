try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import glob
import pyautogui
import csv
import cv2 as cv
import numpy as np

height, width, channels = img.shape
print height, width, channels