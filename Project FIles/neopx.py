import time
import board
import neopixel

def blink_neo_color(r,g,b):
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

    led.brightness = 1
    print("makeing neopx blink")

    while True:
        led[0] = (r, g, b)
        time.sleep(1)
        led[0] = (0,0,0)
        led.deinit()
        break
