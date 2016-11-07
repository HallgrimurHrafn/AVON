import RPi.GPIO as GPIO
import time
import threading


GPIO.setmode(GPIO.BOARD)

# rotary haegri tengt i gpio 33 og vinstri i 31.

# Clockwise:
# 0,0 : state 0
# 1,0 : state 1
# 1,1 : state 2
# 0,1 : state 3
# 0,0 : state 0  hrin er lokid her


cl=0
cr=0
state=0
fstate=0  # former state. sidasta astand semsagt.

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right

def test(channel):
    print('yeei')
def rotary(channel):
    global cl, cr, lock, fstate, state
    if cl ==GPIO.input(33) and cr==GPIO.input(31):  # erum vid i sama state-i?
        return
    cl = GPIO.input(33)     # ef ekki uppfaerum
    cr = GPIO.input(31)
    fstate = state          # uppfaerum gamla astand.
    if cl==1 and cr==0:     # uppfaerum astand og haettum ef astand er ekki 0.
        state=1
        return
    elif cl==1 and cr==1:
        state=2
        return
    elif cl==0 and cr==1:
        state=3
        return
    state=0
    if fstate==1:
        print 'right';
    elif fstate==3:
        print 'left';
    else:
        print 'eitthvad for urskeidis.'


GPIO.add_event_detect(35, GPIO.RISING, callback=test, bouncetime=100)
GPIO.add_event_detect(33, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(31, GPIO.BOTH, callback=rotary)


while True:
    time.sleep(10)
