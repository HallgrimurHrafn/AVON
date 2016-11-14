import pygame
import serial
import random
from random import *

ser = serial.Serial('/dev/ttyAMA0',31250)
pygame.init()
clock = pygame.time.Clock()
channel=1
note_on=0x90+channel-1
note_off=0x80+channel-1
all_note_off=0xB0+channel-1

dt=0
x=12
value=100
note= 60
message=chr(all_note_off)+chr(123)+chr(0)
ser.write(message)
while True:
	message=chr(note_on)+chr(note)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(note_off)+chr(note)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(144)+chr(note+4)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(note_off)+chr(note+4)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(144)+chr(note+7)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(note_off)+chr(note+7)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(144)+chr(note+11)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(note_off)+chr(note+11)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(144)+chr(note+12)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(note_off)+chr(note+12)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(144)+chr(note+11)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(note_off)+chr(note+11)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(144)+chr(note+7)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(note_off)+chr(note+7)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(144)+chr(note+4)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
	message=chr(note_off)+chr(note+4)+chr(value)
	ser.write(message)
	dt = clock.tick(x)
