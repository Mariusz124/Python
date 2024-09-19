import speech_recognition as sr
import pyttsx3 as tts
import os,sys,time

# Obiekty
r= sr.Recognizer()
engine=tts.init()
engine.setProperty('voice',engine.getProperty('voices')[0].id)
# wczytaj Chrome
chrome='C:\\"Program Files"\\Google\\Chrome\\Application\\chrome.exe'
def speak(text):
    engine.say(text)
    engine.runAndWait()
def getText():
    try:
        with sr.Microphone() as source:
            print("Nasłuchuję...",end='\r')
            audio = r.listen(source)
            text=r.recognize_google(audio, language="pl-PL")
            if text == "":
                return None
            else:
                return text
    except:
        return None
def czy_zawiera(string,slowa):
    return [element for element in slowa if element in string.lower()]
print("Aby wyjśc powiedz Dowidzenia")
WYKRYJ = ['bot','robot','robocie','kolego']
DOWIDZENIA = ['dowidzenia','do widzenia','papa','żegnaj']
SZUKAJ = ['wyszukaj','szukaj','znajdz','googluj','pokaż']
while True:
    time.sleep(0.5)
    cur = getText()
    print(""*50,end="\r")
    if cur!= None:
        if len(czy_zawiera(cur,WYKRYJ)):
            if len(czy_zawiera(cur,DOWIDZENIA)):
                speak("Żegnaj")
                break
            elif len(czy_zawiera(cur,SZUKAJ)):
                linczek = cur.lower().split(''+ czy_zawiera(cur,SZUKAJ)[0]+'')[1]
                speak("Oto co udało mi się znaleźć.")
                url="https://www.google.com/search?q="+linczek.replace("","+").replace("?","%3F")
                os.system(chrome+""+url)