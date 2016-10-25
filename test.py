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
    time.sleep(1)
    ser.write(80)
    ser.write(3C)
    ser.write(64)
    time.sleep(1)
    ser.write(90)
    ser.write(3C)
    ser.write(0)
    counter += 1
    #print(counter)
