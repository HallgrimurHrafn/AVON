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
        for blah in range (0,8):
            t=time.time()
            if not Main.cam:
                break
            if Main.seen:
                t1=threading.Thread(target=opperate, args=(glo.xcursor,))
                t2=threading.Thread(target=opperate, args=(glo.ycursor,))
                t3=threading.Thread(target=opperate, args=(glo.zcursor,))
                if glo.xcursor==1 and blah==7 or glo.xcursor==1 and blah==3:
                    t1.start()
                    print "x", glo.xcursor
                else:
                    # t1.start()
                    pass
                if glo.ycursor==1 and blah==7 or glo.ycursor==1 and blah==3:
                    t2.start()
                else:
                    # t2.start()
                    pass
                if glo.zcursor==1 and blah==7 or glo.zcursor==1 and blah==3:
                    t3.start()
                else:
                    # t3.start()
                    pass
            else:
                tick
            time.sleep(Main.timi/8+time.time()-t)

def opperate(x):
    exec glo.mod[x]


def notes(note):
    midime.tm(144+Main.voice, note, 100)
    time.sleep(Main.timi-Main.timi*Main.lengd)
    midime.tm(128+Main.voice, note, 0)

def pitch(val):
    midime.tm(224+Main.voice, 0 ,val)
