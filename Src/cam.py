import Main
import midime
import glo
import threading


### TODO:
# laga fyrir skipt um function eda lengi ekki a mynd.
# function til ad breyta Main.x,y,z,seen.
# prufa pitch function
# control functions in general.

def cam():
    while Main.cam:
        time.sleep(Main.time-(time.time()-Main.tick))
        for blah in nrange (0,8):
            if not Main.cam:
                break
            if Main.seen:
                t1=threading.Thread(target=opperate, args=(glo.xcursor))
                t2=threading.Thread(target=opperate, args=(glo.ycursor))
                t3=threading.Thread(target=opperate, args=(glo.zcursor))
                if glo.xcursor==1 and blah==7:
                    t1.start()
                    print "x", glo.xcursor
                else:
                    t1.start()
                if glo.ycursor==1 and blah==7:
                    t2.start()
                else:
                    t2.start()
                if glo.zcursor==1 and blah==7:
                    t3.start()
                else:
                    t3.start()
            else:
                tick
            time.sleep(Main.timi/8)

def opperate(x):
    exec glo.mod[x]


def notes(note):
    midime.tm(144+Main.voice, note, 100)
    time.sleep(Main.timi-Main.timi*Main.lengd)
    midime(128, note, 0)

def pitch(val):
    midime.tm(224+Main.voice, 0 ,val)
