import pyttsx

def onWord(name, location, length):
   print 'word', name, location, length
   if location > 10:
      engine.stop()
engine = pyttsx.init()
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
