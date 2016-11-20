import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set up STOP button


def stopper(channel):
    print "blah"

GPIO.add_event_detect(38, GPIO.BOTH, callback=stopper, bouncetime=50)

while True:
    time.sleep(10)
