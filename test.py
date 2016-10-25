    #!/usr/bin/env python
import time
import serial
import pygame
import struct

ser = serial.Serial(
    port='/dev/serial1', #eda sys0 eda hvad sem hinn var.
    baudrate = 38400,
    #parity=serial.PARITY_NONE,
    #stopbits=serial.STOPBITS_ONE,
    #bytesize=serial.EIGHTBITS,
    #timeout=1)
#counter =0
#while 1:
#    time.sleep(1)
#    ser.write(struct.pack("\x80\x3C\x64"))
#    time.sleep(1)
#    ser.write(struct.pack("\x90\x3C\x00"))
#    counter += 1
#    #print(counter)


message = [0, 0, 0]
while True:
    i = 0
    while i < 3:
        data = ord(ser.read(1)) # read a byte
        if data >> 7 != 0:  
            i = 0      # status byte!   this is the beginning of a midi message!
        message[i] = data
        i += 1
        if i == 2 and message[0] >> 4 == 12:  # program change: don't wait for a
            message[2] = 0                      # third byte: it has only 2 bytes
            i = 3

    messagetype = message[0] >> 4
    messagechannel = (message[0] & 15) + 1
    note = message[1] if len(message) > 1 else None
    velocity = message[2] if len(message) > 2 else None

    if messagetype == 9:    # Note on
        print 'Note on'
    elif messagetype == 8:  # Note off
        print 'Note off'            
    elif messagetype == 12: # Program change
        print 'Program change'
