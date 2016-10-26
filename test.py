    #!/usr/bin/env python
import time
import serial
import pygame
import mido
import struct

ser = serial.Serial(
    port='/dev/serial1', #eda sys0 eda hvad sem hinn var.
    baudrate = 38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS,
    timeout=0
    )
#counter =0


while 1:
    time.sleep(1)
    ser.flushInput()
    x=ser.write(mido.Message('note_on', channel=0, note=60, velocity=100).hex())
    ser.flush()
    print(mido.Message('note_on', channel=0, note=60, velocity=100).hex())
    print(x)
    time.sleep(1)
    ser.flushInput()
    x=ser.write(mido.Message('note_off', channel=0, note=60, velocity=0).hex())
    ser.flush()
    print(mido.Message('note_off', channel=0, note=60, velocity=0).hex())
    print(x)
