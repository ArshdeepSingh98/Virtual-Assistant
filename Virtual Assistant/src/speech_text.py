import speech_recognition as sr
import pyaudio
import text_speech
import time
# obtain audio from the microphone
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        text_speech.say("Say something!")
        audio = r.listen(source, timeout=8)
    input_textr=""
    # recognize speech using Sphinx
    try:
        #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        input_textr = r.recognize_google(audio)
        print("You said :- " + input_textr)
        return input_textr
    except sr.UnknownValueError:
        text_speech.say("Could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))