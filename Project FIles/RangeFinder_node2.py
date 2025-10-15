
print("Range Finder Node 2")
import time
import board # type: ignore
import busio # type: ignore
import digitalio # type: ignore

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip.
# set GPIO pins as necessary
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Initialze RFM
from adafruit_rfm import rfm9x #type: ignore
radio = rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

radio.enable_crc = True
radio.low_datarate_optimize = True
radio.coding_rate = 5 # accepted values are 5-8
radio.signal_bandwidth = 62500
radio.receive_timeout = 3 #receive timieout for radio (changes depending on packet length)
radio.spreading_factor = 12 # accepted values are 7-12 6 requiers special configuration (not suported here)
                           # 12 will give slowest troughput but highest range
                           # 6 is fastest but shortest range
# set node addresses
radio.node = 2
radio.destination = 1
# initialize counter
counter = 0
ack_failed_counter = 0
radio.tx_power=23
import neoblink #type: ignore
neoblink.blink_neo_color(0, 255, 0, 0.5)
# Wait to receive packets.
print("Waiting for packets...")
while True:
    # Look for a new packet: only accept if addresses to my_node
    packet = radio.receive()
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        neoblink.blink_neo_color(255, 255, 255, 0.5)
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("RSSI: {0}".format(radio.last_rssi))
