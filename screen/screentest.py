from PIL import Image

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

# Raspberry Pi config.
DC = 18
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0

# TFT LCD display class
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

# Initialize display.
disp.begin()

#clear to white background
disp.clear((255,255,255))

# Load and image
print('Loading image')
image = Image.open('test.png')

# Resize and rotate
image = image.rotate(90).resize((240,320))

# Draw image
print('Drawing image')
disp.display(image)
