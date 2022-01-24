import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#This will speak what is put through it
def speak():
    engine.say(audio)
    engine.runAndWait()
