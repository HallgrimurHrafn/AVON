import numpy as np
import Render

# navigation tools.
navx=0          # visar sem benda a hvar vid erum
navy=0

#fClickMap er map fyrir functions eftir thvi hvar vid erum i menu-inu ef klikkad er.
fClickMap=np.chararray((4,8), itemsize=25)         # max 25 stafir.. haegt ad auka.
fClickMap[:][:]="pass"

# multiple lines fyrir exec.
# x= """
# blah
# blah
# """.



#fScrollMap er map fyrir functions eftir thvi hvar vid erum i menu-inu. scrollfunctions
fScrollMap=np.chararray((4,8), itemsize=25)
fScrollMap[:][:]="pass"
# globalRelated change
fScrollMap[1][0]="channelchange(val)"   # svona getum vid baett vid functions :D
fScrollMap[1][1]="tempchange(val, 5)"
fScrollMap[1][3]="livechange()"
fScrollMap[1][4]="camerachange()"
fScrollMap[1][5]="lengdChange(val)"
fScrollMap[1][6]="FLASHchange(val)"

# tempchange
fScrollMap[2][0]="tempchange(val, 100)"
fScrollMap[2][1]="tempchange(val, 10)"
fScrollMap[2][2]="tempchange(val, 1)"

# skalichange
for x in range (0,8):
    fScrollMap[3][x]="skalichange(val,"
    fScrollMap[3][x]+=str(7-x)+")"

# ChannelRelated layer 1
# fScrollMap[4][0]=
# fScrollMap[4][1]=
# fScrollMap[4][2]=


def move(i, val):
    if i==1:
        moveHorizontal(val)
    else:
        moveVertical(val)


def moveHorizontal(val):
    global navx, navy
    if

def moveVertical(val):
    global navx

def click(i):
    if i==1:
        movedown()
    else:
        moveup()

def movedown():
    global fClickMap
    kort(fClickMap)

def moveup():
    global navx
    if navy-1>0:
        navy-=1
        navx=oldnavx
        Render.Render()


def kort(matrix):
    global navy, navx               # matrix er annad hvort nav eda
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


def lengdChange(val): # tharf ad adlaga fyrir prosentu
    if 0<Main.lengd+val<1:
        Main.lengd=Main.lengd+val
        Render.Render()

def FLASHchange(val): # tharf ad adlaga fyrir prosentu
    if 0<Main.FLASH+val<1:
        Main.FLASH=Main.FLASH+val
        Render.Render()

def skalichange(val,i):
    if 0<i<15:
        if 0<=Main.skali[i]+val<128:
            Main.skali[i]=Main.skali[i]+val
            Render.Render()

# sma documentation
# um hvad tharf ad gera til ad breyta sumum hlutum i
# main fallinu til ad fa effect.


# stylla lengd notu, prosenta af 1. hversu lengi notan lifir yfir 1 slag.
# 1.)   Main.lengd=<value>          # 0<value<1.
#                                   # 0.1 thydir ad notan lifi 90% af timanum.

# stylla lengdina a taktmaelis flashi.
# 1.)   Main.FLASH=<value>          # 0<value<1, i hlutfalli vid tempo.
