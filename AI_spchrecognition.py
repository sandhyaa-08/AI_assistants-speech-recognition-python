import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from playsound import playsound

def wake_sound():   
    playsound(r"D:\Python AI\wake up.wav")

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

print("Voice Assistant Started...")
wake_sound()   

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = text.lower()
        print("You said:", text)
        return text
    except:
        return ""

while True:
    print("Waiting for wake word...")
    text = listen_command()   

    if "hello nexa" in text:
        speak("Yes, how can I help you?")
        break


while True:
    text = listen_command()   

    if "open notepad" in text:
        speak("Opening notepad")
        speak("notepad")

        os.system("notepad")

    if "open chrome" in text:
        speak("Opening Chrome")
        os.system("start chrome")

        os.system("chrome")

    elif text in ["exit", "stop", "quit", "close"]:
        speak("Goodbye ")
        break
