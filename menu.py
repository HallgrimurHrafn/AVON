import numpy as np
import Render

# navigation tools.
navx=0          # visar sem benda a hvar vid erum i
navy=0
navz=0
navmax_z=np.zeros(('x', 'y'))     # x og y placeholder fyrir max fjolda optiona.
navmax_x=np.array([3, 2, 5])      # fylki fyrir max x, navmax_x.length=navmax_y
navmax_y=3                  # max dyppt y. 3 er placeholder.
nav=np.zeros(('x','y'))     # x og y placeholder fyrir max fjolda optiona.




def initNav():
    nav[0][0]="tempchange()"
    nav[0][1]="function"        # svona getum vid baett vid functions :D

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
    global navy, navx, nav
    exec nav(navx, navy)                    # ur nav er fall i streng,
#                                           # exec breytir i koda og keyrir fallid.

def tempchange():
    global navz
    if 0<=Main.tempo+navz<=600:
        Main.taptemp=0
        time.sleep(0.01)
        Main.tempo=Main.tempo+navz
        Main.taptemp=1


# sma documentation
# um hvad tharf ad gera til ad breyta sumum hlutum i
# main fallinu til ad fa effect.

# breyta tempo:
# 1.)   Main.taptemp=0              # af virkja tap tempo a medan
# 2.)   Main.tempo= <value>         # velja tempo
# 3.)   Main.taptemp=1              # virkja tap tempo aftur.

# stylla lengd notu, prosenta af 1. hversu lengi notan lifir yfir 1 slag.
# 1.)   Main.lengd=<value>          # 0<value<1.
#                                   # 0.1 thydir ad notan lifi 90% af timanum.

# stylla lengdina a taktmaelis flashi.
# 1.)   Main.FLASH=<value>          # 0<value<1, i hlutfalli vid tempo.


# skipta um channel/voice/whatever
# 1.)   Main.v=<value>              # value verdur rasin.
# 2.)   Main.ChannelChange()        # ser algjorlega um skiptinguna.

#  liveplay
# 1.)   Main.lGO=1 eda 0            # 0 kveikir og 1 slekkur
# 2.)   Main.multithread()          # held thetta aetti ad duga. tharf ad testa


# skali
# 1.)   Main.skali[i]=<value>       # i visar til trellis, 7 fyrir botm, 0 fyrir top
#                                   # 0<value<128,  MIDI nota.
#                                   # breytir ollum channelum...
