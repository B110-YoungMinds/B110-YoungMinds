import os
import ctypes
import pythoncom
import pyttsx3
import ctypes
import time
import speech_recognition as sr
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def wo(message):
        print(message)
        if (message == 'Restart' or message=='restart'):
                engine.say('Are you sure you want to restart')
                engine.runAndWait()
                me=re()
                if(me=="yes" or me=="Yes"):
                        engine.say('Restarting your PC, sir')
                        engine.runAndWait()
                        os.system("shutdown /r /t 1")
                        
        elif (message == 'Shutdown' or message=='shutdown'):
                engine.say('Are you sure you want to shutdown')
                engine.runAndWait()
                me=re()
                if(me=="yes" or me=="Yes"):
                        engine.say('Shutting down your PC, sir')
                        engine.runAndWait() 
                        os.system("shutdown /s /t 1")
        elif(message == "Lock" or message == "lock"):
                        engine.say('Are you sure you want to lock')
                        engine.runAndWait()
                        me=re()
                        print()
                        if(me=="yes" or me=="Yes"):
                                engine.say('Locking your PC, sir')
                                engine.runAndWait() 
                                ctypes.windll.user32.LockWorkStation()
def re():
        r = sr.Recognizer() 
        with sr.Microphone() as source:                                                                       
                print("Speak:k")
                audio = r.record(source,duration=5)
        mess=r.recognize_google(audio)
        return mess
