import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

left = 33
right = 31

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(right, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right

def test(channel):
    print('yeei')
def rotary(left_or_right):
    print left
    print
    print right

GPIO.add_event_detect(35, GPIO.RISING, callback=test, bouncetime=100)
GPIO.add_event_detect(left, GPIO.FALLING, callback=rotary, bouncetime=75)
GPIO.add_event_detect(right, GPIO.FALLING, callback=rotary, bouncetime=75)


while True:
    time.sleep(10)
