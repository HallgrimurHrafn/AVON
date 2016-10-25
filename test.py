    #!/usr/bin/env python
import time
import serial
import pygame

ser = serial.Serial(
	port='/dev/serial1', #eda sys0 eda hvad sem hinn var.
    baudrate = 38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)
counter =0
while 1:
	#ser.write('Write counter: %d \n'%(counter))
	time.sleep(1)
	counter += 1
	print(counter)
