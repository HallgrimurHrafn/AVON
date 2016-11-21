import time
import glo


def screen():
    while True:
        print "x", glo.navx, "y", glo.navy
        time.sleep(2)
