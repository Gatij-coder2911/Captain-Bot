# pip install pyaudio
import time
import mysql.connector
# pip install setuptools 
# from bot.views import username_value   
import pywhatkit as kit
import pyautogui as pt  # mouse and keyboard control
import os
import pyjokes
from googlesearch import search
import openai
import pyttsx3   # text to speech
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib  #mail use
from newsapi import *
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)
rate = engine.setProperty("rate",200)

print(voices)

# newsapi = NewsApiClient(api_key="YOUR_API_KEY")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def set_reminder():
    speak("! ! What shall I remind you ?")
    text = takeMessage()

    speak("! ! In how many minutes? !!! !! ! ! !!! ! ! ! !")
    # local_time = takeMessage()

    # local_time = local_time.replace("captain" , "").strip()
    # print(local_time)
    # minu = int(local_time)
    # Convert minutes to seconds
    # int(local_time) = local_time * 60
    # minu *= 60
    # minut = int(input('Enter your time'))
    # Wait for the specified time
    speak('okay I will remind you')
    time.sleep(10)
    speak('i am reminding you  to "{}"'.format(text))
    # Display the reminder
    # os.system(f"osascript -e 'display notification \"{text}\" with title \"Reminder\"'")

def get_current_day():
    day_number = datetime.datetime.today().weekday() + 1
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[day_number - 1]


def get_weather(api_key, city):
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            speak(f"Weather in {city}:")
            speak(f"Description: {weather_description}")
            speak(f"Temperature: {temperature}°C")
            speak(f"Humidity: {humidity}%")
            speak(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data['message']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")




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

      if "captain " in query:
        datetime_value = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
        cur.execute("INSERT INTO data(username, userquery, query_datetime) VALUES('{}', '{}', '{}')".format(user_name, query, datetime_value))    
        query = query.replace("captain" , "").strip()
        print(query)
        if 'search' in query:
            # speak('Searching')
            query = query.replace("search ", "")
            try:
                # Perform the Google search
                # search_results = search(query, num=5, stop=5, pause=2)

                # # Print the search results
                # for i, result in enumerate(search_results, start=1):
                #     print(f"{i}. {result}")
                results = wikipedia.summary(query, sentences=1)
                # results = openai.Completion.create(query , sentence=1)
                # results = search(query, pause=2)
                speak("According to google")
                print(results)
                speak(results)
            except:
                speak("Sorry I get what you are trying to search on google")
             
             
        elif ('remind me' in query  or 'set a reminder' in query):
            set_reminder()
            # speak('okay I will remind you')
            
                
        elif "tell me a joke" in query:
            speak(pyjokes.get_joke())
           
        elif "day" in query:
            current_day = get_current_day()
            speak(f"!!! The day is {current_day}")

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

        elif ('hold' in query ) or ("stop" in query):
               pt.press("k")
               
        elif ('start' in query ) or ("resume" in query):
               pt.press("k")

        elif ('continue' in query) : 
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
        elif 'weather' in query:
            # Provide your OpenWeatherMap API key here
            api_key = '0e7565793df0658d7e5c8c8c4bfcc109'

            # Specify the city for which you want to get weather information
            city = 'Bhopal'

            # Call the function to get weather data
            get_weather(api_key, city)
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
            speak("proceeding to Exit in 3!!! 2!!! 1!!!")
            # speak("!!!!Exiting Program..")
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

# fetch user name from database
if(mycon.is_connected):
    print('connected successfully')
    # fetch latest user name
    cur.execute('select username from users order by id desc limit 1')
    username_value = cur.fetchall()[0][0]
    print(username_value)


start_program(username_value)# text