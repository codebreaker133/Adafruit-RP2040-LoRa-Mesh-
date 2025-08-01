from time import sleep
import board #type: ignore
import busio #type: ignore
import adafruit_ssd1327 #type: ignore
import displayio #type: ignore
from adafruit_display_text import label #type: ignore
#from displayio import I2CDisplay as I2CDisplayBus
import terminalio #type: ignore
# Release display resources at the start
displayio.release_displays()


print("All modules loaded successfully")
# Set up I2C interface
SDA = board.SDA #set board I2C Data pin
SCL = board.SCL #set board I2C Clock pin

i2c = busio.I2C(SCL, SDA) # use both I2C pins and initialise I2C bus

print("I2C started")
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
WIDTH = 128 #display width (pixels)
HEIGHT = 128 #display heighth (pixels)

display = adafruit_ssd1327.SSD1327(display_bus, width=WIDTH, height=HEIGHT, ) #start display object

splash = displayio.Group()
display.root_group = splash

def write_to_display(text):
    splash.pop() if len(splash) > 0 else None # if the length of data on screen /= 0 clear screen
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=3, y=60, scale=2) #format write string
    splash.append(text_area) # write formated string to screen

