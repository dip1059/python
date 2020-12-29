import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty('voice', 'en-westindies+f3')
engine.say(f"Hello there")
engine.runAndWait()

r=sr.Recognizer()
with sr.Microphone() as source:
    voice = r.listen(source)
    text = r.recognize_google(voice)
    print(text)
