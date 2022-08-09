import pyttsx3
import speech_recognition as sr
import json

class AI():
    __name = ""
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice' ,voices[0].id)
        name = voices[0].name
        print(name)

        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name

        print("Listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self.__name
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait()

    def say(self, sentence):
        print(sentence)
        self.before_speaking.trigger(sentence)
        self.engine.say(sentence)
        self.engine.runAndWait()
        self.after_speaking.trigger(sentence)

def listen(self):
           
        phrase = ""
        
        if self.r.AcceptWaveform(self.audio.read(4096,exception_on_overflow = False)):
            self.before_listening.trigger()
            phrase = self.r.Result()
            phrase = phrase.removeprefix('the')
            
            phrase = str(json.loads(phrase)["text"])

            if phrase:
                self.after_listening.trigger(phrase)
            return phrase

        return None