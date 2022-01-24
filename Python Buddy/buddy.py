import speech_recognition as speechRec 
import pyttsx3, pyaudio,pyjokes

engine = pyttsx3.init('sapi5')

#Modifies the voices rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)

#Modifies the engines voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



#This will speak what is put through it
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#This will convert all speech to text using the speech_recognizition tool from google
def translator():
    rec = speechRec.Recognizer()

    with speechRec.Microphone() as source:
        print("I am listening...")
        speak('I am listening')
        audio = rec.listen(source)

        try:
            query = rec.recognize_google(audio)
            print(f"Master:{query}")
            return query
        except:
            print("Try Again")
            return ''


while True:
    query = translator().lower()

    try:
        if 'hello' in query:
            speak("Hello! ")
    
        elif 'bye' in query:
            speak("Goodbye! ")
            break
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
    
        else:
            speak("I couldn't quite catch that")
    except:
        break