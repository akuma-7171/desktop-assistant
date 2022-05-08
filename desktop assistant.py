import pyttsx3
import webbrowser as wb
import smtplib
import pywhatkit as k
import os
import wikipedia
import speech_recognition as sr
import datetime




engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def wish():

    hr = int(datetime.datetime.now().hour)

    if hr>=0 and hr<12:
        speak("hey good morning my name is jarvis how can i help you")

    elif hr>=12 and hr<18 :
        speak("hey good aftrnoon my name is jarvis how can i help you")

    else:
        speak("hey good evening my name is jarvis how can i help you")


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:

        print("say that again please")
        speak("say that again please")
        return "None"


    return query



def sendit(to, content):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("jeetgandhi.ict19@gmail.com", "asQW@123")
    server.sendmail("nihardabhi.ict19@gmail.com", to, content)
    server.close()


if __name__ == "__main__":

    wish()


    while 1:

        query = takecommand().lower()


        if "wikipedia" in query:

            speak("searching on wikipedia")

            query = query.replace("wikipedia", "")

            res = wikipedia.summary(query, sentences=4)
            speak("according to wikipedia")
            speak(res)



        elif 'open facebook' in query:

            wb.open("facebook.com")


        elif 'open instagram' in query:

            wb.open("instagram.com")

        elif "open whatsapp" in query:

            wb.open("web.whatsapp.com")

        elif 'open google' in query:

            speak("what shuold i search on google")

            cm = takecommand()

            k.search(f"{cm}")


        elif 'play something on youtube' in query:

            speak("what should i play on youtube")

            s = takecommand()

            k.playonyt(f"{s}")


        elif 'send a mail' in query:

            try:
                speak("what should i write in mail")

                content = takecommand()

                to = "nihardabhi.ict19@gmail.com"

                sendit(to, content)

                speak("mail has been sent")

            except Exception:

                speak("sorry, something went wrong i can not send the mail")
