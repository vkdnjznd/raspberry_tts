import speech_recognition as sr
from subprocess import call
import os
import time
from gtts import gTTS

def defaultVoice(message):
    os.popen('espeak -v ko -s 150 "'+message+'" --stdout | sudo aplay 2>/dev/null')
 

def sayingVoice1(message):
    filename='gtts.wav'
    tts = gTTS(text=message, lang="ko")
    tts.save(filename)
    os.popen('sudo mpg123 gtts.wav && pkill mpg123')


def callback(recognizer, audio):  
        try:
            message = r.recognize_google(audio, language='ko-kr', show_all=False)
            print('message = {}, type = {}'.format(message, type(message)))
            if message == "안녕":
                sayingVoice1("안녕하세요")
            else:
                sayingVoice1(message)

        except sr.UnknownValueError:
            print("Unknown")


r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

r.energy_threshold=50

with mic as source:
        r.adjust_for_ambient_noise(source)
        #r.adjust_for_ambient_noise(source)
        #audio = r.listen(source, timeout=0, phrase_time_limit=2.5)

stop_listening = r.listen_in_background(mic, callback)


#for _ in range(50):
#    time.sleep(0.1)

#stop_listening(wait_for_stop=False)

while True: time.sleep(0.1)
