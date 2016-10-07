import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 8

GPIO.setup(led,GPIO.OUT)
print("Light on")
GPIO.output(led,GPIO.HIGH)
time.sleep(1)
print("Light off")
GPIO.output(led,GPIO.LOW)
GPIO.cleanup()