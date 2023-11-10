from time import sleep
import os,cv2
from PIL import Image, ImageGrab
import pyperclip
import pyautogui as pt
import pyscreenshot
import pytesseract
import configparser
import keyboard

pct_x = pt.size()[0]/ImageGrab.grab().size[0]
pct_y = pt.size()[1]/ImageGrab.grab().size[1]
mensaje="como estas?"
nombre="Brenda"
def buscar_respuesta(mensaje):
	pyperclip.copy(mensaje)
	while True: 
		pos = pt.locateCenterOnScreen('imagenes/google.png',grayscale=False, confidence=.9)
		if pos is not None:
			break
	pt.click(pos)
	while True: 
		pos = pt.locateCenterOnScreen('imagenes/chatgpt.png',grayscale=False, confidence=.9)
		if pos is not None:
			break
	pt.click(pos)
	pt.click(133,178)
	sleep(2)
	posicion = pt.locateCenterOnScreen('imagenes/nombre.png',region=(13,246,310,650), grayscale=False, confidence=.9)
	if posicion is not None:   #si nombre aparece
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.click(x,y)
		posicion = pt.locateCenterOnScreen('imagenes/enviarmsj.png', grayscale=False, confidence=.9)
		if posicion is not None:
			x = int(posicion[0])*pct_x
			y = int(posicion[1])*pct_y
			pt.click(x,y)
		pt.hotkey('ctrl', 'v')
		pt.hotkey("enter")
		while True:
			posicion = pt.locateCenterOnScreen('imagenes/volveragenerar.png', grayscale=False, confidence=.9)
			if posicion is not None:
				break  
		pt.hotkey('ctrl', 'shift', 'c')
		msg = pyperclip.paste()
		# os.system("start WhatsApp:")
		return msg
	else:    #si no aparece el nombre crea uno y lo guarda
		pt.hotkey('ctrl', 'v')
		pt.hotkey("enter")
		while True:
			posicion = pt.locateCenterOnScreen('imagenes/volveragenerar.png', grayscale=False, confidence=.9)
			if posicion is not None:
				break  
		# Realiza las acciones que deseas cuando aparece "volveragenerar.png"
		pt.hotkey('ctrl', 'shift', 'c')
		msg = pyperclip.paste()
		while True:
			posicion = pt.locateCenterOnScreen('imagenes/creanombregpt.png', grayscale=False, confidence=.9)
			if posicion is not None:
				break  # Sal del bucle si la imagen se detecta
		posicion = pt.locateCenterOnScreen('imagenes/creanombregpt.png', grayscale=False, confidence=.9)
		if posicion is not None:
			x = int(posicion[0])*pct_x
			y = int(posicion[1])*pct_y
			pt.click(x,y)
			pt.tripleClick(x-30,y)
			keyboard.write(nombre)
			pt.press("enter")
		# os.system("start WhatsApp:")
		return msg

buscar_respuesta(mensaje)



# while True: 
# 	pos = pt.locateCenterOnScreen('imagenes/nombre.png', region=(13,246,310,650),grayscale=False, confidence=.9)
# 	if pos is not None:
# 		break
# pt.click(pos, duration=0.25)
# posicion = pt.locateCenterOnScreen('imagenes/nombre.png',region=(13,246,310,650), grayscale=False, confidence=.9)
# if posicion is not None:   #si nombre aparece
# 	x = int(posicion[0])*pct_x
# 	y = int(posicion[1])*pct_y
# 	pt.click(x,y)