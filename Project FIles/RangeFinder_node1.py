
print("range finder node 1")


import time
import board # type: ignore
import busio # type: ignore
import digitalio # type: ignore

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip.
# set GPIO pins as necessary -- this example is for Raspberry Pi
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)
from adafruit_rfm import rfm9x #type: ignore
# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Initialze RFM radio
radio = rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

transmit_interval = 4.0
radio.enable_crc = True
radio.low_datarate_optimize = True
radio.coding_rate = 5 # accepted values are 5-8
radio.xmit_timeout = (transmit_interval - 0.25) # timeout for transmition time
radio.signal_bandwidth = 62500 # See accepted values in picture
radio.spreading_factor = 12 # accepted values are 7-12, 6 requiers special configuration (not suported here)
                           # 12 will give slowest troughput but highest range
                           # 6 is fastest but shortest range
# set node addresses
radio.node = 1
radio.destination = 2
radio.tx_power=23
import neoblink #type: ignore
# send startup message from node
neoblink.blink_neo_color(0, 255, 0, 1)
radio.send_with_ack(bytes("startup message from node {}".format(radio.node), "UTF-8"))

# Wait to receive packets.
print("Waiting for packets...")
# initialize flag and timer
time_now = time.monotonic()
while True:
    if time.monotonic() - time_now > transmit_interval:
        # reset timeer
        time_now = time.monotonic()
        counter += 1
        # send a mesage
        print("sending data")
        radio.send(bytes("test from:{}".format(radio.node), "UTF-8"))
        neoblink.blink_neo_color(000, 000, 255, 1)
        
