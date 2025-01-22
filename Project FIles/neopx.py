import time
import board
import neopixel

def blink_neo_white():
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

    led.brightness = 0.3

    while True:
        led[0] = (255, 255, 255)
        time.sleep(1)
        led[0] = (0,0,0)
        break
