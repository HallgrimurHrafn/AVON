import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click
GPIO.setup(33, GPIO.IN) # rotary left
GPIO.setup(31, GPIO.IN) # rotary right

def test(channel):
    print('yeei')
def left(channel):
    print('left')

def right(channel):
    print('right')

GPIO.add_event_detect(35, GPIO.RISING, callback=test, bouncetime=100)
GPIO.add_event_detect(33, GPIO.FALLING, callback=left)
GPIO.add_event_detect(31, GPIO.FALLING, callback=right)


while True:
    time.sleep(10)
