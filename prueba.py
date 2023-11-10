from time import sleep
import os,cv2
from PIL import Image, ImageGrab
import pyperclip
import pyautogui as pt
import pyscreenshot
import pytesseract
import configparser
pt.displayMousePosition()


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# os.system("start WhatsApp:")
# pct_x = pt.size()[0]/ImageGrab.grab().size[0]
# pct_y = pt.size()[1]/ImageGrab.grab().size[1]


# def esaudio():
# 	while True:
# 		posicion = pt.locateCenterOnScreen('imagenes/audio.png', region=(592,869,50,70), grayscale=False, confidence=.9)
# 		if posicion is not None:
# 			print("Es un audio")
# 			sleep(1)
# 		else:
# 			print("No es un audio")
# 			sleep(1)
# esaudio()
