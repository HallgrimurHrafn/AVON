from PIL import Image
import ImageDraw
import ImageFont

import time

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

import sys
sys.path.insert(0, '../Src/') # So I can test functions in Render.py. Can delete this later.
# import Render

# import Main
import glo

textbgr = (100,100,100)
tempo = 120

# Raspberry Pi config.
DC = 18
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0




# TFT LCD display class
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

draw=disp.draw()

def Avon():   # i put this here so we could get the logo on the screen when the program starts up.
    image = Image.open('avon.png')
    image = image.rotate(90).resize((240,320))
    disp.display(image)


# Initialize display.
disp.begin()

#clear to black background
disp.clear((0,0,0))

# Load and image
print('Loading AVON image')
Avon()

time.sleep(10)

#clear to white background
disp.clear((255,255,255))

draw.rectangle((0, 0, 239, 319), fill=textbgr)

font = ImageFont.load_default()

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

def draw_rotated_text(image, text, position, angle, font, fill=(100,100,100)):
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

# Write two lines of white text on the buffer, rotated 90 degrees counter clockwise.
draw_rotated_text(disp.buffer, str(tempo)+' bpm' , portrait([300, 120]), 90, font, fill=textbgr)

draw_rotated_text(disp.buffer, 'KHSB-8', (170, 90), 90, font, fill=(255,255,255))
