# pip install pyaudio
import time
import mysql.connector
# pip install setuptools 
# from bot.views import username_value   
import pywhatkit as kit
import pyautogui as pt  # mouse and keyboard control
import os
import openai
import pyttsx3   # text to speech
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib  #mail use


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)
rate = engine.setProperty("rate",200)

print(voices)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(username):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("hello!! {} how are you ".format(username))

def takeMessage():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 310
        audio = r.listen(source,0,4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vanshjain0311@gmail.com', 'iaoo wcdy ggpf cqwv')
    server.sendmail('getvanshjain11@gmail.com', to, content)
    server.close()

def work(user_name):

      query = takeMessage().lower()

      if "captain" in query:
        datetime_value = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
        cur.execute("INSERT INTO data(username, userquery, query_datetime) VALUES('{}', '{}', '{}')".format(user_name, query, datetime_value))    
        query = query.replace("captain" , "").strip()
        print(query)
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                # print(results)
                speak(results)
            except:
                speak("Sorry I get what you are trying to search on wikipedia")

        elif "youtube" in query:
            # speak("This is what I found for your search!") 
            query = query.replace("youtube search","")
            query = query.replace("youtube","")
            web  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            # kit.playonyt(query)
        
        elif "home" in query:
            pt.hotkey("win", "d")

        elif "just" in query:
            query = query.replace("just" , "")
            pt.write(query)

        elif 'scroll' in query:
            pt.scroll(100, 100)

        elif 'open' in query:
            name = query.replace("open" , "").strip()
            webbrowser.open(f"{name}.com")

        elif 'play' in query:
            song = query.replace("play", "")
            pt.press("home")
            kit.playonyt(song)

        elif ('hold' in query ) or ("continue" in query):
               pt.press("k")

        elif ('out' in query) : 
            return 'out'
            
            
        elif "screenshot" in query:
            image = pt.screenshot()
            image.save('ss.jpg') 
            speak('taken')
        
            
        elif "now" in query:   #EASY METHOD
                    query = query.replace("now","")
                    pt.press("super")
                    pt.typewrite(query)
                    pt.press("enter")
                    
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M %p")
            speak("{}, the time is {}".format(user_name ,strTime))

        elif 'open code' in query:
            codePath = "D:\CAPTAIN_PROJECT\PROJECTS\Captain.py"
            os.startfile(codePath)

        elif 'speak' in query:
            query = query.replace("speak ", "")
            speak(query)
            
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeMessage().lower()
                to = "vanshjain0311@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry '{}' . I am not able to send this email".format(user_name))
                
                
        elif 'shutdown' in query:
                try:
                    speak("say continue to shutdown ?")
                    content = takeMessage().lower()
                    if content == 'continue':
                        speak("proceeding to shutdown in 3!!! 2!!! 1!!!")
                        os.system('shutdown /s /t 2')
                    else:
                        speak('okay!!')
                except Exception as e:
                    print(e)
                    speak("Sorry '{}'. I am not able to shutdown right now".format(user_name))
                    
                    
        elif 'restart' in query:
                try:
                    speak("say continue to restart ?")
                    content = takeMessage().lower()
                    if content == 'continue':
                        speak("proceeding to restart in 3!!! 2!!! 1!!!")
                        os.system('shutdown /r /t 2')
                    else:
                        speak('okay!!')
                except Exception as e:
                    print(e)
                    speak("Sorry '{}'. I am not able to restart right now".format(user_name))
        else:
            print("No query matched")


def start_program(username_value):
    speak("Initializing CAPTAIN")
    user = username_value
    wishMe(user)
    while True:
        a = work(user)
        
        if(a == 'out'):
            print("Exiting Program..")
            speak("!!!!Exiting Program..")
            break
        
username_value = "Vansh"

mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345678',
    database = 'captaindb'
)

cur = mycon.cursor()
mycon.autocommit = True

if(mycon.is_connected):
    print('connected successfully')
    # fetch latest user name
    cur.execute('select username from users order by id desc limit 1')
    username_value = cur.fetchall()[0][0]
    print(username_value)


start_program(username_value)# text