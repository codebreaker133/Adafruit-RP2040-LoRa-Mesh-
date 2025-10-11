
print("range finder node 1")

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Example to send a packet periodically between addressed nodes with ACK
# Author: Jerry Needell
#
import time
import board # type: ignore
import busio # type: ignore
import digitalio # type: ignore
# import adafruit_rfm9x #type: ignore
# set the time interval (seconds) for sending packets
transmit_interval = 2.0

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

radio.enable_crc = True
radio.coding_rate = 5 # accepted values are 5-8
radio.signal_bandwidth = 62500 # See accepted values in picture
radio.spreading_factor = 12 # accepted values are 7-12, 6 requiers special configuration (not suported here)
                           # 12 will give slowest troughput but highest range
                           # 6 is fastest but shortest range
# set node addresses
radio.node = 1
radio.destination = 2
# initialize counter
counter = 0
ack_failed_counter = 0
radio.tx_power=23
import neoblink #type: ignore
# send startup message from my_node
neoblink.blink_neo_color(0, 255, 0, 1)
radio.send_with_ack(bytes("startup message from node {}".format(radio.node), "UTF-8"))

# Wait to receive packets.
print("Waiting for packets...")
# initialize flag and timer
time_now = time.monotonic()
while True:
    # Look for a new packet: only accept if addresses to my_node
    packet = radio.receive(with_header=True)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("RSSI: {0}".format(radio.last_rssi))
        neoblink.blink_neo_color(255, 0, 255, 1)
        # send reading after any packet received
    
    if time.monotonic() - time_now > transmit_interval:
        # reset timeer
        time_now = time.monotonic()
        counter += 1
        # send a  mesage to destination_node from my_node
        print("sending data")
        radio.send(bytes("message from node node {}".format(radio.node), "UTF-8"))
        neoblink.blink_neo_color(000, 000, 255, 1)
        
