import RPi.GPIO as GPIO
import time
import threading
import Main
import menu
import numpy as np

GPIO.setmode(GPIO.BOARD)

# rotary haegri tengt i gpio 33 og vinstri i 31.

# Clockwise:
# 0,0 : state 0
# 1,0 : state 1
# 1,1 : state 2
# 0,1 : state 3
# 0,0 : state 0  hrin er lokid her

# fylki fyrir bada rotary
cl=np.array([0, 0])
cr=np.array([0, 0])
state=np.array([0, 0])
fstate=np.array([0, 0])   # former state. sidasta astand semsagt.
l=np.array([33, "placeholder"])    # vantar gpio channel fyrir rotary 2.
r=np.array([31, "placeholder"])

# rotary 1
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right

# rotary 2
# GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click
# GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
# GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right



def rotary(channel):
    if channel==31 or channel==33 or channel==35:  # hvada rotary er ad senda.
        i=0
    else:
        i=1
    # placeholder verdur gpio fyrir rotary 2 click channel
    if channel==31 or channel == "placeholder"
        cd=True
    else:
        cd=False
    if cd:
        # print "yeii", i        # click kom. af rotary <i>.
        menu.click(i)
    global cl, cr, lock, fstate, state
    if cl[i] ==GPIO.input(33) and cr[i]==GPIO.input(31):  # erum vid i sama state-i?
        return
    cl[i] = GPIO.input(33)     # ef ekki uppfaerum
    cr[i] = GPIO.input(31)
    fstate[i] = state[i]          # uppfaerum gamla astand.
    if cl[i]==1 and cr[i]==0:     # uppfaerum astand og haettum ef astand er ekki 0.
        state[i]=1
        return
    elif cl[i]==1 and cr[i]==1:
        state[i]=2
        return
    elif cl[i]==0 and cr[i]==1:
        state[i]=3
        return
    state[i]=0
    if fstate[i]==1:
        print 'right', i
        menu.move(i, 1)
    elif fstate[i]==3:
        print 'left', i
        menu.move(i, -1)
    else:
        print 'eitthvad for urskeidis.', i

# rotary 1
GPIO.add_event_detect(35, GPIO.RISING, callback=rotary, bouncetime=100)
GPIO.add_event_detect(33, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(31, GPIO.BOTH, callback=rotary)

# rotary 2
# GPIO.add_event_detect(35, GPIO.RISING, callback=rotary, bouncetime=100)
# GPIO.add_event_detect(33, GPIO.BOTH, callback=rotary2)
# GPIO.add_event_detect(31, GPIO.BOTH, callback=rotary2)


while True:
    time.sleep(10)
