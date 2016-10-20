from time import sleep
import RPi.GPIO as GPIO

pin =37  #ma stilla a flest allt held eg. endilega prufa. þetta er int vírinn úr trellis.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def my_callback(channel):
    print("UPDate!")

                                    # stop detection for 0.1 sec
    GPIO.remove_event_detect(pin)     # þessum 2 linum ma mögulega sleppa. ef forritid virkar. prufa ad komenta ut linur
    sleep(0.1)                        # 14-16 og sja hvort thad virki enn.
    GPIO.add_event_detect(pin, GPIO.RISING, callback=my_callback, bouncetime=300)

GPIO.add_event_detect(pin, GPIO.RISING, callback=my_callback, bouncetime=300) #bouncetime.. lesa https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

# you can continue doing other stuff here
while True:
    pass