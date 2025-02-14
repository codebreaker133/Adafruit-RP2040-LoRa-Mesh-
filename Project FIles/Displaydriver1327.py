from time import sleep
import board
import busio
import adafruit_ssd1327
import displayio
from adafruit_display_text import label
#from displayio import I2CDisplay as I2CDisplayBus
import terminalio
# Release display resources at the start
displayio.release_displays()


print("All modules loaded successfully")
# Set up I2C interface
SDA = board.SDA
SCL = board.SCL

i2c = busio.I2C(SCL, SDA)

print("I2C started")
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
WIDTH = 128
HEIGHT = 128

display = adafruit_ssd1327.SSD1327(display_bus, width=WIDTH, height=HEIGHT, )

splash = displayio.Group()
display.root_group = splash

def write_to_display(text):
    splash.pop() if len(splash) > 0 else None
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=3, y=60, scale=2)
    splash.append(text_area)

