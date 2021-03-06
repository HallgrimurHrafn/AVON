import numpy as np
import Main
import time
import math
import glo
import threading
import RPi.GPIO as GPIO
import cam
import Render




## TODO:
# hanna modetoggle fyrir cameru
# skroll i gegnum xyz control parametra fyrir cameru
# banna notenda ad transpose-a skala svo hann fari uppfyrir 127 eda nidurfyrir 0.

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
    if 0<=Main.v+val<=15:
        Main.v=Main.v+val
        Main.ChannelChange()
        renderchan = True # Print new channel on screen
        print Main.voice


def tempchange(val, x):
    if 60/float(Main.tempo+val*x)/float(Main.bar/4)>=0.05:
        Main.taptemp=0
        time.sleep(0.01)
        Main.tempo=Main.tempo+val*x
        Main.taptemp=1


def livechange():
    if Main.lGO==1:
        Main.lGO=0
    else:
        Main.lGO=1
    glo.renderlive = True # print new mode on screen
    Main.multithread()

def camerachange():
    if Main.cam:
        camoff()
    else:
        camon()
    # forrit sem uppfaerir cameramod

def camon():
    # if glo.xcursor or glo.ycursor or glo.zcursor==1:
    #     if Main.lGO==0:
    #         GPIO.remove_event_detect(4)
    Main.cam=True
    Main.seen=True
    t2=threading.Thread(target=cam.vision)
    t2.start()
    t=threading.Thread(target=cam.cam)
    t.start()

def camoff():
    # if glo.xcursor or glo.ycursor or glo.zcursor==1:
    #     if Main.lGO==0:
    #         GPIO.add_event_detect(4, GPIO.FALLING, callback=trellisWatch, bouncetime=350)
    Main.cam=False
    Main.seen=False


def cameraMode(val, xyz):
    if xyz==0:      # x
        glo.xcursor=(glo.xcursor + val)%glo.xmod.size
        print glo.xmod[glo.xcursor]
    elif xyz==1:    # y
        glo.ycursor=(glo.ycursor + val)%glo.ymod.size
        print glo.ymod[glo.ycursor]
    elif xyz==2:    # z
        glo.zcursor=(glo.zcursor + val)%glo.zmod.size
        print glo.zmod[glo.zcursor]

    # if glo.xcursor or glo.ycursor or glo.zcursor==1:
    #     if glo.stat==1:
    #         if Main.lGO==0:
    #             GPIO.remove_event_detect(4)
    #             glo.stat=0
    # else:
    #     if glo.stat==0:
    #         Main.multithread()
    #         glo.stat=1


def notelengdChange(val):
    val=-float(val)/20
    if 0<Main.lengd+val<1:
        Main.lengd=Main.lengd+val
        print Main.lengd


def barChange(val):
    x=math.pow(2,val)
    if 60/float(Main.tempo)/float(x*Main.bar/4)>=0.05:
        Main.bar*=x

# def FLASHchange(val): # tharf ad adlaga fyrir prosentu
#     if 0<Main.FLASH+val<1:
#         Main.FLASH=Main.FLASH+val

def skalarChange(val,x):
    if x==1:
        if 0<=glo.note+val<=127:
            glo.note+=val
            print glo.note
    elif x==0:
        glo.currentscale=(glo.currentscale+val)%glo.skalar.size
        print glo.currentscale
    if glo.currentscale!=3:
        exec glo.skalar[glo.currentscale]
        # print glo.skalar[glo.currentscale]    # adgerdin. debug
        print Main.newskali                     # nyji skalin. debug



def customskali(val,i):
    if 0<=glo.custom[i]+val<=127:
        glo.custom[i]+=int(val)
        Main.newskali=glo.custom.copy()



def customsetup():  # glo.currentscale verdur ad vera staerra en 2.
    if glo.currentscale>2:
        glo.es=glo.currentscale-3
        glo.navy=3
        glo.oldnavx2=glo.navx
        glo.navx=0
        if glo.es>0:
            glo.custom=np.array([glo.note + int(glo.cs[(glo.es-1)*8].copy())])
            for x in range (1,8):
                glo.custom=np.append(glo.custom, glo.note +  int(glo.cs[(glo.es-1)*8+x].copy()))

        else:
            glo.custom=np.array([glo.note, glo.note, glo.note, glo.note, glo.note, glo.note, glo.note, glo.note])


#create new glo.custom scale. thegar vid forum til baka i menu.
def nyrskali():
    print glo.es, glo.currentscale
    for i in range (0,8):
        glo.custom[i]=glo.custom[i]-glo.note
    if glo.es !=0:
        glo.cs=np.append(glo.cs[:(glo.es-1)*8].copy(), glo.custom.copy(), glo.cs[(glo.es-1)*8+7:].copy())
        glo.es=0
    else:
        glo.cs=np.append(glo.cs, glo.custom.copy())
    v=""
    for i in range (0,7):
        if i%3==2:
            v+="\n"
        v+="glo.note + "+str(glo.custom[i])+", "
    v+="glo.note + "+str(glo.custom[7]) +"]" + ")"
    x="Main.newskali=np.array(["+v
    if glo.currentscale==3:
        glo.skalar=np.append(glo.skalar,x)
        glo.currentscale=glo.skalar.size-1
    elif glo.currentscale>3:
        glo.skalar[glo.currentscale]=x
    # exec x   #otharfi thvi glo.customskali uppfaerir.
