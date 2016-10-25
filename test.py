    #!/usr/bin/env python
import time
import serial
import pygame
import struct

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
    ser.write(struct.pack(128))
    ser.write(struct.pack(60))
    ser.write(struct.pack(100))
    time.sleep(1)
    ser.write(struct.pack(144))
    ser.write(struct.pack(60))
    ser.write(struct.pack(0))
    counter += 1
    #print(counter)
