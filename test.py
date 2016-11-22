import RPi.GPIO as GPIO
import time


def stopper():
    print "stoooopp!!!"


def playpause():
    print "PLAY"


def callback_tap():
    print "TAP-IT-NOW"


GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set up STOP button
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set up START button
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set up TAP button

GPIO.add_event_detect(38, GPIO.RISING, callback=stopper, bouncetime=200)
GPIO.add_event_detect(40, GPIO.RISING, callback=playpause, bouncetime=200)
GPIO.add_event_detect(36, GPIO.RISING, callback=callback_tap, bouncetime=200)


while True:
    time.sleep(10)
