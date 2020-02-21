import speech_recognition as sr
import importlib
from pynput.keyboard import Key, Controller
import time
import os
def rec1():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:p")
        audio = r.record(source,duration=5)   

    try:
        message=r.recognize_google(audio)
        print(message.split())
        mess=message.split()
        for i in range(len(mess)):
            if(mess[i]=="open"):
                if(mess[i+1]=="YouTube" or mess[i+1]=="youtube" or mess[i+1]=="gmail" or mess[i+1]=="Gmail" ):
                    full_module_name = "webopener"
                    akrun = importlib.import_module(full_module_name)
                    akrun.webopener(mess[i+1],"")
                elif(mess[i+1][-4:]==".com"):
                    full_module_name = "webopener"
                    akrun = importlib.import_module(full_module_name)
                    akrun.webopener(mess[i+1],"s")
                else:
                    full_module_name = "app_opener"
                    akrun = importlib.import_module(full_module_name)
                    if(len(mess)==2):
                        akrun.openapp(mess[i+1])
                    elif(mess[i+2]=="for" or mess[i+2]=="For"):
                        akrun.openapp(mess[i+1])
                    else:
                        akrun.openapp(mess[i+1]+" "+mess[i+2])
                    break
            elif(mess[i]=="search" or mess[i]=="Search"):
                work=""
                for j in range(len(mess)):
                    if(mess[j]=="in"):
                        if(mess[j+1]=="YouTube" or mess[j+1]=="youtube" or mess[j+1]=="chrome" or mess[j+1]=="Chrome"):
                            full_module_name = "webopener"
                            akrun = importlib.import_module(full_module_name)
                            work=work.split()
                            s=" "
                            s = s.join(work[1:])
                            akrun.webopener(mess[j+1],s)
                    else:
                        if(mess[j]!="Search" or mess[j]!="search"):
                            work=work+" "+mess[j]
            elif(mess[i]=="play" or mess[i]=="Play"):
                work=""
                for j in range(len(mess)):
                    if(mess[j]=="in"):
                        if(mess[j+1]=="YouTube" or mess[j+1]=="youtube"):
                            full_module_name = "webopener"
                            akrun = importlib.import_module(full_module_name)
                            work=work.split()
                            s=" "
                            s = s.join(work[1:])
                            akrun.webopener(mess[j+1],s)
                    else:
                        if("in" in mess):
                            if(mess[j]!="Search" or mess[j]!="search"):
                                work=work+" "+mess[j]
                        else:
                            full_module_name = "webopener"
                            akrun = importlib.import_module(full_module_name)
                            s=" "
                            s = s.join(mess[1:])
                            akrun.webopener("YouTube",s)
            elif(mess[i]=="mail" or mess[i]=="Mail" or mess[i]=="Gmail" or mess[i]=="gmail" or mess[i]=="email" or mess[i]=="Email"):
                full_module_name = "webopener"
                akrun = importlib.import_module(full_module_name)
                akrun.webopener("gmail","")
            elif(mess[i]=="File" or mess[i]=="file"):
                print("file")
                os.system('python file.py')
            elif(mess[i]=="close"):
                print("sdfsfvsgvds")
                keyboard.press(Key.fn)
                keyboard.press(Key.alt)
                keyboard.press(Key.f4)
                keyboard.release(Key.f4)
                keyboard.release(Key.alt)
                keyboard.release(Key.fn)
                
    except:
        pass
i=-1
while(i==-1):
    rec1()
