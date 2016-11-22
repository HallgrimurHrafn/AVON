import Main
import midime
import glo
import threading
import time
import math
import os



### TODO:
# laga fyrir skipt um function eda lengi ekki a mynd.
# function til ad breyta Main.x,y,z,seen.
# prufa pitch function
# control functions in general.

def vision():
    # os.getcwd()
    # os.path.exists('/test2')
    x=[False,3,2,1]

    while Main.cam:
        f = open(os.path.join('../vision/build', "XYZ.txt"), 'r')
        z=0
        for line in f:
            if z==0:
                if line == "True\n":
                    x[z]=True
                else:
                    x[z]=True
            else:
                x[z]=int(line)
            z+=1
        Main.seen=x[0]
        Main.x=x[1]
        Main.y=x[2]
        Main.z=x[3]
        time.sleep(0.05)



def cam():
    while Main.cam:
        t=math.fabs(time.time()-Main.tick)
        if Main.timi-t>=0:
            time.sleep(Main.timi-t)
        else:
            time.sleep(t-Main.timi)
        print Main.x, Main.y, Main.z
        for blah in range (0,8):
            t=time.time()
            if not Main.cam:
                break
            if Main.seen:
                t1=threading.Thread(target=opperate, args=(1,))
                t2=threading.Thread(target=opperate, args=(2,))
                t3=threading.Thread(target=opperate, args=(3,))
                if glo.xcursor==1 and blah==0:
                    t1.start()
                else:
                    if glo.xcursor !=1:
                        exec glo.xmod[glo.xcursor]
                    # pass
                if glo.ycursor==1 and blah==0:
                    t2.start()
                else:
                    if glo.ycursor != 1:
                        exec glo.ymod[glo.ycursor]
                    # pass
                if glo.zcursor==1 and blah==0:
                    t3.start()
                else:
                    if glo.zcursor != 1:
                        exec glo.zmod[glo.zcursor]
                    # pass
            else:
                pass
                # revert to normal!
            if blah !=7:
                time.sleep(Main.timi/8+time.time()-t)

def opperate(x):
    if x==1:
        exec glo.xmod[glo.xcursor]
    if x==2:
        exec glo.ymod[glo.ycursor]
    if x==3:
        exec glo.zmod[glo.zcursor]


def notes(note):
    midime.tm(144+Main.voice, note, 100)
    time.sleep(Main.timi-Main.timi*Main.lengd)
    midime.tm(128+Main.voice, note, 0)


def bPitch(val):
    midime.tm(224+Main.voice, 0 ,val)


def modwheel(val):
    midime.tm(176+Main.voice, 1, val)
