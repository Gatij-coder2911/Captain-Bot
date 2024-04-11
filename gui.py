import tkinter
import customtkinter
from PIL import Image, ImageTk, ImageSequence
import mysql.connector

# import pywhatkit as kit
import pyautogui as pt  # mouse and keyboard control
import os
# import openai
import pyttsx3   # text to speech
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib  #mail use
import threading
import psutil
import time
from CTkTable import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)
rate = engine.setProperty("rate",200)

def typewrite(sentence_list):
    print(len(sentence_list))
    wait_time=0.03
    if len(sentence_list)>=5:
        wait_time=0.03
    for sentence in sentence_list:
        # Word counter
        word_counter=0
        # Typewriter text effect
        char_str=""    
        for i in sentence:
            if i==" ":
                word_counter+=1
            if word_counter>=6:
                char_str=""
                word_counter=0
            char_str+=i
            bot_commands.configure(text=char_str)
            time.sleep(wait_time)# Typing delay
        time.sleep(0.8)# Next sentence typing delay

def speak(audio):

    words = audio.split()  # Split the sentence into words
    subsentences = []  # List to store sub-sentences
    current_subsentence = []  # Temporary list to build each sub-sentence

    for word in words:
        current_subsentence.append(word)  # Add word to current sub-sentence
        if len(current_subsentence) == 6:  # Check if sub-sentence has reached max length
            subsentences.append(" ".join(current_subsentence))  # Join words and add to list
            current_subsentence = []  # Reset for next sub-sentence

    # Append the remaining words as the last sub-sentence if any
    if current_subsentence:
        subsentences.append(" ".join(current_subsentence))

    # for sentence in subsentences:
    #     # Typewriter effect
    #     typewrite(sentence)
    #     engine.say(sentence)
    #     engine.runAndWait()
    
    typing_thread = threading.Thread(target=typewrite, args=(subsentences,))
    typing_thread.start()
    engine.say(audio)
    engine.runAndWait()
    typing_thread.join()


def wishMe(username):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello!! {} How are you ?".format(username))

def takeMessage():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        gif_button.configure(image=mic_img)
        bot_commands.configure(text="Listening...")
        user_input.configure(text="")
        app.update()
        r.pause_threshold = 1
        r.energy_threshold = 310
        audio = r.listen(source,0,4)

    try:
        print("Recognizing...")
        gif_button.configure(image=transformer_img)
        bot_commands.configure(text="Recognizing...")
        app.update()
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        user_input.configure(text=f"User said: {query}")

    except Exception as e:
        print("Say that again please...")
        bot_commands.configure(text="Say that again please...")
        user_input.configure(text="")
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
                speak("Sorry I can not get any information")

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
            # kit.playonyt(song)

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
        else:
            print("No query matched")

# def check_battery():
#     battery = psutil.sensors_battery()
#     if battery is not None:
#         plugged = battery.power_plugged
#         percent = battery.percent
#         if plugged:
#             status = "Plugged in"
#         else:
#             status = "Not plugged in"
#         print(f"Battery Status: {status}")
#         print(f"Battery Percentage: {percent}%")
#     else:
#         print("Battery information is not available.")

def start_program(username_value):
    # bot_commands.configure(text="Initializing CAPTAIN..")
    speak("Initializing CAPTAIN")
    user = username_value
    wishMe(user)
    while True:
        # app.update()
        a = work(user)
        
        if(a == 'out'):
            print("Exiting Program..")
            bot_commands.configure(text="Exiting Program..")
            speak("Exiting Program..!!")
            commands_frame.destroy()
            break

def start_thread():
    start_program(username_value) 

bot_thread=threading.Thread(target=start_thread)

# Database connection
mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'gatij',
    database = 'captain'
)

cur = mycon.cursor()
mycon.autocommit = True

# GUI
app = customtkinter.CTk()
app.geometry("500x650")
# app.resizable(0, 0)
app.title("Captain")

title_frame = customtkinter.CTkFrame(master=app)
title_frame.grid(row=0, column=0, columnspan=3, padx=17, pady=17)
title = customtkinter.CTkLabel(master=title_frame, text="C A P T A I N", font=("Candara", 60), text_color="#00bcd4")
title.grid(row=0,column=0, padx=80, pady=20)

# Function to update the displayed frame
def update_frame(num):
    frame = frames[num]
    gif_label.configure(image=frame)
    num += 1
    if num == frame_count:
        num = 0
    app.after(delay, update_frame, num)

# Open the GIF file
gif = Image.open("captain_logo.gif")

# Extract frames from the GIF
frames = [ImageTk.PhotoImage(image) for image in ImageSequence.Iterator(gif)]
frame_count = len(frames)
delay = gif.info['duration']  # Get the duration between frames

# Create a label to display the frames
gif_label = customtkinter.CTkLabel(app, text="")
gif_label.grid(row=1, column=1, pady=20)

# Images
transformer_img = tkinter.PhotoImage(file=r"./transformer.png")
mic_img = tkinter.PhotoImage(file=r"./microphone.png")

# GIF Central Button
gif_button = customtkinter.CTkButton(app, text="", width=10, height=10, image=transformer_img, fg_color="black", hover_color="#383838", corner_radius=50)
gif_button.grid(row=1, column=1, pady=20)

username_frame = customtkinter.CTkFrame(master=app, width=300, height=200)
username_frame.grid(row=2, column=1)# , pady=100
username_label = customtkinter.CTkLabel(master=username_frame, text="Username", font=("Candara", 40), text_color="#64E6EF")
username_label.pack(padx=20)
user_entry = customtkinter.CTkEntry(master=username_frame, placeholder_text="Enter your Username", height=40, width=300, font=("Consolas Bold", 20), text_color="#B4F6FB", justify="center")
user_entry.pack(padx=30, pady=10)

commands_frame = customtkinter.CTkFrame(master=app, width=50)

bot_commands=customtkinter.CTkLabel(master=commands_frame, text="bot commands", font=("Candara", 20), text_color="#64E6EF")
bot_commands.pack(pady=20)
user_input = customtkinter.CTkLabel(master=commands_frame, text="", font=("Consolas Bold", 20), text_color="#b3c7ca")
user_input.pack(pady=10)

def show_logs():
    # gif_label.destroy()
    # commands_frame.destroy()
    # log_button.destroy()

    logs = customtkinter.CTkToplevel(app)
    logs.geometry("580x500")
    logs.grab_set()

    cur.execute("SELECT userquery, query_datetime FROM data WHERE username='{}'".format(username_value))
    user_data=cur.fetchall()
    row_count=len(user_data)
    
    value_list = [["S.no.", "User Commands", "Date & Time"]]
    for i in range(len(user_data)):
        value_list.append([i+1, user_data[i][0], user_data[i][1]])

    table_frame = customtkinter.CTkScrollableFrame(master=logs)# , width=570, height=500
    table_frame.pack(expand=True, fill="both", padx=20, pady=20)

    curr_username_label = customtkinter.CTkLabel(master=table_frame, text="{} Command Logs".format(username_value), font=("Candara", 30), text_color="#64E6EF")
    curr_username_label.pack()

    table = CTkTable(master=table_frame, row=row_count+1, column=3, values=value_list, header_color="#01579B", font=("Candara", 18), height=50)
    table.pack(expand=True, fill="both", padx=20, pady=20)

log_button = customtkinter.CTkButton(master=app, text="Show Command Logs", font=("Consolas Bold", 18), height=40, fg_color="transparent", hover_color="#00BCD4", border_color="#B4F6FB", border_width=2, corner_radius=15, command=show_logs)


username_value = "Vansh"

def check_user():
    global username_value
    username_value = user_entry.get()
    if username_value=="":
        usercheck_label.configure(text="Error : Empty Username")
    else:
        if username_value.isalpha()==False:
            usercheck_label.configure(text="Error : Invalid Username")
        else:
            usercheck_label.configure(text="")
            # gif_button.configure(image=transformer_img)
            username_frame.destroy()
            commands_frame.grid(row=2, column=1)
            log_button.grid(row=3, column=1, pady=10)   
            app.update()           
            
            print(username_value)
            # Insert username into Database
            if mycon.is_connected():
                print("Connection Successfull!\n")
                # cur.execute("INSERT INTO users(username) VALUES('{}')".format(username_value))
                # start_program(username_value)
                bot_thread.start()
                # bot_thread.join()


usercheck_label = customtkinter.CTkLabel(master=username_frame, text="", font=("Consolas Bold", 16), text_color="#CF6679")
usercheck_label.pack(pady=5)

user_button = customtkinter.CTkButton(master=username_frame, text="Enter", font=("Consolas Bold", 18), height=40, fg_color="transparent", hover_color="#00BCD4", border_color="#B4F6FB", border_width=2, corner_radius=15, command=check_user)
user_button.pack(pady=10)


# Start the animation
app.after(0, update_frame, 0)


app.mainloop()