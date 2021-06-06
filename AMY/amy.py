import pyttsx3
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
import wikipedia
import random
import time
import datetime
from ecapture import ecapture as ec




engine = pyttsx3.init('sapi5')          #sapi5 is a speech Application Programming Interface(API) developed by Microsoft
voices = engine.getProperty('voices')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")    #you can you other voice according to your choice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Moning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("hello human , I am amy  , please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 4000

    with sr.Microphone() as source:
        # print(sr.Microphone.list_microphone_names())
        print("Listening............")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        # r.adjust_for_ambient_noise(source, duration=5)
        r.adjust_for_ambient_noise(source)

    try:
        print("Recognizing........")
        quary = r.recognize_google(audio, language='en-in')
        print(f"user said: {quary}\n")

    except Exception as e:
        # print(e)
        print("say again.....")
        return "None"
    return quary


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            try:
                speak('searching wikipedia')
                query = query.replace('wikipedia', "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
            except  wikipedia.exceptions.PageError:
                continue

        elif "thank you" in query:
            speak('You are welcome sir !')

        elif "hello" in query:
            print("hello sir")
            speak("Hello sir !")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open email" in query:
            webbrowser.open("gmail.com")
            

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
        elif 'time' in query:
            Time = datetime.datetime.now().strftime("%H: %M : %S")
            print(Time)
            speak(Time)
            
        elif 'launch' in query:
            reg_ex = re.search('launch(.*)',query)
            if reg_ex:
                    appname=reg_ex.group(1)
                    appname1=appname+".app"
                    subprocess.Popen(["open","-n","/Applications/"+appname1],stdout=subprocess.PIPE)
                    speak('I have launched the desired application')         
             
        elif 'music' in query:
            music_dir = "C:\\Users\\91774\\music"                #put the directory of music file .... in case of miltiple musics, use random module
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open cmd' in query:
            cmd_Path = "C:\\Windows\\system32\\Cmd.exe"                       #path of cmd.exe
            speak("opening cmd")
            os.startfile(cmd_Path)

        elif 'open browser' in query:
            browser_Path = "C:/Program Files/Mozilla Firefox/firefox.exe"    #path of browser
            speak("opening firefox")
            os.startfile(browser_Path)

        elif "who are you" in query:
            speak('I am Sophia. Your voice assistant . I am made of python code and developed by Girish')

        elif 'what is' in query:
            try:
                speak('searching wikipedia')
                query = query.replace('what is', "")
                results = wikipedia.summary(query, sentences=2)           #If you want more sentences, change the value of sentences
                speak("according to wikipedia")
                print(results)
                speak(results)
            finally:
                speak("cant find")

        elif 'who is' in query:
            try:
                speak('searching wikipedia')
                query = query.replace('who is', "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
            except  wikipedia.exceptions.PageError:
                continue

        elif "repeat" in query:                      #Repeat what you said
            speak('repeating')
            print('repeating..........')
            query = query.replace('repeat', "")
            print(query)
            speak(query)


        elif 'date' in query:
            date = datetime.datetime.now().strftime("%d: %m: %Y")
            print(date)
            speak(date)

        elif 'remind me' in query:
            print("What shall I remind you about?")
            print("listening........")
            x=takeCommand()
            print("In how many minutes?")
            y=takeCommand()
            print("listening........")
            local_time = float(y)
            local_time = local_time * 60
            time.sleep(local_time)
            speak("beep beep beep beep beep beep beep beep beep beep beep REMAINDER beep beep beep beep")

        
        elif "note" in query:
            query=query.replace("note","")
            new_note1=open("text_to_note.txt","x")             #text_to_note.txt will be created in current directory
            new_note1=open("text_to_note.txt","a+")  
            speak("Writing")
            print("writing.......")
            new_note1.write(query)
            new_note1.close()

        elif "show text" in query:
            f=open("text_to_note.txt","r")
            contents=f.read()
            speak("showing text file contents")
            print("showing text file contents........")
            print(contents)    
            


        elif 'bye' in query:                                 #Here I am using break statement
            speak("Good Bye sir ! ")
            break
