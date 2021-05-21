import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(year)
    speak(month)
    speak(day)

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=4 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<=16:
        speak("Good Afternoon Sir")
    elif hour >=16 and hour <=18:
        speak("Good Evening Sir")
    else :
        speak("Good Night Sir")      


    speak("It is AI Assistant developed by Punit. How can I help you?")          

def takeCommand():
    r = sr.Recognizer()   
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source) 
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio , language='en-in')
            print(query)

        except Exception as e:
            speak("unable to hear you")
            print(e)
            return "None"
        return query    

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            Date()
        elif 'wikipedia' in query:
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 3)
            print(result)
            speak(result)

        elif 'search' in query:
            speak("what should i search")    
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif 'bye' in query:
            speak("bye sir")
            quit() 
            