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
    stri="80\3C\64"
    ser.write(stri)
    time.sleep(1)
    stri="90\3C\0"
    ser.write(stri)
    counter += 1
    #print(counter)
