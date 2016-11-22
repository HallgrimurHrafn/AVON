from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import time

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

# import sys
# sys.path.insert(0, '../Src/') # So I can test functions in Render.py. Can delete this later.
# import Render
# import Main
# import glo

textbgr = (100,100,100)
tempo = 120

# Raspberry Pi config.
DC = 18
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0




# Usage:  portrait_position = portrait(landscape_position)
# Before: landscape_position is a pair of integers (x,y) indicating
#         coordinates on a plane where the origin (0,0) is the
#         top-left corner.
# After:  portrait_position is a pair of integers (u,v) indicating the
#         same location on the plane if the plane were rotated 90
#         degrees counterclockwise and the new origin is the top left
#         corner of the rotated plane.
def portrait(landscape_position):

    landscape_x = landscape_position[0]
    landscape_y = landscape_position[1]
    
    portrait_x = landscape_y
    portrait_y = 319-landscape_x

    return (portrait_x, portrait_y)

# Create TFT LCD display class.
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

# Initialize display.
disp.begin()

# Clear the display to a red background.
# Can pass any tuple of red, green, blue values (from 0 to 255 each).
disp.clear((0, 0, 0))

# Alternatively can clear to a black screen by calling:
# disp.clear()

def Avon():   # i put this here so we could get the logo on the screen when the program starts up.
    image = Image.open('avon.png')
    image = image.rotate(90).resize((240,320))
    disp.display(image)

# Define a function to create rotated text.  Unfortunately PIL doesn't have good
# native support for rotated fonts, but this function can be used to make a
# text image and rotate it so it's easy to paste in the buffer.
def draw_rotated_text(image, text, position, angle, font, fill=(255,255,255)):
    # Get rendered font width and height.
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    # Create a new image with transparent background to store the text.
    textimage = Image.new('RGBA', (width, height), (0,0,0,0))
    # Render the text.
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    # Rotate the text image.
    rotated = textimage.rotate(angle, expand=1)
    # Paste the text into the image, using it as a mask for transparency.
    image.paste(rotated, position, rotated)

def Main():

    # draw logo
    Avon()
    time.sleep(1)

    # Get a PIL Draw object to start drawing on the display buffer.
    draw = disp.draw()
    # draw a rectangle around text area for tempo, etc.
    draw.rectangle((0, 0, 59, 319), outline=(0,0,0), fill=textbgr)    
    # draw a rectangle around menu list
    draw.rectangle((59, 319, 239, 179), outline=(0,0,0), fill=textbgr)

    

    # Load default font.
#    font = ImageFont.load_default()
    
    # Alternatively load a TTF font.
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    font = ImageFont.truetype('Minecraftia-Regular.ttf', 18)

    # show bpm
    draw_rotated_text(disp.buffer, str(tempo)+' bpm', (14, 19), 90, font, fill=(255,255,255))
    
    
    # Write buffer to display hardware, must be called to make things visible on the
    # display!
    disp.display()
    
Main()
