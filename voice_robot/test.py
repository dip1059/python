import pyttsx3
import speech_recognition as sr
import pyautogui
import time

# engine = pyttsx3.init()
# engine.setProperty("rate", 150)
# engine.setProperty('voice', 'en-westindies+f3')
# engine.say(f"Hello there")
# engine.runAndWait()

# r=sr.Recognizer()
# with sr.AudioFile("resources/test2.wav") as source:
#     voice = r.listen(source)
#     text = r.recognize_google(voice)
#     print(text)

text = "hello there, how r you"
words = text.split(" ", -1)
print(words)

# pyautogui.hotkey("alt", "tab")
# # time.sleep(1)
# try:
#     tab = pyautogui.locateOnScreen("resources/yout.png")
#     loc = pyautogui.center(tab)
#     pyautogui.click(loc)
# except:
#     tab = pyautogui.locateOnScreen("resources/vol.png")
#     loc = pyautogui.center(tab)
#     pyautogui.click(loc)
#     pyautogui.click(loc)
# finally:
#     print("failed")
#
# pyautogui.press("tab", 13)
# pyautogui.press("up")

