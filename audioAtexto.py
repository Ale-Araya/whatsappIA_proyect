import time
import pyautogui
import speech_recognition as sr

def extract_audio_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("Texto extraído del audio:", text)
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        print("Error en la solicitud de reconocimiento de voz:", str(e))

# Llama a la función para extraer y transcribir el audio
extract_audio_and_transcribe()
