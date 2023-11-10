from time import sleep
import os,cv2
from PIL import Image, ImageGrab
import pyperclip
import pyautogui as pt
import pyscreenshot
import pytesseract
import configparser

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def leer_mensaje():
	img = cv2.imread('imagenes/nombre.png')
	img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
	img = cv2.medianBlur(img,1)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
	dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
	contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	mensaje = ''

	for cnt in contours[::-1]:
		x, y, w, h = cv2.boundingRect(cnt)
		cropped = thresh1[y:y + h, x:x + w]
		#config = ('--oem 1 --psm 6')				#Activar para cualquier idioma
		config = ('-l spa --oem 1 --psm 6')		#Activar sólo para español
		text = pytesseract.image_to_string(cropped, config=config)
		text = text.replace('\n',' ')
		mensaje += text

	if mensaje != '':
		print(mensaje)
		pyperclip.copy(mensaje)
		sleep(1)
leer_mensaje()