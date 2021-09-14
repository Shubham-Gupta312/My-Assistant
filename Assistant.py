import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


'''
WISH ME ACCORDING TO TIME
      
'''
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print('Good Morning!')
        speak('Good Morning!')
    elif hour >= 12 and hour < 16:
        print('Good AfterNoon!')
        speak('Good AfterNoon!')
    elif hour >= 16 and hour < 20:
        print('Good Evening!')
        speak('Good Evening!')
    else:
        print('Good Night!')
        speak('Good Night!')

    print("Hi, I am Your Assistant.")
    speak('I am Your Assistant. Please Tell me How Can I Help You?')


'''
IT TAKES THE COMMAND  AS INPUT FROM USER AND RETURN STRING OUTPUT
'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print('Please Say Again..')
        return 'None'
    return query

'''
IT SEND THE MAIL
'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your-Gmail-Id', 'Your-Password')
    server.sendmail('yourgmail.com', to, content)
    server.close()


if __name__ == '__main__':
    # speak('Hey! How are you')
    wishMe() 
    while True:
        query = takeCommand().lower()

        # Logic to execute Task on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=4)
            speak('According To Wikipedia..')
            speak(result)
            print(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'E:\\JAVA SCRIPT\\Project\\music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            # print()
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            path = 'C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'shubhamgupta7082@gmail.com'
                sendEmail(to, content)
                speak('Emal has been Sent!')
            except Exception as e:
                # print(e)
                speak('Sorry!, I am not able to send this Email!')

        elif 'quit' in query:
            exit()
