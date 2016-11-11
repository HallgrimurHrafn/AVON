import numpy as np
import Render

# navigation tools.
navx=0          # visar sem benda a hvar vid erum i nav
navy=0
navz=0          # visir fyrir foll innan i nav.
navmax_z=np.zeros(('x', 'y'))     # x og y placeholder fyrir max fjolda optiona.
navmax_x=np.array([3, 2, 5])      # fylki fyrir max x, navmax_x.length=navmax_y
navmax_y=3                  # max dyppt y. 3 er placeholder.
nav=np.zeros(('x','y'))     # x og y placeholder fyrir max fjolda optiona.




def initNav():
    nav[0][0]="channelchange(val)"        # svona getum vid baett vid functions :D
    nav[0][1]="tempchange(val, 10)"
    nav[0][3]="livechange()"
    nav[0][4]="camerachange()"
    nav[0][5]="lengdChange(val)"
    nav[0][6]="FLASHchange(val)"

    nav[1][0]="tempchange(val, navz)"
    nav[1][1]="skalichange(val,navz)"


def move(i, val):
    if i==1:
        moveHorizontal(val)
    else:
        moveVertical(val)


def moveHorizontal(val):
    global navx, navmax_x, navy, navz
    if

def moveVertical(val):
    global navx, navz,

def click(i):
    if i==1:
        movedown()
    else:
        moveup()

def movedown():
    global navmax_y, navy
    if not (navy+1>navmax_y):
        navy+=1
        Render.Render()

def moveup():
    global navy
    if navy-1>0:
        navy+=1
        Render.Render()


def kort():
    global navy, navx, nav, navz
    exec nav(navy, navx)                    # ur nav er fall i streng,
#                                           # exec breytir i koda og keyrir fallid.

def channelchange(val):
    if 0<=Main.v+val<=15:
        Main.v=Main.v+val
        Main.ChannelChange()
        Render.Render()


def tempchange(val):
    if 0<=Main.tempo+val<=600:
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
