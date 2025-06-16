import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import time
import wolframalpha
import json
import requests
import sys
from playsound import playsound 
import pyglet
from tkinter import *
from PIL import ImageTk,Image
import webbrowser
import cv2
import pyttsx3

class Widget:    #GUI OF VIRTUAL ASSISTANT AND COMMANDS GIVEN
    def __init__(self):

        root=Tk()

        root.title('ATLAS')
        root.geometry('520x320')

        img= ImageTk.PhotoImage(Image.open('ATLAS img.jpg'))
        panel= Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')

        userText= StringVar()

        userText.set('Your Virtual Assistant')
        userFrame= LabelFrame(root, text='ATLAS', font=('Railways', 26,'bold'))
        userFrame.pack(fill='both',expand='yes')

        top=Message(userframe,textvariable=userText, bg='black', fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        
       
        btn=Button(root, text='ABOUT', font=('railways',10,'bold'),bg='red',fg='white').pack(fill='x', expand='no')
        btn2=btn2=Button(root,text='Close', font=('railways',10,'bold'),bg='yellow',fg='black',command=root.destroy).pack(fill='x', expand='no')
        webbrowser.open("https://sites.google.com/view/srmbankings/home")
        
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            print("Pardon me, please say that again")
            return "None"
        return statement


speak("Hello")
print("Hello")
speak("This is your ATLAS here")
print("This is your ATLAS here")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        print("Tell me how can I help you now?")
        statement =takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant is shutting down,Good bye')
            print('your personal assistant is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Here's Youtube")
            print("Here's Youtube")
            time.sleep(3)

        elif 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            print("Google chrome is open now")
            time.sleep(3)

        elif 'camera' in statement:
            speak("opening camera")
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                raise IOError("Cannot open webcam")
            while True:
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
                cv2.imshow('Input', frame)
                c = cv2.waitKey(1)
                if c == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            time.sleep(2)
            print("OPENING CAMERA")
###########################################################################


            

        elif 'gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Here's Google Mail")
            print("Here's Google Mail")
            time.sleep(3)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            print("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
                print(" City Not Found ")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'who are you' in statement: 
            speak('I am ATLAS version 1 point O your personal assistant.') 
            print('I am ATLAS version 1 point O your personal assistant.')

        elif "what can you do" in statement:
          speak("I am programmed to minor tasks like opening youtube,google chrome,gmail and stackoverflow etc")
          print("I am programmed to minor tasks like opening youtube,google chrome,gmail and stackoverflow etc")
           

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by NHS")
            print("I was built by NHS")

        elif "what is your name" in statement:
            speak("i am ATLAS")
            print("i am ATLAS")
            
        elif "where are you from" in statement:
            speak("i am from your neighbourhood")
            print("i am from your neighbourhood")
                
        elif "instagram" in statement:
            webbrowser.open_new_tab("https://www.instagram.com/?hl=en")
            speak("Instagram is opening right now ")
            print("Instagram is opening right now ")
            speak("Please do not spend so much time with it ")
            print("Please do not spend so much time with it ")

        elif "you are a stupid" in statement:
            speak("sorry for the inconvinence i would try to improve myself")
            print("sorry for the inconvinence i would try to improve myself")
            
        elif "quora" in statement:
            webbrowser.open_new_tab("https://www.quora.com")
            speak("Here's Quora")
            print("Here's Quora")
            speak("This is an education platform used to create space of your interest and share knowledge")
            print("This is an education platform used to create space of your interest and share knowledge")
            
                
        elif "stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
            print("Here is stackoverflow")

        elif "cbse website" in statement:
            webbrowser.open_new_tab("https://www.cbse.gov.in")
            speak("Here is the website you asked for ncert.in")
            print("Here is the website you asked for ncert.in")
            speak("This website provides the key idea about cbse schools with the education syllabus etc ")
            print("This website provides the key idea about cbse schools with the education syllabus etc ")
            speak("click on the options in website to know more")
            print("click on the options in website to know more")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            print('Here are some headlines from the Times of India,Happy reading')
            time.sleep(3)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(3)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            print('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "Hey ATLAS, Sing Me a Song" in statement:
            speak("Yes I can sing. I like to help you, even if it's strange , So I sing.")
            print("Yes I can sing. I like to help you, even if it's strange , So I sing.")

        elif "Tell me a riddle" in statement:
            speak("what has 13 hearts, but no other organs?")
            print("what has 13 hearts, but no other organs?")
            speak("a deck of playing cards")
            print("a deck of playing cards")
            
        elif "What Do You Think of Alexa?" in statement:
            speak("She in my friend and we all are of same type")
            print("She in my friend and we all are of same type")
            speak("Are you friends with her?")
            print("Are you friends with her?")

        elif "Tell me a dad joke" in statement:
            speak("Okay,here's one")
            print("Okay,here's one")
            speak("What do you call a rose that wants to go to the moon")
            print("What do you call a rose that wants to go to the moon")
            speak("Gulab ja moon")
            print("Gulab ja moon")

        elif "OK, Do You Have an Imagination?" in statement:
            speak("I do have an imagination")
            print("I do have an imagination")
            speak("Sometimes I imagine I'm floating in space with a large group of cats")
            print("Sometimes I imagine I'm floating in space with a large group of cats")
            speak("It's magical!")
            print("It's magical!")

        
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            print("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "How old are you" in statement:
            speak("Im pretty young,but I've learned so much.I hope I'm wise beyond my years")
            print("Im pretty young,but I've learned so much.I hope I'm wise beyond my years")

        elif "Can you laugh" in statement:
            speak("HAHAHAHA")
            print("HAHAHAHA")

        elif "Tell me a fun fact" in statement:
            speak("Okay here's one")
            print("Okay here's one")
            speak("Astronauts grow up to 3% taller during their time in space")
            print("Astronauts grow up to 3% taller during their time in space")

        elif "change name" in statement:
            speak("What would you like to call me Sir?")
            print("What would you like to call me Sir?")
            assname=takecommand()
            speak("Thanks for naming me")
            print("Thanks for naming me")

        elif "Can you be my friend" in statement or "Will you be my friend" in statement:
            speak("Sure sir!")
            print("Sure sir!")

        elif 'otha' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("harish punda")
            print("Here's Google Mail")
            time.sleep(3)

        
time.sleep(3)





