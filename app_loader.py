import pyautogui as py
import speech_recognition as sr
import pyttsx3 as p
import time


def apploader():
    r50 = sr.Recognizer()
    with sr.Microphone() as source50:
        r50.adjust_for_ambient_noise(source50)
        audio50 = r50.listen(source50)
        try:
            instruction5 = r50.recognize_google(audio50)
            print(instruction5)
        except sr.UnknownValueError:
            print("err1 -- please say it again")
            apploader()
        except sr.RequestError as e:
            print("err2")
            apploader()
        except Exception as e:
            print("err3 -- please say it again")
            apploader()
    try:
        py.hotkey('winleft', 's')
        time.sleep(3)
        py.typewrite(instruction5)
        time.sleep(5)
        py.press('right')
        time.sleep(2)
        py.press('enter')
        from repeat import first1
        first1()
    except:
        from repeat import first1
        first1()