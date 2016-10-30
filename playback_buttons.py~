import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

time_stamp = time.time() # used for debouncing and tap timing


# Set up 16, 20, and 21 as inputs. 
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up TAP button
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up STOP button
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up START button

# run whenever TAP is pressed
def callback_tap(channel):
    print('TAP')

# run when STOP is pressed
def callback_stop(channel):
    print('STOP')

# run when START is pressed
def callback_start(channel):
    print('START')

# monitor inputs 16, 20, and 21 for button presses, 
# disregard button "bounces" or presses faster than 100 ms
GPIO.add_event_detect(16, GPIO.FALLING, callback=callback_tap, bouncetime=100)
GPIO.add_event_detect(20, GPIO.FALLING, callback=callback_stop, bouncetime=100)
GPIO.add_event_detect(21, GPIO.FALLING, callback=callback_start, bouncetime=100)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit 
GPIO.cleanup()           # clean up GPIO on normal exit  

