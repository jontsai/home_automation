import pyttsx

engine = pyttsx.init()
voice = engine.getProperty('voice')
engine.setProperty('voice', 'english-us')
print 'Voice: %s' % voice

engine.say('Greetings!')
engine.say('How are you today?')
engine.say('This is pretty cool.')
engine.runAndWait()
