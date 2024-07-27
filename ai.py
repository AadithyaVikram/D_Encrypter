'''
import speech_recognition as sr
import pyttsx3
import time
import keyboard
# obtain audio from the microphone
r = sr.Recognizer()
pyttsx3.speak("welcome sir. jarvis is ready for you")
print("ready to listen")

jarvis=pyttsx3.init()

def welcome():
    if "hi" in a.lower():
        pyttsx3.speak("hi sir")
    if "hello" in a.lower():
        pyttsx3.speak("hello sir")
def rtime():
    if 'time' in a.lower():
        atime=time.localtime()
        medi=""
        if int(atime[3])>12:
            medi="pm"
            hours=(int(atime[3])-12)
        else:
            medi="am"
            hours=int(atime[3])
        hm=str(hours)+"  "+str(atime[4])+medi
        jarvis.setProperty("rate",150)
        #jarvis.say(hours)
        #jarvis.say(atime[3])
        jarvis.say(hm)
        jarvis.setProperty("rate",200)
        jarvis.runAndWait()
def rdate():
    if "date" in a.lower():
        adate=time.localtime()
        jarvis.say(adate[2])
        jarvis.say(adate[1])
        jarvis.say(adate[0])
def apologize():
    if "apologize" in a.lower():
        jarvis.say("sorry")
def mygratitude():
    if 'gratitude' in a.lower():
        jarvis.say("thank you very much")
def quitzzz():
    if "close" in a.lower():
        pyttsx3.speak("ok sir, going to shutdown mode")
        if hourzzz>20:
            pyttsx3.speak("good night sir")
        quit()
def dotype():
    if 'type' in a.lower():
        pyttsx3.speak("now ready sir.")
        typed=r.listen(source)
        typed=r.recognize_google(audio_type)
def wish():
    if "vish" in a.lower():
        pyttsx3.speak("ok sir. to whom sir..")
        wishto=r.listen(source)
        wishto1=r.recognize_google(wishto)
        pyttsx3.speak("message sir")
        messag=r.listen(source)
        messag1=r.recognize_google(messag)
        m=messag1+wishto1
        jarvis.say(m)
        
with sr.Microphone() as source:
    ctime=time.localtime()
    hourzzz=int(ctime[3])
    if hourzzz<12:
        pyttsx3.speak("good morning sir")
    elif hourzzz<16:
        pyttsx3.speak("good afternoon sir")
    else:
        pyttsx3.speak("good evening sir")
    print("listening sir")
    pyttsx3.speak("listening sir")
    try:
        audio = r.listen(source)
        a=r.recognize_google(audio)
        
        if "jarvis" in a.lower():
            print(a)
            welcome()
            rtime()
            rdate()
            apologize()
            mygratitude()
            dotype()
            quitzzz()
    except:
                print("unable to recognize sir.......Reloading")
                pyttsx3.speak("unable to recognize sir.......Reloading")

for i in range(10):
    with sr.Microphone() as source:
        print("listening sir")
        pyttsx3.speak("listening sir")
        try:
            pyttsx3.speak("analyzing")
            audio = r.listen(source)
            a=r.recognize_google(audio)
            
            if "jarvis" in a.lower():
                print(a)
                welcome()
                rtime()
                rdate()
                apologize()
                mygratitude()
                dotype()
                quitzzz()
        except:
                    print("unable to recognize sir.......Reloading")
                    pyttsx3.speak("unable to recognize sir.......Reloading")


'''



'''
import pywhatkit
pywhatkit.sendwhatmsg(phone_no, message, time_hour, time_min)'''



print("testing")

