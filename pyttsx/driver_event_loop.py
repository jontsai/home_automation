import pyttsx

engine = pyttsx.init()
def onStart(name):
   print 'starting', name
def onWord(name, location, length):
   print 'word', name, location, length
def onEnd(name, completed):
   print 'finishing', name, completed
   if name == 'fox':
      engine.say('What a lazy dog!', 'dog')
   elif name == 'dog':
      engine.endLoop()
engine = pyttsx.init()
engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
engine.startLoop()
