import RPi.GPIO as GPIO
import time
import threading
import Main
import menu


GPIO.setmode(GPIO.BOARD)

# rotary haegri tengt i gpio 33 og vinstri i 31.

# Clockwise:
# 0,0 : state 0
# 1,0 : state 1
# 1,1 : state 2
# 0,1 : state 3
# 0,0 : state 0  hrin er lokid her

# rotary1
cl1=0
cr1=0
state1=0
fstate1=0  # former state1. sidasta astand semsagt.

# rotary2
cl2=0
cr2=0
state2=0
fstate2=0  # former state2. sidasta astand semsagt.

# rotary 1
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary cl1ick
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right

# rotary 2
# GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary cl1ick
# GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
# GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right

def test(channel):
    print('yeei')
def rotary(channel):
    global cl1, cr1, lock, fstate1, state1
    if cl1 ==GPIO.input(33) and cr1==GPIO.input(31):  # erum vid i sama state-i?
        return
    cl1 = GPIO.input(33)     # ef ekki uppfaerum
    cr1 = GPIO.input(31)
    fstate1 = state1          # uppfaerum gamla astand.
    if cl1==1 and cr1==0:     # uppfaerum astand og haettum ef astand er ekki 0.
        state1=1
        return
    elif cl1==1 and cr1==1:
        state1=2
        return
    elif cl1==0 and cr1==1:
        state1=3
        return
    state1=0
    if fstate1==1:
        print 'right';
    elif fstate1==3:
        print 'left';
    else:
        print 'eitthvad for urskeidis.'

# rotary 1
GPIO.add_event_detect(35, GPIO.RISING, callback=test, bouncetime=100)
GPIO.add_event_detect(33, GPIO.BOTH, callback=rotary1)
GPIO.add_event_detect(31, GPIO.BOTH, callback=rotary1)

# rotary 2
# GPIO.add_event_detect(35, GPIO.RISING, callback=test, bouncetime=100)
# GPIO.add_event_detect(33, GPIO.BOTH, callback=rotary2)
# GPIO.add_event_detect(31, GPIO.BOTH, callback=rotary2)


while True:
    time.sleep(10)
