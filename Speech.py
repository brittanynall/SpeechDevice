import pyttsx
import pyttsx.voice
import pyttsx.drivers.espeak

class Speech():
    def say_action(self,action):
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-75)
        vol = engine.getProperty('volume')
        engine.setProperty('volume', vol+10)
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[69].id)
        count = 0
        for v in voice:
            count =count+1
            print v.id, count
        engine.say(action)
        engine.runAndWait()