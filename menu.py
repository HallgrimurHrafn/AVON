import numpy as np
import Render
import Main
import math

# navigation tools. navx og navy eru stadsetningarnar okkar i function maps.
navx=0
navy=0
oldnavx=0

# skalar related
es=0                #edit skali, es=1 fyrir custom skala 1, es=2 fyrir customskala 2....
note=60
currentscale=0      #0= dur, 1=moll, 2=penta, 3,4,5.... =customs 1,2,3....
# ef currentscale >2 ma gera adgerd i custom.
skalar=np.chararray(3, itemsize=10)
skalar[0]="Main.skali=np.array([note+12, note+11, note+9, note+7, note+5, note+4, note+2,note])"
skalar[1]="Main.skali=np.array([note+12, note+10, note+8, note+7, note+5, note+3, note+2,note])"
skalar[2]="Main.skali=np.array([note+17, note+15, note+12, note+10, note+7, note+5, note+3, note])"
skalar[3]="pass"   # custom skali
custom=np.array([60, 60, 60, 60, 60, 60, 60, 60])
cs=[]
#fClickMap er function map fyrir click.
fClickMap=np.chararray((5,8), itemsize=25)         # max 25 stafir.. haegt ad auka.
fClickMap[:][:]="pass"

#fScrollMapY er function map fyrir scroll y
fScrollMapY=np.chararray((5,8), itemsize=25)
fScrollMapY[:][:]="pass"

#fScrollMapX er function map fyrir scroll x
fScrollMapX=np.chararray((5,8), itemsize=25)
fScrollMapX[:][:]="pass"


def initScrollY():
    fScrollMapY[0][0]="tempchange(val, 1)"
    fScrollMapY[0][1]="channelchange(val)"   # svona getum vid baett vid functions :D
    #skali fScrollMapX[0][2]
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
        fScrollMapY[3][x]="customskali(val,"
        fScrollMapY[3][x]+=str(7-x)+")"


    fScrollMapY[4][0]="cameraMode(val,0)"
    fScrollMapY[4][1]="cameraMode(val,1)"
    fScrollMapY[4][2]="cameraMode(val,2)"

# fScrollMapX initialization starts
def initScrollX():
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
# fScrollMapX initialization ends


def initClick():
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

def move(i, val):
    global fScrollMapX, fScrollMapY
    if i==1:
        kort(fScrollMapX,val)
    else:
        kort(fScrollMapY,val)


def click(i):
    global fClickMap
    if i==1:
        kort(fClickMap,0)
    else:
        moveup()


def moveup():
    global navx, oldnavx, navy
    if navy=3:
        nyrskali()
    if navy-1>0:
        navy-=1
        navx=oldnavx
        Render.Render()


def kort(matrix,val):
    global navy, navx, oldnavx     # matrix er annad hvort nav eda
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

def camera(val, xyz):
    if xyz==0:      # x
        pass
    elif xyz==1:    # y
        pass
    elif xyz==2:    # z
        pass
    Render.Render()

def nodelengdChange(val):
    val=float(val/20)
    if 0<Main.lengd+val<1:
        Main.lengd=Main.lengd+val
        Render.Render()

# def FLASHchange(val): # tharf ad adlaga fyrir prosentu
#     if 0<Main.FLASH+val<1:
#         Main.FLASH=Main.FLASH+val
#         Render.Render()


#create new custom scale.
def nyrskali():
    global note, es, cs, custom, skalar
    note=custom[7]
    for i in range (0,7):
        custom[i]=custom[i]-note
    if es !=0:
        # cs=np.append(cs[:es*8].copy(), custom.copy(), cs[es*8+8:].copy())
        es=0
    else:
        cs=np.append(cs, custom.copy())
    v=""
    for i in range (0,7):
        v+="note + "+str(custom[i])+", "
    v+="note"
    x="Main.skali=np.array(["+v+"])"
    skalar=np.append(skalar,x)
    custom=np.array([60, 60, 60, 60, 60, 60, 60, 60])

def customskali(val,i):
    if 0<=custom[i]+val<=127:
        custom[i]+=val
        skalarChange(1, 2)

def skalarChange(val,x):
    global note, currentscale, skalar
    if x==1:
        if 0<=note+value<=127:
            note+=value
    elif x==0:
        currentscale=(currentscale+val)%skalar.size
    if currentscale!=2:
        exec skalar[currentscale]
    Render.Render()

def customsetup():
    global currentscale, es, navy, navx, oldnavx, custom, skalar
    if currentscale>2:
        es=currentscale-3
        navy=3
        oldnavx=navx
        navx=0
        if es>0:
            custom=cs[(es-1)*8:(es-1)*8+8]

def barChange(val):
    x=math.pow(2,val)
    if 60/float(Main.tempo)/float(x*Main.bar/4):
        Main.bar*=x
        Render.Render()
