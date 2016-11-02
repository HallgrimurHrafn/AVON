import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

left = 33
right = 31

x=False

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(right, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right

def test(channel):
    print('yeei')
def rotary(channel):
    global x, left, right
    x=(GPIO.input(left) and not GPIO.input(right)) and (GPIO.input(right) and not GPIO.input(left))
    print x

GPIO.add_event_detect(35, GPIO.RISING, callback=test, bouncetime=100)
GPIO.add_event_detect(left, GPIO.FALLING, callback=rotary, bouncetime=20)
GPIO.add_event_detect(right, GPIO.FALLING, callback=rotary, bouncetime=20)


while True:
    time.sleep(10)
