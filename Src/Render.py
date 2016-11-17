import Main
import glo
import threading
import time
from PIL import Image
import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

# Raspberry Pi config.
DC = 18
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0

last=time.time()
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))
disp.begin()
disp.clear()

### TODO:
# Create the ability to scroll through the list on the left.
#   since there are more options than we can easily fit on the left we need
#   to be able to scroll through it. I reccomend using a global variable page
#   to indicate screen page. if page =1 it changes the location for objects on
#   screen such that all items are 2 levels higher. top 2 items will be gone.
#   for the bottom we shouldnt be able to scroll lower than the length of the item
#   list. If there is an odd number of items. The lowest item should be a blank rather
#   than a placeholder text.  THIS IS UP TO YOU TO DESIGN THOUGH.
#
# Custom scale on the screen. if we are editing scales the uppermost interface of
#   the 3 chunks needs to be cleared and only have the name of the scale (custom1, custom2 or
#   creating new custom depending on glo.currentscale, names are up to you) as well as each
#   note appearing on the screen such that 60 -> c3. a good way to do this is midi#//12=the number
#   and midi#%12 is the note. so from 61 we'd get 4 and 1. have a string matrix of length 12 that
#   maps such that string[1]="C#".
#
# create the function below named cursor. it should take glo.cursor and give you the location
#   as well as the type of cursor you need and draw it. use it in Render. You need to add
#   the locations to glo.cursor yourself. give them their own colors. That should
#   help the user locate it more easily.
#
# create the function below named chunk. it should be used to enter the items in the list
#   as well as their location and should put it on the screen. Think of Render as a
#   system to put all the blocks on the screen through functions and afterward it updates the
#   display it self.
#
# create the function below named camera. it should only be called if Main.seen=True.
#   its result should be that x and y are intersecting perpendicular lines and z should be a radius
#   of a filled circle formed at their intersection.
#
# if glo.navy=4 then we are editing the functions for x,y,z from the camera. their functions have
#   as of this moment in time not been defined but the top chunk of the 3 should be changed so that
#   we instead show x: blah  y:blah  z:blah. where they'd be propperly spaced and blah would be replaced
#   with their function. I imagine you will need to create a string array to display the functions as
#   text rather then some silly numbers :)
#
# Try to store variables in glo.py... eventually I'd prefer to have most programs only functions and
#   all variables located seperately. it makes it easier for usage.


### NOTE:
# helpful stuff https://learn.adafruit.com/user-space-spi-tft-python-library-ili9341-2-8?view=all
# The part of the screen that is dedicated to the camera is 180x180 px
# The screen is 240x320px
# more than ~5 frames per second won't work!
#
# glo variables:
# glo.cursor[navy][navx]  - locations for cursor to be, and whether the cursor
#   is > or _. 1 for > and 0 for _.
# glo.currentscale points to type of scale. for it the text must say:
#   0: Dur (or major), 1: moll (or minor), 2:penta, 3: CreateCustomScale (or just something intuitive)
#   4 and forward: custom +str(glo.currentscale-3).
# glo.note is the base note for the scale we are in. MIDIformat, needs to be visualized differently
#
# Main variables
# camera options. Main.x, Main.y and Main.z give you the location of the camera.
#   Main.cam is a boolean value whether or not the cam is on. Main.seen is a boolean
#   whether object is spotted. if false, dont draw based on x,y,z.
# Main.bar is the type of note we are playing. on default it is 8. 4 would be a quareter note.
# Main.tempo is explains it self.
# Main.lGO is 1 or 0. it stands for livemode on or off.
# Main.voice is the channel we are on. it range is (0,15), kindly visulize as (1,16)
# 1-Main.length is a percentage of tempo that the note plays for.
#
# finally I reccomend you keeping colors and such as a global variable. that makes it easier
#   for us to mess with it to get a good luck once everything is set up.

# I think this is it. GO CRAZY!!!


def Avon():   # i put this here so we could get the logo on the screen when the program starts up.
    image = Image.open('avon.png')
    image = image.rotate(90).resize((240,320))
    disp.display(image)


def Render():
    global last
    last2=time.time()  # a little something since the screen cant handle more than
    if last2>last+0.2  # more than 5 frames per second.
        return thebuffer()
    last=last2

    print "navx",glo.navx,"navy",glo.navy

def thebuffer():
    time.sleep(0.2)
    Render()

def cursor(location, type):
    pass

def chunk(location, text):
    pass

def camera(x,y,z):
    pass
