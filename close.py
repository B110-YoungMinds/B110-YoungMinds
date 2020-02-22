import os
import time
import pywinauto
import os
import ctypes
import pythoncom
import pyttsx3 
import speech_recognition as sr
from pynput.keyboard import Key,Controller
from pywinauto import application
keyboard= Controller()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('which task you want to close?')
engine.runAndWait() 
r1= sr.Recognizer()                                                                                  
with sr.Microphone() as source:                                                                      
        print("Speak:p")
        audio = r1.record(source,duration=3)
m=r1.recognize_google(audio)
print(m)
m = m+".exe"
engine.say('Closing'+m)
engine.runAndWait()
os.system("TASKKILL /F /IM "+m)
time.sleep(10)
