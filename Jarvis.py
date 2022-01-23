import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
# Install all above modules through pip

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

    speak("I am Jarvis, an artificial intelligence named xxt2fse3gf4x654bg3fsgd2fs3fd 4, please tell how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:{query}\n")
    except Exception as e:
        print("Sir, Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Write sender gmail here', 'Write sender password here')
    server.sendmail('Write sender gmail here', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open codewithharry" in query:
            webbrowser.open("codewithharry.com")

        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        elif "play music" in query:
            music_dir = "Type the location of your music here"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "the date" in query:
            strDay = date.today()
            speak(f"Sir, today's date is {strDay} ")
            speak(f"Sir, today's date is {strDay} ")

        elif "open code editor" in query:
            programPath = "Type the target of your problem here"
            os.startfile(programPath)
            
        elif "open microphone" in query:
            programPath = "C:\Program Files (x86)\WOMic\WOMicClient.exe"
            os.startfile(programPath)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Type receiver gmail here"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")