import numpy as np
import Render
import Main
import time
import math
import glo
import config

## TODO:
# a glo.custom skali ad bua til glo.note midad vid grunnton eda vid global breytuna glo.note.
# hanna modetoggle fyrir cameru
# skroll i gegnum xyz control parametra fyrir cameru

# allar breytur eru geymdar i glo.py

def move(i, val):
    if i==0:
        kort(0,val)
    else:
        kort(1,val)


def click(i):
    if i==1:
        kort(2,0)
    else:
        moveup()


def moveup():
    if glo.navy==3:
        nyrskali()
        glo.navy=2
        glo.navx=glo.oldnavx2
    elif glo.navy>0:
        glo.navy=0
        glo.navx=glo.oldnavx
        Render.Render()


def kort(x,val):
    if x==0:
        print glo.fScrollMapX[glo.navy][glo.navx]
        exec glo.fScrollMapX[glo.navy][glo.navx]
    elif x==1:
        print glo.fScrollMapY[glo.navy][glo.navx]
        exec glo.fScrollMapY[glo.navy][glo.navx]
    elif x==2:
        print glo.fClickMap[glo.navy][glo.navx]
        exec glo.fClickMap[glo.navy][glo.navx]
    #                               # exec breytir i koda og keyrir fallid.


def channelchange(val):
    if 0<=config.v+val<=15:
        config.v=config.v+val
        Main.ChannelChange()
        Render.Render()


def tempchange(val, x):
    if 60/float(Main.tempo+val*x)/float(Main.bar/4)>=0.05:
        config.taptemp=0
        time.sleep(0.01)
        Main.tempo=Main.tempo+val
        config.taptemp=1
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

def notelengdChange(val):
    val=float(val/20)
    if 0<Main.lengd+val<1:
        Main.lengd=Main.lengd+val
        Render.Render()

# def FLASHchange(val): # tharf ad adlaga fyrir prosentu
#     if 0<Main.FLASH+val<1:
#         Main.FLASH=Main.FLASH+val
#         Render.Render()


#create new glo.custom scale. thegar vid forum til baka i menu.
def nyrskali():
    glo.note=glo.custom[7]
    for i in range (0,7):
        glo.custom[i]=glo.custom[i]-glo.note
    if glo.es !=0:
        # glo.cs=np.append(glo.cs[:glo.es*8].copy(), glo.custom.copy(), glo.cs[glo.es*8+8:].copy())
        glo.es=0
    else:
        glo.cs=np.append(glo.cs, glo.custom.copy())
    v=""
    for i in range (0,7):
        v+="glo.note + "+str(glo.custom[i])+", "
    v+="glo.note"
    x="Main.skali=np.array(["+v+"])"
    if glo.currentscale==3:
        glo.skalar=np.append(glo.skalar,x)
        glo.currentscale=glo.skalar.size-1
    elif glo.currentscale>3:
        glo.skalar[glo.currentscale]=x
    # exec x   #otharfi thvi glo.customskali uppfaerir.
    Render.Render()

def customskali(val,i):
    if 0<=glo.custom[i]+val<=127:
        glo.custom[i]+=val
        Main.skali=glo.custom.copy()
        Render.Render()


def skalarChange(val,x):
    if x==1:
        if 0<=glo.note+value<=127:
            glo.note+=value
    elif x==0:
        glo.currentscale=(glo.currentscale+val)%glo.skalar.size
    if glo.currentscale!=2:
        exec glo.skalar[glo.currentscale]
    Render.Render()

def customsetup():
    if glo.currentscale>2:
        glo.es=glo.currentscale-3
        glo.navy=3
        glo.oldnavx2=glo.navx
        glo.navx=0
        if glo.es>0:
            glo.custom=glo.cs[(glo.es-1)*8:(glo.es-1)*8+8]
        else:
            glo.custom=np.array([glo.note, glo.note, glo.note, glo.note, glo.note, glo.note, glo.note, glo.note])

def barChange(val):
    x=math.pow(2,val)
    if 60/float(Main.tempo)/float(x*Main.bar/4)>=0.05:
        Main.bar*=x
        Render.Render()
