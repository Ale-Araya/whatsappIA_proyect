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

name="Brenda"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
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
def nombres():
    posicion = list(pt.locateAllOnScreen('imagenes/slots.png', grayscale=False, confidence=.9))
    posiciones_guardadas = []
    for i, posicion in enumerate(posicion):
        x, y, _, _= posicion  
        posiciones_guardadas.append((x, y))
    for i, (x, y) in enumerate(posiciones_guardadas):
        pt.moveTo(x + 20, y + 15)
        sleep(0.5)
        iml = pt.screenshot(region=(x+25,y,210,30))
        iml.save(r"C:\Users\Usuario\Desktop\pruebas de bots py\PizzaCrespo\imagenes\imagetoimage.png")
        slotnombre=leer_slotname()
        print(slotnombre)
        match = re.search(fr'{re.escape(name)}', slotnombre)
        if match:
            print(f'verdadero aca aparece:{name},caracteres')
            print(f'verdadero aca aparece:{slotnombre},caracteres')
            pt.click(x,y)
            break
    else:
        print(f'falso:aca no aparece :{name},caracteres')
        print(f'falso aca no aparece:{slotnombre},caracteres')
        pt.click(133,178)
                
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
nombres()