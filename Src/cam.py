import Main
import midime
import glo
import threading

def cam():
    while True:
        if not Main.cam:
            return
        if Main.seen:
            t1=threading.Thread(target=None, args=(0))
            t1.start()
            t2=threading.Thread(target=None, args=(1))
            t2.start()
            t3=threading.Thread(target=None, args=(2))
            t3.start()
            time.sleep(Main.timi)

def opperate(x):
    if x==0:
        exec glo.xmod[glo.xcursor]
    if x==1:
        exec glo.ymod[glo.ycursor]
    if x==2:
        exec glo.zmod[glo.zcursor]


def notes(note):
    midime.tm(144, note, 100)
    time.sleep(Main.timi-Main.timi*Main.lengd)
    midime(128, note, 0)
