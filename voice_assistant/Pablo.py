import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time
import requests
import pyjokes
import subprocess
import re
from word2number import w2n

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

app_paths = {
"chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
"spotify": "C:\\Users\\Abdoe\\AppData\\Roaming\\Spotify\\Spotify.exe",
"notion": "C:\\Users\\abdoe\\AppData\\Local\\Programs\\Notion\\Notion.exe"
}

# Speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen for voice input and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Speech service is unavailable.")
        return ""

#listens for the wake word "Pablo"
def listen_for_wake_word():
    while True:
        with sr.Microphone() as source:
            print("Waiting for wake word...")
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio).lower()
                print("You said:", command)
                if "pablo" in command:
                    speak("Yes?")
                    return  # Exit when wake word is detected
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                speak("Speech service unavailable.")
                break

# for multiple listen trie
def retry_listen(max_attempts=3):
    for attempt in range(max_attempts):
        response = listen()
        if response:
            return response
        elif attempt < max_attempts - 1:
            speak("Can you please repeat that?")
    speak("Sorry, I couldn't understand.")
    return ""

# Open specific applications based on the command
def open_app(app_name):
    """if "chrome" in app_name:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "spotify" in app_name:
        os.startfile("C:\\Users\\Abdoe\\AppData\\Roaming\\Spotify\\Spotify.exe")
    elif "notion" in app_name:
        os.startfile("C:\\Users\\abdoe\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs")"""
    for name in app_paths:
        if name in app_name:
            path = app_paths[name]
            webbrowser.open(path) if path.startswith("http") else os.startfile(path)
            return
    speak(f"Sorry, I can't find {app_name} on this system.")

#set timers
def set_alarm(seconds):
    speak(f"Timer set for {seconds // 60} minutes from now.")
    time.sleep(seconds)
    speak("Time's up!")

#get weather information
def get_weather(city="Cairo"):
    api_key = "076a726bbccd40b172eb3622dff00a38"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        speak(f"The weather in {city} is {temp} degrees Celsius.")
    else:
        speak("Couldn't fetch weather data.")

# google search
def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the results for {query}")

#tell random jokes
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

# play asked Youtube videos
def play_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    speak(f"Playing {query} on YouTube")

def extract_minutes(text):
    matches = re.findall(r'\d+', text)
    if matches:
        return int(matches[0])
    return None

# Handle voice commands
def handle_command(command):
    if "your name" in command:
        speak("My name is Pablo. Nice to meet you.")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "what time is it" in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}.")
    elif "thank you" in command:
        speak("You're welcome!")
    elif "open" in command:
        app = command.replace("open", "").strip()
        speak(f"Opening {app}.")
        open_app(app)
    elif "open spotify" in command:
        speak("Opening Spotify.")
        open_app("spotify")
    elif "set" and  "timer" in command:
        k = 0
        while (k < 4):
            speak("For how many minutes?")
            minutes_str = retry_listen()
            try:
                #minutes = int(''.join(filter(str.isdigit, minutes_str)))
                minutes = extract_minutes(minutes_str)
                #speak(f"Setting timer for {minutes} minutes.")
                speak(f"Do you want me to set a timer for {minutes} minutes?")
                confirmation = retry_listen()
                if "yes" in confirmation:
                    set_alarm(minutes * 60)
                    break
                elif "no" in confirmation.lower():
                    speak("Okay, let's try again.")
                    k+=1
            except ValueError:
                speak("Sorry, I couldn't understand the number of minutes.")
                k+=1
    elif "weather" in command:
        speak("Which city's weather would you like to know?")
        city = retry_listen()
        speak(f"Getting weather for {city}.")
        if city:
            get_weather(city)
        else:
            get_weather()
    elif "search for" in command:
        search_query = command.split("search for")[-1]
        google_search(search_query)
    elif "search" in command and "youtube" in command:
        video = command.replace("play", "").replace("on youtube", "").strip()
        play_youtube(video)
    elif "joke" in command:
        tell_joke()
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I don't understand that yet.")

# Main loop
if __name__ == "__main__":
    speak("Hello, I am Pablo your voice assistant. How can I help you today?")
    while True:
        listen_for_wake_word()

        command = retry_listen()
        if command:
            handle_command(command)
