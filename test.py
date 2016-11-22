import RPi.GPIO as GPIO
import time


def stopper(channel):
    print "stoooopp!!!"


def playpause(channel):
    print "PLAY"


def callback_tap(channel):
    print "TAP-IT-NOW"


GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up STOP button
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up START button
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up TAP button

GPIO.add_event_detect(38, GPIO.FALLING, callback=stopper, bouncetime=200)
GPIO.add_event_detect(40, GPIO.FALLING, callback=playpause, bouncetime=200)
GPIO.add_event_detect(36, GPIO.FALLING, callback=callback_tap, bouncetime=200)


while True:
    time.sleep(10)
