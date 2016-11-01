import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click

def test(channel):
    print('yeei')

GPIO.add_event_detect(35, GPIO.FALLING, callback=test, bouncetime=200)
while True:
    time.sleep(10)
