import time
import getpass

USER = input("Please type your username: ")
USER.lower
#password = input("please type in your passwod: ")
password = getpass.getpass(prompt="please type in your password: ")

if USER == "ben" or "shaun" or "aaron" or "steve" or "jesus":
    password
else:
    print("wrong username")
    exit()
    
if password == "jarvis":
    time.sleep(3)
    print("hello " + USER + ",welcome to jarvis your personal AI assistant")
    time.sleep(5)
    print("Intializing face recognition")
    time.sleep(7)
    #from jarvis import initial_conversation
    #initial_conversation()
    from lock import locking
    locking()
else:
    print("wrong password")
    exit()