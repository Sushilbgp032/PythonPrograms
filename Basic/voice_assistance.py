import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognition=sr.Recognition()
    with sr.Microphone() as source:
        print("Listening...")
        recognition.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recogning...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnKnownValueError:
            print(" Not Undestand ")

sptext()


