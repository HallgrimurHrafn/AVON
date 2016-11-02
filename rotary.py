import RPi.GPIO as GPIO
import time
import threading


GPIO.setmode(GPIO.BOARD)

left = 33
right = 31
cl=0
cr=0
x=False

lock=threading.Lock()

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary click
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary left
GPIO.setup(right, GPIO.IN, pull_up_down=GPIO.PUD_UP) # rotary right

def test(channel):
    print('yeei')
def rotary(channel):
    global x, left, right, cl, cr, lock
    if cl ==GPIO.input(left) and cr==GPIO.input(right):
        return
    cl=GPIO.input(left)
    cr=GPIO.input(right)
    lock.acquire()
    if GPIO.input(right)==GPIO.input(left):
        return
    if GPIO.input(left)>GPIO.input(right):
        print 'left'
    elif GPIO.input(right)>GPIO.input(left):
        print 'right'
    lock.release()

GPIO.add_event_detect(35, GPIO.RISING, callback=test, bouncetime=100)
GPIO.add_event_detect(left, GPIO.FALLING, callback=rotary)
GPIO.add_event_detect(right, GPIO.FALLING, callback=rotary)


while True:
    time.sleep(10)
