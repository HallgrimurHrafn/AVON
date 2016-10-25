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
    ser.write(struct.pack(hex("\x80\x3C\x64")))
    time.sleep(1)
    ser.write(struct.pack(hex("\x90\x3C\x00")))
    counter += 1
    #print(counter)
