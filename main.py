# importing the libraries
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def voice_output(source):
    engine.say(source)
    engine.runAndWait()

def greet():
    timeInHour = int(datetime.datetime.now().hour)
    if 0 <= timeInHour < 12:
        voice_output("Good morning")
    elif 12 <= timeInHour < 17:
        voice_output("Good afternoon")
    elif 17 <= timeInHour < 22:
        voice_output("Good evening")
    else:
        voice_output("Good night! You should sleep")

    voice_output("I am your virtual assistant. Let me know how may I help you.")

def takeCommand():
    listening = sr.Recognizer()
    with sr.Microphone() as source:
        voice_output("Hi! I am listening...")
        listening.pause_threshold = 1
        audio = listening.listen(source)

        try:
            voice_output("Recognising...")
            query = listening.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            # voice_output("Say that again")
            return "Nothing"

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result_div = soup.find_all(class_='BNeawe')
    if result_div:
        return result_div[0].get_text()
    else:
        return "No results found."
    
def bing_search(query):
    search_url = f"https://www.bing.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result_div = soup.find_all(class_='b_algo')
    if result_div:
        return result_div[0].get_text()
    else:
        return "No results found."

def callByname():
        query = takeCommand().lower()
        if 'wikipedia' in query:
            voice_output("Wait Sagar, I am searching.")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            voice_output("According to Wikipedia,")
            voice_output(result)

        elif 'open youtube' in query:
            voice_output("Opening YouTube in your web browser")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            voice_output("Opening Google in your web browser")
            webbrowser.open("https://www.google.com/")

        elif 'open github' in query:
            voice_output("Opening GitHub in your web browser")
            webbrowser.open("https://github.com")

        elif 'open youtube' in query:
            voice_output("Opening YouTube in your web browser")
            webbrowser.open("https://www.youtube.com/")

        elif 'open canva' in query:
            voice_output("Opening YouTube in your web browser")
            webbrowser.open("https://www.canva.com/")
        
        elif 'google search' in query:
            query = query.replace("google search", "")
            voice_output("Searching on Google...")
            result = google_search(query)
            voice_output("Here is the search result:")
            voice_output(result)

        elif 'being search' in query:
            query = query.replace("bing search", "")
            voice_output("Searching on bing...")
            result = google_search(query)
            voice_output("Here is the search result:")
            voice_output(result)

        elif 'exit please' in query:
            voice_output("Thank you for chatting with me. Have a nice day.")
            exit(1)
            
        elif 'weather' in query:
            search_url = f"https://www.google.com/search?q={query}"
            response = requests.get(search_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            weather_div = soup.find(class_="wob_t")
            if weather_div:
                voice_output(weather_div.text)

        elif 'what' in query:
            query = query.replace("google search", "")
            voice_output("Searching on Google...")
            result = google_search(query)
            voice_output("Here is the search result:")
            voice_output(result)

        else:
            voice_output("Can you please say that again?")

def continiousAudio():
    while True:
        listening = sr.Recognizer()
        with sr.Microphone() as source:
            listening.pause_threshold = 0.5
            audio = listening.listen(source)
            try:
                print("I am ready to listen...")
                query = listening.recognize_google(audio, language='en-in')
                query = query.lower()  # Convert query to lowercase
                if 'alexa' in query:
                    callByname()
                else:
                    break  
            except Exception as e:
                break  




if __name__ == "__main__":
    greet()
    while True:
        continiousAudio()
        
