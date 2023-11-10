from time import sleep
import os,cv2
from PIL import Image, ImageGrab
import pyperclip
import pyautogui as pt
import pyscreenshot
import pytesseract
import configparser
import keyboard
import re

#pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract' 					#Para MacOS
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 	#Para Windows


#Ajuste del Pixel
pct_x = pt.size()[0]/ImageGrab.grab().size[0]
pct_y = pt.size()[1]/ImageGrab.grab().size[1]
inverso = int(ImageGrab.grab().size[0]/pt.size()[0])

#Abrir WhatsApp
sleep(1)
#os.system("open /Applications/WhatsApp.app") 	#Para MacOS
os.system("start WhatsApp:") 					#Para Windows10+


#Enviar Respuesta
def enviar_respuesta():
	posicion = pt.locateCenterOnScreen('imagenes/clip.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		# pt.moveTo(x + 50, y, duration=.5)
		pt.click(x + 50, y)
		#pt.hotkey("command", "v")				#Para MacOS
		pt.hotkey("ctrl", "v")					#Para Windows
		pt.typewrite("\n", interval=.01)
		sleep(1)
		pt.typewrite("\n", interval=.01)
		sleep(1)

#Decidir que responder
def buscar_respuesta(mensaje):
	respuesta=""
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
	posicion = list(pt.locateAllOnScreen('imagenes/slots.png', grayscale=False, confidence=.9))
	posiciones_guardadas = []
	for i, posicion in enumerate(posicion):
		x, y, _, _= posicion  
		posiciones_guardadas.append((x, y))
	for i, (x, y) in enumerate(posiciones_guardadas):
		pt.moveTo(x + 20, y + 15)
		sleep(0.1)
		iml = pt.screenshot(region=(x+25,y,210,30))
		iml.save(r"C:\Users\Usuario\Desktop\pruebas de bots py\PizzaCrespo\imagenes\imagetoimage.png")
		slotnombre=leer_slotname()
		name=leer_nombre()
		slotsESP=slotnombre.strip().replace(" ","")
		namesESP=name.strip().replace(" ","")
		if namesESP == slotsESP:
			pt.click(x,y)
			while True: 
				pos = pt.locateCenterOnScreen('imagenes/enviarmsj.png',grayscale=False, confidence=.9)
				if pos is not None:
					break
			pt.click(pos)
			# pt.write(f"hola soy{name}")
			pt.hotkey('ctrl', 'v')
			pt.hotkey("enter")
			while True:
				posicion = pt.locateCenterOnScreen('imagenes/volveragenerar.png', grayscale=False, confidence=.9)
				if posicion is not None:
					break  
			pt.hotkey('ctrl', 'shift', 'c')
			msg = pyperclip.paste()
			os.system("start WhatsApp:")
			respuesta=msg
			break
	else:
		pt.click(133,178)
		# pt.write(f"hola soy{name}")
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
			nombre=leer_nombre()
			keyboard.write(nombre)
			pt.press("enter")
			sleep(1)
		os.system("start WhatsApp:")
		respuesta=msg
	return respuesta
def leer_slotname(): 
        img = cv2.imread('imagenes/imagetoimage.png')       
        img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
        img = cv2.medianBlur(img,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
        dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        slotname = ''

        for cnt in contours[::-1]:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped = thresh1[y:y + h, x:x + w]
            #config = ('--oem 1 --psm 6')				#Activar para cualquier idioma
            config = ('-l spa --oem 1 --psm 6')		#Activar sólo para español
            text = pytesseract.image_to_string(cropped, config=config)
            text = text.replace('\n',' ')
            slotname += text
        if slotname != '':
            return slotname
#leer nombre
def leer_nombre():
	img = cv2.imread('imagenes/nombre.png')
	img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
	img = cv2.medianBlur(img,1)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
	dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
	contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	nombre = ''

	for cnt in contours[::-1]:
		x, y, w, h = cv2.boundingRect(cnt)
		cropped = thresh1[y:y + h, x:x + w]
		#config = ('--oem 1 --psm 6')				#Activar para cualquier idioma
		config = ('-l spa --oem 1 --psm 6')		#Activar sólo para español
		text = pytesseract.image_to_string(cropped, config=config)
		text = text.replace('\n',' ')
		nombre += text
	if nombre != '':
		return nombre
#Leer Mensaje
def leer_mensaje():
	img = cv2.imread('imagenes/texto.png')
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
		respuesta = buscar_respuesta(mensaje)
		pyperclip.copy(respuesta)
		sleep(1)
		enviar_respuesta()

#Capturar una foto del mensaje
def extraer_mensaje():
	coor_x_ini,coor_y_ini,coor_x_fin,coor_y_fin = 0,0,0,0

	posicion = pt.locateCenterOnScreen('imagenes/nuevo.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		pt.click()
		sleep(1)

	posicion = pt.locateCenterOnScreen('imagenes/clip.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		pt.moveTo(x*0.92, y*0.935, duration = .5)				#Ajustar aqui valores de x,y
		pt.click()
		coor_x_ini,coor_y_ini = int(x*0.92),int(y*0.935)		#Ajustar aqui valores de x,y
		sleep(1)

	posicion = pt.locateCenterOnScreen('imagenes/happy.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		coor_x_fin,coor_y_fin = int(x),int(y)

	if coor_x_ini !=0 and coor_y_ini !=0 and coor_x_fin!=0 and coor_y_fin!=0:
		pic = pyscreenshot.grab(bbox=(coor_x_ini*inverso, (coor_y_fin - (coor_y_ini-coor_y_fin))*inverso, coor_x_fin*inverso, coor_y_ini*inverso))
		img2 = Image.open('imagenes/black.png')
		pic.paste(img2, ((pic.size[0] - img2.size[0]),0), mask = img2)
		pic.save('imagenes/texto.png')
		sleep(1)
		posicion = pt.locateCenterOnScreen('imagenes/audio.png', region=(592,869,50,70), grayscale=False, confidence=.9)
		if posicion is not None:
			keyboard.write("por el momento no puedo leer audios, podrías enviarme un mensaje escrito por favor?")
			keyboard.press("enter")
		else:
			leer_mensaje()
	else:
		print('Oh Oh tenemos algún problema')

#Buscar nuevos mensajes
def buscar_nuevo_mensaje():
	posicion = pt.locateCenterOnScreen('imagenes/circulo.png',region=(81,190,430,800), grayscale=False, confidence=.8)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		sleep(1)
		pt.moveTo(x-340,y-45, duration=.05)
		# pt.click()
		iml = pt.screenshot(region=(x-340,y-45,282,35))
		iml.save(r"C:\Users\Usuario\Desktop\pruebas de bots py\PizzaCrespo\imagenes\nombre.png")
		sleep(1)
		pt.click()
		extraer_mensaje()
	else:
		sleep(1)
		posicion = pt.locateCenterOnScreen('imagenes/inicio.png', grayscale=False, confidence=.9)
		if posicion is not None:
			x = int(posicion[0])*pct_x
			y = int(posicion[1])*pct_y
			pt.moveTo(x-50,y, duration=.05)
			pt.click()
		# print('No hay nuevos mensajes')

while True:
	sleep(1)
	buscar_nuevo_mensaje()