import mysql.connector
# pip install setuptools 
# from bot.views import username_value   
import pywhatkit as kit
import pyautogui as pt  # mouse and keyboard control
import os
import pyttsx3   # text to speech
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib  #mail use
import threading
import time
import requests

def reminder_speak(remind_audio):
    remind_engine = pyttsx3.init('sapi5')
    remind_voices = remind_engine.getProperty('voices')
    remind_engine.setProperty('voice', remind_voices[0].id)
    remind_rate = remind_engine.setProperty("rate",200)

    remind_engine.say(remind_audio)
    remind_engine.runAndWait()
    remind_engine.stop()


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.setProperty("rate",200)
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

        # elif 'open code' in query:
        #     codePath = "D:\CAPTAIN_PROJECT\PROJECTS\Captain.py"
        #     os.startfile(codePath)

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
                        os.system('shutdown /s /t 1')
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
        # This functionality will work for input like ("captain remind me at 9:45 PM")
        elif 'remind me' in query:
            
            time_extracted=extract_time(query)
            print(time_extracted)
            speak("What should I remind you?")
            reminder_text=takeMessage().lower()
            
            if time_extracted and reminder_text!="none":
                set_reminder(time_extracted, reminder_text)
                
            else:
                speak("Sorry, I couldn't understand the time for the reminder.")

        elif 'weather' in query:
            # Provide your OpenWeatherMap API key here
            api_key = '0e7565793df0658d7e5c8c8c4bfcc109'

            # Specify the city for which you want to get weather information
            city = 'Bhopal'

            # Call the function to get weather data
            get_weather(api_key, city)
        else:
            print("No query matched")

# Global reminder thread
reminder_thread = None

def set_reminder(alarm_time, reminder_text):
    now = datetime.datetime.now()
    print("Alarm time :", alarm_time)
    print("Current Time :", now)
    if alarm_time > now:
        delta = (alarm_time - now).total_seconds()
        print("Difference :", delta)
        speak("The Alarm has been set for {}".format(alarm_time.strftime("%I:%M %p")))
        # This will execute remind() function after waiting for delta seconds in a seperate Thread
        global reminder_thread
        reminder_thread = threading.Timer(delta, remind, args=(reminder_text,))
        reminder_thread.start()
    else:
        speak("Alarm time has already passed.")

def remind(reminder_text):
    reminder_speak(f"Reminder: {reminder_text}")

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
            speak(f"Wind Speed: {wind_speed} meters per second")
        else: 
            speak(f"Error: {data['message']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_time(text):
  """Extracts the hour and minute from a time string in 24-hour format with optional meridian indicator (AM/PM) and returns a datetime object.

  Args:
      text: The text string containing the time information.

  Returns:
      A datetime object representing the extracted time or None if no valid time is found.
  """
  words = text.lower().split()  # Convert to lowercase and split into words
  time_str = None

  # Check for presence of "at" or "in" before the time
  if "at" in words or "in" in words:
    time_index = words.index("at") if "at" in words else words.index("in")
    # Assuming the time follows "at" or "in"
    if time_index + 1 < len(words):
      time_str = words[time_index + 1]

  # Handle cases without "at" or "in" (assuming time is at the beginning)
  elif len(words) >= 2:
    # Extract hour and minute considering single-digit hours
    time_str = words[0] + (":" if len(words[0]) == 1 else "") + words[1]

  if time_str:
    try:
      # Extract hour and minute (assuming colon separator)
      hour, minute = map(int, time_str.split(":"))

      # Handle meridian indicator (PM adds 12 hours)
      if len(words) >= 3 and (words[-1] == "pm" or words[-1] == "p.m."):
        hour = (hour + 12) % 24  # Adjust for PM

      # Ensure leading zero for single-digit minutes
      minute_str = str(minute).zfill(2)  # Pad with leading zero if needed

      # Create datetime object using today's date
      today = datetime.datetime.today()
      return today.replace(hour=hour, minute=int(minute_str))
    except ValueError:
      pass  # Ignore invalid time formats

  return None  # No valid time extracted

def start_program(username_value):
    speak("Initializing CAPTAIN")
    user = username_value
    wishMe(user)
    while True:
        
        a = work(user)
        
        if(a == 'out'):
            print("Exiting Program..")
            if reminder_thread: # if the reminder thread has been created or not
                if reminder_thread.is_alive():
                    speak("Alarm is still active!")
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