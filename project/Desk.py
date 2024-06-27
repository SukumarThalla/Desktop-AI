import speech_recognition as sr
import pyttsx3
import os
import pygame
import datetime
import webbrowser
import pyautogui 
import smtplib



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""

def play_music():
    music_path = "/home/apiiit-rkv/Desktop/maths/"  # Change this to the path of music folder
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(music_path, "01 Ik Vaari Aa - Raabta (Arijit Singh) 320Kbps.mp3")) 
    pygame.mixer.music.play()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Easy Sir. Please tell me how may I help you") 
def lock_screen():
    
    pyautogui.hotkey("win", "l")
    speak("Screen locked.")
def open_youtube():
    webbrowser.open("https://www.youtube.com")

def takeCommand():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""



def write_to_diary(entry):
   
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")

  
    diary_entry = f"{date_string}\n{entry}\n\n"

    
    with open("diary.txt", "a") as file:
        file.write(diary_entry)
    print("Diary entry written successfully.")
def get_date():
    today = datetime.datetime.today()
    date_str = today.strftime("%B %d, %Y")  # Example format: December 25, 2023
    return date_str

def get_day():
    today = datetime.datetime.today()
    day_str = today.strftime("%A")  # Example format: Monday
    return day_str

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('r180571@rguktrkv.ac.in','7403LOKI')
    server.sendmail('r180571@rguktrkv.ac.in',to, content)
    server.close()


def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if "exit" in command:
            speak("Goodbye See you again!")
            break
        elif "open notepad" in command:
            speak("Opening Notepad.")
            os.system("notepad.exe")
        elif "play music" in command:
            speak("Playing music.")
            play_music()
        elif "wish me" in command:
       	    speak("wishing you")
       	    wishMe();
       	elif "open google" in command:
            webbrowser.open("google.com")
        elif "lock screen" in command:
            lock_screen()
        elif "volume up" in command:
            volume_up()
            speak("Volume up.")
        elif "volume down" in command:
            volume_down()
            speak("Volume down.") 
        elif "open youtube" in command:
            open_youtube()
            speak("Opening YouTube.")
        elif 'email to loki' in command:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "lokeshkundlavari@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend , I am not able to send this email") 
        elif "today date" in command:
            date = get_date()
            speak(f"Today's date is {date}.")
        elif "what is today" in command:
            day = get_day()
            speak(f"Today is {day}.")
        elif "diary" in command:
            speak("What would you like to add to your diary?")
            diary_entry = listen()
            write_to_diary(diary_entry)


if __name__ == "__main__":
    main()

