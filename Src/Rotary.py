import RPi.GPIO as GPIO
import time
# import menu
import numpy as np



# rotary haegri tengt i gpio 11 og vinstri i 31.

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

GPIO.setmode(GPIO.BOARD)
# rotary 1
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click

# rotary 2
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click



def rotary(channel):
    print channel
    global cl, cr, lock, fstate, state
    if channel==11 or channel==13 or channel==37:  # hvada rotary er ad senda.
        i=0  # rotary 1
        # print GPIO.input(13),GPIO.input(11), "debug1", state[0]
    else:
        i=1  # rotary 2
        # print GPIO.input(31),GPIO.input(29), "debug2", state[1]
    # placeholder verdur gpio fyrir rotary 2 click channel
    if channel==37 or channel == 32:
        cd=True
    else:
        cd=False
    if cd:
        print "yeii", i        # click kom. af rotary <i>.
        # menu.click(i)
    if i==0:
        if cl[i] ==GPIO.input(13) and cr[i]==GPIO.input(11):  # erum vid i sama state-i?
            return
        cl[i] = GPIO.input(13)     # ef ekki uppfaerum
        cr[i] = GPIO.input(11)
    else:
        if cl[i]==GPIO.input(31) and cr[i]==GPIO.input(29):
            return
        cl[i]=GPIO.input(31)
        cr[i]=GPIO.input(29)
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
        # menu.move(i, 1)
    elif fstate[i]==3:
        print 'left', i
        # menu.move(i, -1)
    else:
        return
        print 'eitthvad for urskeidis.', i

# rotary 1
GPIO.add_event_detect(11, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(13, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(37, GPIO.RISING, callback=rotary, bouncetime=150)

# rotary 2
GPIO.add_event_detect(29, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(31, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(32, GPIO.RISING, callback=rotary, bouncetime=150)


while True:
    time.sleep(10)
