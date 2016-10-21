from time import sleep
import RPi.GPIO as GPIO

pin =37  #ma stilla a flest allt held eg. endilega prufa. thetta er int virinn ur trellis.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def blah():
	time.sleep(0.01)
	if GPIO.input(37) == GPIO.HIGH:
		print('high')	
	if GPIO.input(37) == GPIO.LOW:
		print('low')



while True:
	blah()
