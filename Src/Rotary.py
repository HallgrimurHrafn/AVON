import RPi.GPIO as GPIO
import time
import threading
# import Main
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
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click

# rotary 2
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click



def rotary(channel):
    global cl, cr, fstate, state
    if channel==33 or channel==35 or channel==37:  # hvada rotary er ad senda.
        i=0  # rotary 1
    else:
        i=1  # rotary 2
    # placeholder verdur gpio fyrir rotary 2 click channel
    if channel==37 or channel == 32:
        cd=True
    else:
        cd=False
    if cd:
        # print "yeii", i        # click kom. af rotary <i>.
        menu.click(i)
    global cl, cr, lock, fstate, state
    if i==0:
        if cl[i] ==GPIO.input(35) and cr[i]==GPIO.input(33):  # erum vid i sama state-i?
            return
        cl[i] = GPIO.input(35)     # ef ekki uppfaerum
        cr[i] = GPIO.input(33)
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
        # print 'right', i
        menu.move(i, 1)
    elif fstate[i]==3:
        # print 'left', i
        menu.move(i, -1)
    else:
        return
        # print 'eitthvad for urskeidis.', i

# rotary 1
GPIO.add_event_detect(33, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(35, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(37, GPIO.RISING, callback=rotary, bouncetime=100)

# rotary 2
GPIO.add_event_detect(29, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(31, GPIO.BOTH, callback=rotary)
GPIO.add_event_detect(32, GPIO.RISING, callback=rotary, bouncetime=100)


def initScrollY():
    menu.fScrollMapY[:][:]="pass"
    menu.fScrollMapY[0][0]="tempchange(val, 1)"
    menu.fScrollMapY[0][1]="channelchange(val)"   # svona getum vid baett vid functions :D
    #skali fScrollMapX[0][2]
    menu.fScrollMapY[0][3]="livechange()"
    menu.fScrollMapY[0][4]="camerachange()"
    menu.fScrollMapY[0][5]="notelengdChange(val)"
    menu.fScrollMapY[0][6]="barChange(val)"

    # tempchange
    menu.fScrollMapY[1][0]="tempchange(val, 100)"
    menu.fScrollMapY[1][1]="tempchange(val, 10)"
    menu.fScrollMapY[1][2]="tempchange(val, 1)"

    # skali
    menu.fScrollMapY[2][0]="skalarChange(val,1)"
    menu.fScrollMapY[2][1]="skalarChange(val,0)"

    # customskali
    for x in range (0,8):
        menu.fScrollMapY[3][x]="customskali(val,"
        menu.fScrollMapY[3][x]+=str(7-x)+")"


    menu.fScrollMapY[4][0]="cameraMode(val,0)"
    menu.fScrollMapY[4][1]="cameraMode(val,1)"
    menu.fScrollMapY[4][2]="cameraMode(val,2)"

# fScrollMapX initialization starts
def initScrollX():
    fScrollMapX=np.chararray((5,8), itemsize=25)
    fScrollMapX[:][:]="pass"
    low="""
    if val==1:
        navx+=val
        Render.Render()"""
    high="""
    if val==-1:
        navx+=val
        Render.Render()"""
    default="""
    navx+=val
    Render.Render()"""
    fScrollMapX[0][0]=low
    fScrollMapX[0][1]=default
    fScrollMapX[0][2]=default
    fScrollMapX[0][3]=default
    fScrollMapX[0][4]=default
    fScrollMapX[0][5]=default
    fScrollMapX[0][6]=high

    fScrollMapX[1][0]=low
    fScrollMapX[1][2]=default
    fScrollMapX[1][3]=high

    fScrollMapX[2][0]=low
    fScrollMapX[2][1]=high

    fScrollMapX[3][0]=low
    fScrollMapX[3][1]=default
    fScrollMapX[3][2]=default
    fScrollMapX[3][3]=default
    fScrollMapX[3][4]=default
    fScrollMapX[3][5]=default
    fScrollMapX[3][6]=default
    fScrollMapX[3][7]=high

    fScrollMapX[4][0]=low
    fScrollMapX[4][0]=default
    fScrollMapX[4][0]=high
    menu.fScrollMapX=fScrollMapX
# fScrollMapX initialization ends


def initClick():
    fClickMap=np.chararray((5,8), itemsize=25)
    fClickMap[:][:]="pass"
    fClickMap[0][0]="""
    oldnavx=navx
    navx=0
    navy=1
    Render.Render()"""
    fClickMap[0][2]="""
    oldnavx=navx
    navx=0
    navy=2
    Render.Render()"""
    fClickMap[0][4]="""
    oldnavx=navx
    navx=0
    navy=4
    Render.Render()"""
    fClickMap[2][1]="customsetup()"
    menu.fClickMap=fClickMap

initScrollY()
initScrollX()
initClick()

while True:
    time.sleep(10)
