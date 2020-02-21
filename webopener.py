import speech_recognition as sr
import time
import webbrowser
import importlib
import pyttsx3

def webopener(app,work):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')            
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    if(work=="s"):
        webbrowser.get(chrome_path).open(app)
    elif(work==""):
        app=app+".com"
        webbrowser.get(chrome_path).open(app)
        if(app=="YouTube.com"):
            full_module_name = "youtube_control"
            akrun = importlib.import_module(full_module_name)
            engine.say("Tell the number of the link")
            engine.say("I repeat Tell the number of the link")
            engine.runAndWait()
            akrun.startcont()
        else:
            print("email")
    else:
        if(app=="YouTube"):
            full_module_name = "youtube_control"
            akrun = importlib.import_module(full_module_name)
            webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query="+work)
            engine.say("Tell the number of the link")
            engine.say("I repeat Tell the number of the link")
            engine.runAndWait()
            akrun.startcont()
        elif(app=="Chrome" or app=="chrome"):
            webbrowser.get(chrome_path).open("https://www.google.com/search?q="+work)
