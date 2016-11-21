import Main
import midime
import glo
import threading
import time
import math



### TODO:
# laga fyrir skipt um function eda lengi ekki a mynd.
# function til ad breyta Main.x,y,z,seen.
# prufa pitch function
# control functions in general.

def cam():
    while Main.cam:
        t=math.fabs(time.time()-Main.tick)
        if Main.timi-t>=0:
            time.sleep(Main.timi-t)
        else:
            time.sleep(t-Main.timi)
        for blah in range (0,16):
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
                tick
            time.sleep(Main.timi/16*2+time.time()-t)

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

def sPitch(val):
    midime.tm(224+Main.voice, val ,0)
