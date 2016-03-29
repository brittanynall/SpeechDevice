import pyttsx
import pyttsx.voice

class Speech():
    def say_action(self,action):
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-75)
        vol = engine.getProperty('volume')
        engine.setProperty('volume', vol+10)
        engine.say(action)
        engine.runAndWait()