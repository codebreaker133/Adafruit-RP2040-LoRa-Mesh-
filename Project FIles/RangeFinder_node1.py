print("Hello World!")

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
from adafruit_rfm import rfm9x
# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Initialze RFM radio
radio = rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# set delay before sending ACK
radio.ack_delay = 0.2
radio.enable_crc = True
radio.coding_rate = 4
# radio.signal_bandwidth = 62.5
radio.spreading_factor = 9
# set node addresses
radio.node = 1
radio.destination = 2
# initialize counter
counter = 0
ack_failed_counter = 0
radio.tx_power=23
import neoblink
# send startup message from my_node
neoblink.blink_neo_color(0, 255, 0)
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
        print("Received (raw header):", [hex(x) for x in packet[0:4]])
        print("Received (raw payload): {0}".format(packet[4:]))
        print("RSSI: {0}".format(radio.last_rssi))
        neoblink.blink_neo_color(255, 0, 255)
        # send reading after any packet received
    
    if time.monotonic() - time_now > transmit_interval:
        # reset timeer
        time_now = time.monotonic()
        counter += 1
        # send a  mesage to destination_node from my_node
        neoblink.blink_neo_color(0, 0, 255)
        if not radio.send(
            bytes("message from node node {}".format(radio.node), "UTF-8")
        ):
            print("transmiting")            
            neoblink.blink_neo_color(000, 000, 255)
    if radio.packet_sent() == True:
            neoblink.blink_neo_color(255, 0, 255)
        
