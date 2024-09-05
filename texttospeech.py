##
import pyttsx3

text_speech = pyttsx3.init()
answer = input("what do you want me to say")
text_speech.say(answer)
text_speech.runAndWait()

##
import subprocess
talk = input("what do you want to say\n")
subprocess.run(["say", talk])
##
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting Noise")
    recognizer.adjust_for_ambient_noise(source, duration=7)
    print("Recording for 4 Seconds")
    recorded_audio = recognizer.listen(source, timeout=4)
    print("Done listening")
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
        recorded_audio,
        language="en-us"
    )
    print("Decoded Text : {}".format(text))
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as ex:
    print("Could not request results from Google Web Speech API; {0}".format(ex))
    ##

