from pynput.keyboard import Key, Controller
import time
import pyttsx3
def openapp(app):
    keyboard = Controller()
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')            
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("opening "+app)
    engine.runAndWait()
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(1)
    for char in app:
      keyboard.press(char)
      keyboard.release(char)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
