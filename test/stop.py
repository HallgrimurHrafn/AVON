import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up STOP button


def stopper():
    print "blah"

GPIO.add_event_detect(38, GPIO.FALLING, callback=stopper, bouncetime=200)

while True:
    time.sleep(10)
