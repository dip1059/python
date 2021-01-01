import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
luna = pyttsx3.init()
# voices = luna.getProperty('voices')
luna.setProperty("rate", 170)
luna.setProperty('voice', "en-westindies+f2")


def talk(text):
    luna.say(text)
    luna.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'luna' in command or 'lona' in command:
                command = command.replace('luna', '')
                return command
            else:
                return ""
    except:
        return ""


def run_luna():
    command = take_command()
    if not command:
        return

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'say hello' in command:
        words = command.split(" ", -1)
        # name = command.replace('say hello to', '')
        name = words[len(words)-1]
        talk(f'Hello {name}, Happy new year')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:
    run_luna()
