    #!/usr/bin/env python
import time
import serial
import pygame

ser = serial.Serial(
	port='/dev/ttyAMA0',
    baudrate = 31250,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)
var counter =0
while 1:
	ser.write('Write counter: %d \n'%(counter))
	time.sleep(1)
	counter += 1