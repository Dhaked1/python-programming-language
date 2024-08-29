import pyttsx3 
import speech_recognition as sr
import wikipedia
import datetime 
import webbrowser
import os


# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Function to speak the given text."""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Function to greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 17:
        speak("Good Afternoon!")    
    else:
        speak("Good Evening!")
    speak("I am Jarvis, ma'am. Please tell me how I may help you.") 
   


def takecommand():
    """Function to take command from the user and return the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return "None"
    return query
    
if __name__ == "__main__":
    wishme()
    #while True:
    if 1:    
        query = takecommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')    
        elif 'play music' in query:
            music_dir = "C:\\Users\\HP\\Music\\songs"    
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        elif 'open code' in query:
            codepath = "a\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codepath)
    