import numpy as np
import Render
import Main

# navigation tools. navx og navy eru stadsetningarnar okkar i function maps.
navx=0
navy=0
oldnavx=0

#fClickMap er function map fyrir click.
fClickMap=np.chararray((4,8), itemsize=25)         # max 25 stafir.. haegt ad auka.
fClickMap[:][:]="pass"

#fScrollMapY er function map fyrir scroll y
fScrollMapY=np.chararray((4,8), itemsize=25)
fScrollMapY[:][:]="pass"

#fScrollMapX er function map fyrir scroll x
fScrollMapX=np.chararray((4,8), itemsize=25)
fScrollMapX[:][:]="pass"


def initScrollY():
    fScrollMapY[0][0]="tempchange(val, 1)"
    fScrollMapY[0][1]="channelchange(val)"   # svona getum vid baett vid functions :D
    fScrollMapX[0][2]="pass"  #skali
    fScrollMapY[0][3]="livechange()"
    fScrollMapY[0][4]="camerachange()"
    fScrollMapY[0][5]="nodelengdChange(val)"
    fScrollMapY[0][6]="barChange(val)"

    # tempchange
    fScrollMapY[1][0]="tempchange(val, 100)"
    fScrollMapY[1][1]="tempchange(val, 10)"
    fScrollMapY[1][2]="tempchange(val, 1)"

    # skali
    fScrollMapY[2][0]="skalarChange(val,1)"
    fScrollMapY[2][1]="skalarChange(val,0)"

    # customskali
    for x in range (0,8):
        fScrollMapY[3][x]="skalichange(val,"
        fScrollMapY[3][x]+=str(7-x)+")"


    fScrollMapY[4][0]="cameraMode(val,0)"
    fScrollMapY[4][1]="cameraMode(val,1)"
    fScrollMapY[4][2]="cameraMode(val,2)"

# fScrollMapX initialization starts
def initScrollX():
    low="""
    if val==1:
        navx+=val """
    high="""
    if val==-1:
        navx+=val """
    default="navx+=val"
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
# fScrollMapX initialization ends


def initClick():
    fClickMap[0][0]="""
    oldnavx=navx
    navx=0
    navy=1 """
    fClickMap[0][2]="""
    oldnavx=navx
    navx=0
    navy=2 """
    fClickMap[0][4]="""
    oldnavx=navx
    navx=0
    navy=4 """
    fClickMap[2][1]=

def move(i, val):
    if i==1:
        moveHorizontal(val)
    else:
        moveVertical(val)


def moveHorizontal(val):
    global navx, navy, nav
    if navx+val>=0:
        if nav[navy][navx+val]

def moveVertical(val):
    global navx

def click(i):
    global fClickMap
    if i==1:
        kort(fClickMap,0)
    else:
        moveup()


def moveup():
    global navx, oldnavx
    if navy-1>0:
        navy-=1
        navx=oldnavx
        Render.Render()


def kort(matrix,val):
    global navy, navx, oldnavx               # matrix er annad hvort nav eda
    exec matrix[navy][navx]
    #                               # exec breytir i koda og keyrir fallid.


def channelchange(val):
    if 0<=Main.v+val<=15:
        Main.v=Main.v+val
        Main.ChannelChange()
        Render.Render()


def tempchange(val, x):
    if 0<=Main.tempo+val*x<=600:
        Main.taptemp=0
        time.sleep(0.01)
        Main.tempo=Main.tempo+val
        Main.taptemp=1
        Render.Render()


def livechange():
    if Main.lGO==1:
        Main.lGO=0
    else:
        Main.lGO=1
    Main.multithread()
    Render.Render()

def camerachange():
    if Main.cGO==1:
        Main.cGO=0
    else:
        Main.cGO=1

    # forrit sem uppfaerir cameramod
    Render.Render()


def nodelengdChange(val): # tharf ad adlaga fyrir prosentu
    if 0<Main.lengd+val<1:
        Main.lengd=Main.lengd+val
        Render.Render()

# def FLASHchange(val): # tharf ad adlaga fyrir prosentu
#     if 0<Main.FLASH+val<1:
#         Main.FLASH=Main.FLASH+val
#         Render.Render()

def skalichange(val,i):
    if 0<i<15:
        if 0<=Main.skali[i]+val<128:
            Main.skali[i]=Main.skali[i]+val
            Render.Render()

def skalarChange(val,x):
    pass

def barChange(val):
    pass
