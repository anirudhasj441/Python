
import pyttsx3
import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
l=['s','p','c']
sc_usr=0
sc_com=0
play_again='y'
while play_again=='y':
    com=random.sample(l,1)
    #print(type(com[0]))
    usr=input('s,p,c:')
    print('com=',com[0],'\nusr=',usr)
    if com[0]=='s':
        if usr=='p':
            print('usr win')
            sc_usr+=1
        elif usr=='s':
            print('it\'s tie')
        else:
            print('com win')
            sc_com+=1
    elif com[0]=='p':
        if usr=='c':
            print('usr win')
            sc_usr+=1
        elif usr=='p':
            print('it\'s tie')
        else:
            print('com win')
            sc_com+=1
    elif com[0]=='c':
        if usr=='s':
            print('usr win')
            sc_usr+=1
        elif usr=='c':
            print('it\'s tie')
        else:
            print('com win')
            sc_com+=1
    speak('would you like to play again!')
    play_again=input("would you like to play again:")
print('score of com:',sc_com)
print('score of usr:',sc_usr)
if sc_com>sc_usr:
    speak('you lose')
    print('you lose')
else:
    speak('you win')
    print('you win')