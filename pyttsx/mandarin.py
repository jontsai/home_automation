import pyttsx

engine = pyttsx.init()
engine.setProperty('voice', 'Mandarin')
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+5)
engine.say('ni wen wo ai ni yo duo sheng, wo ai ni you ji fen. wo di ai ye zhen, wo de xin ye zhen, yueliang dai biao wo de xin')
engine.say('dui mian de nvu hai kan guo lai, kan guo lai, kan guo lai')
engine.say('Ni hao. Jin tian zao shang hao')
engine.say('ni chi dongxi le ma? wo xiang yao shuijiao')
engine.say('ni kebukeyi gei wo yi kuai qian')
engine.runAndWait()
