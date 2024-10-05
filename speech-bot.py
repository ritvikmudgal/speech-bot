import speech_recognition as sr
import os
import webbrowser
import datetime
import random as r
import cv2
a=r.randint(10,30)
def say(text):
    os.system(f"say {text}")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Can You be a little more clear"

if __name__ == '__main__':
    say("Your personal A I here")
    while True:
        print('listening')
        query = takecommand()
        sites=[["Youtube","https://www.youtube.com/feed/subscriptions"],["Pintrest","https.pintrest.com"],["Google","https://www.google.com/"],["snapchat","https://web.snapchat.com/"],["Github","https://github.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Boss..")
                webbrowser.open(site[1])
        if 'thank'.lower() in query.lower():
            say('My pleasure Boss')
        if 'Hello'.lower() in query.lower():
            say('Hello Boss')
        if "time" in query:
            hours = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Boss, The Time is {hours} hours and {min}minutes")
        Apps = [["Spotify", "/Applications/Spotify.app"], ["chrome", "/Applications/Google Chrome 2.app"],["Anime", "/Applications/AnimeSuge.app"], ["pycharm", "/Applications/PyCharm CE.app"]]
        for App in Apps:
            if f"open {App[0]}".lower() in query.lower():
                say(f"opening {App[0]} Boss")
                os.system(f"open {App[1]}")
        if "finish" in query:
            say("Bye Boss, ")
            break;
        if "camera" in query:
            say("opening Camera Boss")
            cam = cv2.VideoCapture(0)
            while True:
                ret, img= cam.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(10)
                if k==27:
                    break;
            cam.release()
            cv2.destroyAllWindows()