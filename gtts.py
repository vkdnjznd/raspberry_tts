from gtts import gTTS
import os

def sayingVoice1(message):
    engine = pyttsx3.init(debug=True)
    voices = engine.getProperty('voices')
    volume = engine.getProperty('volume')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    engine.say(message)
    engine.runAndWait()

#sayingVoice1("Hello")
#mp3_fp = BytesIO()

filename='voice.mp3'
tts = gTTS(text='Hello', lang="en")
tts.save('voice.wav')
os.popen('sudo mpg123 voice.wav && pkill mpg123')




