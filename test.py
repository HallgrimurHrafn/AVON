#!/usr/bin/env python
import time
import serial
import pygame
import mido   # info fyrir mido. https://mido.readthedocs.io/en/latest/ports.html
import struct

ser = serial.Serial(
    port='/dev/ttyAMA0', # thetta er serialportid a raspberry.
    baudrate = 38400,
    parity=serial.PARITY_NONE,       # latum RS3232 sja um thetta.
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False
    # timeout=0
)
#counter =0

t=time.time()
while True:

    ser.write(hex(5))
