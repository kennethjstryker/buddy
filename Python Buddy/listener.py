import speech_recognition as speechRec 

#This will convert all speech to text using the speech_recognizition tool from google
def translator():
    rec = speechRec.Recognizer()

    with speechRec.Microphone() as source:
        print("I am listening...")
        audio = rec.listen(source)

        try:
            query = rec.recognize_google(audio)
            print(f"master:{query}")
            return query
        except:
            print("Try Again")
