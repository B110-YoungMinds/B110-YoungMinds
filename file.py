import pythoncom
import pyttsx3
import shutil
import os
import sys
from os import path
import speech_recognition as sr
from pynput.keyboard import Key,Controller
from pywinauto import application
keyboard= Controller()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('What you you like to do?')
engine.runAndWait()
r = sr.Recognizer()                                                                                  
with sr.Microphone() as source:                                                                      
        print("Speak:p")
        audio = r.record(source,duration=3)
message=r.recognize_google(audio)
#work(message)
#def work():
if(message == 'Copy'or message == 'copy'):
                engine.say('Say the file name you want to copy?')
                engine.runAndWait()
                r1 = sr.Recognizer()                                                                                  
                with sr.Microphone() as source:                                                                      
                          print("Speak:p")
                          audio = r1.record(source,duration=3)
                m1=r1.recognize_google(audio)
                m1=m1+".txt"
                print(m1)
                engine.say('Say the New file name')
                engine.runAndWait()
                r2 = sr.Recognizer()                                                                                  
                with sr.Microphone() as source:                                                                      
                        print("Speak:p")
                        audio = r2.record(source,duration=3)
                m2=r2.recognize_google(audio)
                m2=m2+".txt"
                print(m2)
                shutil.copyfile(m1,m2)
elif(message == 'rename' or message == 'Rename'):
                        engine.say('Say the file name you want to rename?')
                        engine.runAndWait()
                        r3 = sr.Recognizer()                                                                                  
                        with sr.Microphone() as source:                                                                      
                                print("Speak:p")
                                audio = r3.record(source,duration=3)
                        d1=r3.recognize_google(audio)
                        d1=d1+".txt"
                        engine.say('Say the New file name')
                        engine.runAndWait()
                        r3 = sr.Recognizer()                                                                                  
                        with sr.Microphone() as source:                                                                      
                                print("Speak:p")
                                audio = r3.record(source,duration=3)
                        d2=r3.recognize_google(audio)
                        d2=d2+".txt"
                        if path.exists("guru99.txt"):
# get the path to the file in the current directory
                                src = path.realpath(d1);
# rename the original file
                #os.rename('guru99.txt','career.guru99.txt')
                        os.rename(d1,d2)
elif(message == 'Create' or message == 'create'):
                                engine.say('Say the file name you want to create?')
                                engine.runAndWait()
                                r5 = sr.Recognizer()                                                                                  
                                with sr.Microphone() as source:                                                                      
                                        print("Speak:p")
                                        audio = r5.record(source,duration=3)
                                d5=r5.recognize_google(audio)
                                d5=d5+".txt"
                                f= open(d5,"w+")
else:
        exit()
