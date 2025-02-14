import speech_recognition as sr
import pyttsx3
import webbrowser
import music
from datetime import date


r=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listencommand(command):
    print(command)
    if (command.lower()=="open google"):
        speak("Opening google...")
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "date" in command.lower():
        today=date.today()
        print(f"Todays date is : {today}")
        speak(f"Todays date is : {today}")
    elif command.lower().startswith("play"):
        song=command.lower().split(" ")[1]
        link=music.musiclist[song]
        speak("Playing Songs...")
        webbrowser.open(link)
    elif "news" in command.lower():
        webbrowser.open("https://www.thehindu.com/news/")

if __name__=="__main__":
    speak("Nexus active")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source,timeout=2)
                output=r.recognize_google(audio)
                print(f"Output : {output}")
                if(output.lower()=="nexus"):
                    speak("what you want to ask")
                    with sr.Microphone() as source:
                        print("Ask")
                        audio=r.listen(source,timeout=2)
                        output=r.recognize_google(audio)
                        listencommand(output)
                        
        
        except Exception as e:
            print(e)
