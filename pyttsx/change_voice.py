import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
for voice in voices:
   print voice.id, voice.age, voice.gender, voice.languages, voice.name
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
