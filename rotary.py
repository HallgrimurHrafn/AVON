import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click
GPIO.setup(33, GPIO.IN) # rotary left
GPIO.setup(31, GPIO.IN) # rotary right

def test(channel):
    print('yeei')
def left(channel):
    GPIO.remove_event_detect(31)
    print('left')
    GPIO.add_event_detect(31, GPIO.FALLING, callback=right, bouncetime=100)

def right(channel):
    GPIO.remove_event_detect(33)
    print('right')
    GPIO.add_event_detect(33, GPIO.FALLING, callback=left, bouncetime=100)

GPIO.add_event_detect(35, GPIO.RISING, callback=test, bouncetime=100)
GPIO.add_event_detect(33, GPIO.FALLING, callback=left, bouncetime=100)
GPIO.add_event_detect(31, GPIO.FALLING, callback=right, bouncetime=100)


while True:
    time.sleep(10)
