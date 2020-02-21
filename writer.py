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
engine.say('What you you like to do, sir?')
engine.runAndWait()
r = sr.Recognizer()                                                                                  
with sr.Microphone() as source:                                                                      
        print("Speak:p")
        audio = r.record(source,duration=3)
message=r.recognize_google(audio)
print(message)
if (message == 'open notepad' or message=='Open notepad' or message=='Open Notepad' or message=='open Notepad'):
        engine.say('Opening Notepad')
        app =  application.Application()
        app.start("Notepad.exe")
        engine.say('would you like to type in notepad?')
        engine.runAndWait()
        r2 = sr.Recognizer()                                                                                  
        with sr.Microphone() as source:                                                                      
                print("Speak:p")
                audio = r2.record(source,duration=5)
        message1=r2.recognize_google(audio)      
        for char in message1:
                keyboard.press(char)
                keyboard.release(char)
        keyboard.press(Key.ctrl)
        keyboard.press('s')
        keyboard.release(Key.ctrl)
        keyboard.release('s')
        engine.say('Say the file name')
        engine.runAndWait()
        r3 = sr.Recognizer()                                                                                  
        with sr.Microphone() as source:                                                                      
                print("Speak:p")
                audio = r3.record(source,duration=3)
        me=r3.recognize_google(audio)
        for char in me:
                keyboard.press(char)
                keyboard.release(char)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.ctrl)
        keyboard.press('s')
        keyboard.release(Key.ctrl)
        keyboard.release('s')      
else:
        exit()

