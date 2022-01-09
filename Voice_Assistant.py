import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from wikipedia.wikipedia import random
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    
    speak("I am your Voice Assistant sir. Please tell, how i can help you")

def takeCommand():
    # It takes audio from mic and returns into string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again...")
        return "None"
    return query

def play_music():
    music_dir = "D:\\mp3"
    songs = os.listdir(music_dir)
    # print(songs)
    randNo = random.randint(0, len(songs)-1)
    num = random.randint(0, len(songs))
    # print(num)
    speak('playing music')
    os.startfile(os.path.join(music_dir, songs[num]))

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aakanshanain@gmail.com', 'merrorwethcomv')
    server.sendmail('aakanshanain@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    run = True
    while run:
        query = takeCommand().lower()
    
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('opening youtube...')
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in query:
            speak('opening stackoverflow website...')
            webbrowser.open('stackoverflow.com')

        elif 'open mdu website' in query:
            speak('opening mdu website...')
            webbrowser.open('mdu.ac.in')

        elif 'open mdu website' in query:
            speak('opening w3 schools website...')
            webbrowser.open('w3schools.com')

        elif 'play music' in query:
            play_music()

        elif 'open programs folder' in query:
            m_dir = "D:\\Programming"
            speak('opening folder')
            os.startfile(m_dir)
        
        elif 'open Web development' in query:
            m_dir = "D:\\Web Development"
            speak('opening folder')
            os.startfile(m_dir)
        
        elif 'open downloads folder' in query:
            m_dir = "C:\\Users\\Deepak Verma\\Downloads"
            speak('opening folder')
            os.startfile(m_dir)

        elif 'open chrome' in query:
            dir = "C:\\Program Files\\Google\\Chrome\\Application"
            fil_name = "chrome.exe"
            speak('Opening chrome')
            os.startfile(os.path.join(dir, fil_name))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        
        elif 'command prompt' in query:
            dir = "C:\Windows\system32"
            fil_name = "cmd.exe"
            speak('Opening command prompt')
            os.startfile(os.path.join(dir, fil_name))
        
        elif 'open whatsapp' in query:
            dir = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2134.10.0_x64__cv1g1gvanyjgm\\app"
            fil_name = "WhatsApp.exe"
            speak('Opening whatsapp')
            os.startfile(os.path.join(dir, fil_name)) 
        
        elif 'quit' in query:
            speak('I am going to sleep, Thanks for the time, You can also call me again for help')
            run = False

        elif 'open code' in query:
            codepath = "C:\\Users\\Deepak Verma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Opening V S Code')
            os.startfile(codepath)

        elif 'open spotify' in query:
            codepath = "C:\\Users\\Deepak Verma\\AppData\\Roaming\\Spotify\\Spotify.exe"
            speak('Opening Spotify')
            os.startfile(codepath)
        
        elif 'send an email' in query:
            email_id = input('Enter Email id: ')
            try:
                speak('What should I say?')
                content = takeCommand()
                sendEmail(email_id, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif "who am i" in query:
            speak('Sir Your name is Deepak Verma, a Learner')
            speak('It is my pleasure that i am your assistant')