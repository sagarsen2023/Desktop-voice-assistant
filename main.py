# importing the libraries
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bardapi import Bard
import os
import re
import random
import subprocess
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def generate_summary(text, num_sentences=3):
    sentences = sent_tokenize(text) # Tokenizing the text into sentences
    # Calculating the term frequency of each word in the text
    word_frequencies = {}
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        for token in tokens:
            token = token.lower()
            if token not in stopwords.words('english'):
                if token not in word_frequencies:
                    word_frequencies[token] = 1
                else:
                    word_frequencies[token] += 1

    # Calculating the sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        sentence_score = 0
        tokens = word_tokenize(sentence)
        for token in tokens:
            token = token.lower()
            if token in word_frequencies:
                sentence_score += word_frequencies[token]
        sentence_scores[sentence] = sentence_score
    # Sorting the sentences by their scores
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    # Generating the summary by selecting the top sentences
    summary = ""
    num_sentences = min(len(sorted_sentences), num_sentences)  # Choose the specified number of sentences as the summary
    for i in range(num_sentences):
        summary += sorted_sentences[i][0] + " "
    # Removing asterisks and other unwanted characters
    summary = re.sub(r'\*+', '', summary)
    summary = summary.strip()
    return summary

# Function to get the operating system
def get_operating_system():
    platform = sys.platform.lower()
    if "win" in platform:
        return "Windows"
    elif "darwin" in platform:
        return "macOS"
    elif "linux" in platform:
        return "Linux"
    else:
        return "Unknown"

# Creating the voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# The Bard API
# os.environ["_BARD_API_KEY"] = "YOUR_BARD_API_KEY"  #Enter your BARD API key here. Otherwise, your code will not work
# Code for the voice output
def voice_output(source):
    engine.say(source)
    engine.runAndWait()

# The block of code which will run on startup
def greet():
    timeInHour = int(datetime.datetime.now().hour)
    if 0 <= timeInHour < 12:
        voice_output("Good morning")
    elif 12 <= timeInHour < 17:
        voice_output("Good afternoon")
    elif 17 <= timeInHour < 22:
        voice_output("Good evening")
    else:
        voice_output("You should sleep.")

# The training module
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

def callByname():
        query = takeCommand().lower()

        if re.search("open youtube|open the youtube website|can you open youtube for me|can you open the youtube website for me|can you open the website for me that is at www.youtube.com", query):
            voice_output("Opening YouTube in your web browser")
            webbrowser.open("https://www.youtube.com/")

        elif re.search("open google|open the google website|can you open google for me|can you open the google website for me|can you open the website for me that is at www.google.com", query):
            voice_output("Opening Google in your web browser")
            webbrowser.open("https://www.google.com/")

        elif re.search("open google|open the google website|can you open google for me|can you open the google website for me|can you open the website for me that is at www.github.com", query):
            voice_output("Opening GitHub in your web browser")
            webbrowser.open("https://github.com")

        elif re.search("open wikipedia|open the wikipedia website|can you open google for me|can you open the wikipedia website for me|can you open the website for me that is at www.wikipedia.com", query):
            voice_output("Opening YouTube in your web browser")
            webbrowser.open("https://www.wikipedia.com/")

        elif re.search("open amazon|open the amazon website|can you open amazon for me|can you open the amazon website for me|can you open the website for me that is at www.amazon.in", query):
            voice_output("Opening amazon in your web browser")
            webbrowser.open("https://www.amazon.in/")
        
        elif re.search("open canva|open the canva website|can you open canva for me|can you open the canva website for me|can you open the website for me that is at www.canva.com", query):
            voice_output("Opening Canva in your web browser")
            webbrowser.open("https://www.canva.com/")
        
        elif re.search("open flipkart|open the flipkart website|can you open flipkart for me|can you open the flipkart website for me|can you open the website for me that is at www.flipkart.com", query):
            voice_output("Opening flipkart in your web browser")
            webbrowser.open("https://www.flipkart.com/")

        elif re.search("play some musics|play some music|play song|play some songs|play music", query):
            musicDirectory = "D:\\Music"
            songs = os.listdir(musicDirectory)
            n = len(songs)
            x = random.randint(0, n-1)
            os.startfile(os.path.join(musicDirectory, songs[x]))

        elif re.search("pause the musics|stop the music|pause song|pause the songs|pause music|pause the music|Close the music", query):
            path = "C:\\Program Files (x86)\\Windows Media Player"
            subprocess.run(["taskkill", "/im", "wmplayer.exe", "/f"], shell=True)
            
        elif re.search("exit|exit from the program|close the program|exit please|i want to close the program", query):
            voice_output("Thank you for chatting with me. Have a nice day.")
            exit()


        else:
            text = ''''''
            detailed_text = Bard().get_answer(query)['content']
            text = detailed_text
            summarized_output = generate_summary(text, num_sentences=2)
            print(detailed_text)  # Print the detailed text first
            voice_output(summarized_output)  # Speak the summarized output
           
def continuousAudio():
    while True:
        listening = sr.Recognizer()
        with sr.Microphone() as source:
            listening.pause_threshold = 0.5  # Increase the pause threshold
            print("I am ready to listen...")
            try:
                audio = listening.listen(source, timeout=None)  # Set timeout to None to keep listening indefinitely
                query = listening.recognize_google(audio, language='en-in').lower()
                print(f"User said: {query}")
                if 'exit please' in query:
                    voice_output("Thank you for chatting with me. Have a nice day.")
                    break
                elif 'alexa' in query:
                    callByname()
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                voice_output(f"Error occurred: {e}")

if __name__ == "__main__":
    greet()
    continuousAudio()
