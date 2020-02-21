from pynput.mouse import Button, Controller
import speech_recognition as sr
import time

def rec(i):

    mouse = Controller()

    print('current pointer location'.format(
    mouse.position))

    if(i<=3):

        mouse.position = (340, 330+((i-1)*150))
        print('pointer moved to'.format(
        mouse.position))

        mouse.move(5, -5)

        mouse.press(Button.left)
        mouse.release(Button.left)

        mouse.click(Button.left, 2)
        
    elif(i<=6):
        
        #mouse.scroll(0,100)
        time.sleep(2)
        mouse.scroll(0,-610)
        

        mouse.move(5, -5)

        mouse.position = (340, 300+((i-4)*150))
        print('pointer moved to'.format(
        mouse.position))

        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.click(Button.left, 2)

    elif(i<=9):
        
        #mouse.scroll(0,100)
        time.sleep(2)
        mouse.scroll(0,-1220)
        

        mouse.move(5, -5)

        mouse.position = (340, 300+((i-7)*150))
        print('pointer moved to'.format(
        mouse.position))

        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.click(Button.left, 2)

    elif(i<=12):
        
        #mouse.scroll(0,100)
        time.sleep(2)
        mouse.scroll(0,-1830)
        

        mouse.move(5, -5)

        mouse.position = (340, 300+((i-10)*150))
        print('pointer moved to'.format(
        mouse.position))

        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.click(Button.left, 2)
def startcont():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:c")
        audio = r.record(source,duration=5)
    message=r.recognize_google(audio)
    i=int(message)
    print(i)
    rec(i)
#i=int(input())
#rec(i)
