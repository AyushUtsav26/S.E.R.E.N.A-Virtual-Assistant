from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import wikipedia
from requests import get
from bs4 import BeautifulSoup
import random
import pyjokes
from urllib.request import urlopen




flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning mister utsav")
    elif hour>=12 and hour<18:
        speak("Good Afternoon mister utsav")
    else:
        speak("Good evening mister utsav")

    speak("Please tell me what can i do for you!") 

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recognizing......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry, i did not get what you mean, please Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if 'terminate' in self.query:
                speak("system closing. Have a nice day sir!")
                sys.exit()
            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube")
            
            elif 'open stack overflow' in self.query:
                webbrowser.open("stackoverflow.com")
                speak("opening stack overflow")

            elif 'wikipedia' in self.query:  #if wikipedia found in the query then this block will be executed
              speak('Searching Wikipedia...')
              self.query = self.query.replace("wikipedia", "")
              results = wikipedia.summary(self.query, sentences=4) 
              speak("According to Wikipedia")
              speak(results) 

            elif 'what is the time' in self.query:
              strTime = datetime.datetime.now().strftime("%H:%M:%S")    
              speak(f"Sir, the time is {strTime}")

            elif 'ip address' in self.query:
              ip = get('https://api.ipify.org').text
              speak(f"you ip address is {ip}")
              print(f"ip address:{ip}")

            elif 'open cmd' in self.query:
              speak("opening command prompt")
              os.system("start cmd")

            elif 'open unity hub' in self.query:
             speak("opening unity hub")
             unityPath = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
             os.startfile(unityPath)

            elif 'open notepad' in self.query:
             speak("opening notepad")
             notepath = "C:\\Windows\\system32\\notepad.exe"
             os.startfile(notepath)
        
            elif 'open ms word' in self.query:
             speak("opening microsoft word")
             wordpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\winword.exe"
             os.startfile(wordpath)    

            elif 'open my github' in self.query:
                webbrowser.open("https://github.com/AyushUtsav26")
                speak("opening your git hub")

            elif 'how are you' in self.query:
             speak("I am fine, Thank you")
             speak("How are you, Sir")
 
            elif 'fine' in self.query or "good" in self.query:
             speak("It's good to know that your fine")

            elif 'thanks' in self.query or "thank you" in self.query:
                speak("welcome sir!") 

            elif "who are you" in self.query or "What is your name" in self.query:
             speak("I am an artificial intelligence, my creator named me serena, serena means smart exceptional resouceful excellent natural language processing artificial intelligence")


            elif "who made you" in self.query or "who created you" in self.query:
              speak("I have been created by mister Ayush Utsav, he is an engineer.")

            elif 'joke' in self.query:
             speak(pyjokes.get_joke())

            elif 'reason behind your creation' in self.query:
              speak("It is a mystery!")

            elif "major task" in self.query:
             speak("To help mister utsav to fulfil his dreams.")



FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())