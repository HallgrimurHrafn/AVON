import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# just for testing
tap_number = 0
tap = []
period = []
tempo = 120

# Set up 16, 20, and 21 as inputs.
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up TAP button
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up STOP button
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up START button

# Usage: tempo = calculate_tempo(tap)
# Before: tap is a nonempty list of floating point values, representing seconds.
# After: tempo contains the average bpm between the last two values in tap. For example, if tap = [
def calculate_tempo(tap, period, tempo):

    # add the newest tap time to the tap[] list.
    current_time = time.time()
    tap.append(current_time)

    tap_count = len(tap)


    if tap_count == 1: # not enough taps yet, so don't alter tempo.
        return tempo

    elif tap[-1] - tap[-2] >= 3: # if 3 seconds have passed between
                                 # last 2 taps erase all but last tap
                                 # time and do not alter tempo.
        tap = [tap[-1]]
        return tempo

    elif tap_count == 2:
        # add a new period (time between taps) but don't adjust tempo.
	    period.append(tap[-1]-tap[-2])
	    return tempo

    # else: # tap_count > 2:
    # add a new period and calculate tempo in bpm.
    period.append(tap[-1]-tap[-2])

    # if len(period) > 3: period = period[-3:] # use only the last three periods to take an average.
    # avg_period = sum(period) / len(period)

    avg_period = (period[-1]+period[-2]) / 2

    # new tempo in bpm = 60 sec / avg of last 2, rounded to nearest integer.
    new_tempo = int(round(60/avg_period))
    return new_tempo


# Usage: callback_tap(channel). runs whenever TAP button pressed.
# Before: global variable tempo is an integer.
# After: tempo = average tempo of last three taps.
def callback_tap(channel):

    global tap, period, tempo

    tempo = calculate_tempo(tap, period, tempo)
    print 'tempo =', tempo, 'bpm'


# run when STOP is pressed
def callback_stop(channel):
    print('STOP')

# run when START is pressed
def callback_start(channel):
    print('START')

# monitor inputs 16, 20, and 21 for button presses,
# disregard button "bounces" or presses faster than 100 ms
GPIO.add_event_detect(16, GPIO.FALLING, callback=callback_tap, bouncetime=200)
GPIO.add_event_detect(20, GPIO.FALLING, callback=callback_stop, bouncetime=200)
GPIO.add_event_detect(21, GPIO.FALLING, callback=callback_start, bouncetime=200)


# Keep this test program running until forced to quit.
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

#GPIO.cleanup()           # clean up GPIO on normal exit
