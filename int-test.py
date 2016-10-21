import time
import RPi.GPIO as GPIO
import Adafruit_Trellis


matrix0 = Adafruit_Trellis.Adafruit_Trellis()
matrix1 = Adafruit_Trellis.Adafruit_Trellis()
matrix2 = Adafruit_Trellis.Adafruit_Trellis()
matrix3 = Adafruit_Trellis.Adafruit_Trellis()


trellis = Adafruit_Trellis.Adafruit_TrellisSet(matrix0, matrix1, matrix2, matrix3)

I2C_BUS = 1

trellis.begin((0x70,  I2C_BUS), (0x71, I2C_BUS), (0x72, I2C_BUS), (0x73, I2C_BUS))


pin =37  #ma stilla a flest allt held eg. endilega prufa. thetta er int virinn ur trellis.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def blah():
	time.sleep(0.01)
	if GPIO.input(37) == GPIO.HIGH:
		print('high')	
	if GPIO.input(37) == GPIO.LOW:
		print('low')



while True:
	blah()
