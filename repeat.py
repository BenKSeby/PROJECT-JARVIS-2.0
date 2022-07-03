import speech_recognition as sr
import pyttsx3 as p
import sys
import time


# def first1():
#     engine = p.init()
#     r10 = sr.Recognizer()
#     with sr.Microphone() as source10:
#         r10.adjust_for_ambient_noise(source10)
#         audio10 = r10.listen(source10)
#         try:
#             instruction1 = r10.recognize_google(audio10)
#             print(instruction1)
#         except sr.UnknownValueError:
#             print("")
#         except sr.RequestError as e:
#             print("")
#         #except UnboundLocalError as e2:
#         #   print("")
#     while True:
#         try:
#             if "Jarvis" in instruction1:
#                 engine.setProperty("rate", 140)
#                 engine.say("yes sir")
#                 engine.runAndWait()
#                 from repetition import first
#                 first()
#                 # time.sleep(60)
#                 # break
#             if "shutdown" in instruction1:
#                 print("""shutting down full Jarvis""")
#                 print("SEE YA !")
#                 break
#                 #quit()
#                 #from test import terminate
#                 #terminate()
#             else:
#                 from repeat import first1
#                 return first1()
#         except:
#             pass
#             from repeat import first1
#             return first1()
instruction1 = ""
def first1():
    engine = p.init()
    global instruction1
    r10 = sr.Recognizer()
    with sr.Microphone() as source10:
        r10.adjust_for_ambient_noise(source10)
        audio10 = r10.listen(source10)
        try:
            instruction1 = r10.recognize_google(audio10)
            print(instruction1)
        except sr.UnknownValueError:
            print("err1 -- please give the instruction")
            first1()
        except sr.RequestError as e:
            print("err2 -- please give the instruction")
            first1()
        except Exception as e:
            first1()
    while True:
        if "Jarvis" in instruction1:
            engine.setProperty("rate", 140)
            engine.say("yes sir")
            engine.runAndWait()
            from repetition import first
            return first()
        else:
            pass
            first1()