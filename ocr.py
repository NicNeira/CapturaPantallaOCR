# -*- coding: utf-8 -*-
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extraer_texto(imagen):
    img = cv2.imread(imagen)
    texto = pytesseract.image_to_string(img)
    return texto
