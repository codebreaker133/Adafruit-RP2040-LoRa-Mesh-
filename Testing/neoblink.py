import time
import board
import neopixel

def blink_neo_color(r,g,b,times):
    led = neopixel.NeoPixel(board.NEOPIXEL, 1) #start connection with neopx
    led.brightness = 1
    while True:
        led[0] = (r, g, b)
        time.sleep(times)
        led[0] = (0,0,0)
        led.deinit() # close connection with neopx
        break
