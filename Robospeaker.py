import pyttsx3
engine = pyttsx3.init()
if __name__ == '__main__':
    print("Welcome to robospeaker 1.1. Created by Aditya ")
    while True:
        x = input("what do u want me to speak: ")
        engine.say(x)
        if x == "q":
            break
        engine.runAndWait()