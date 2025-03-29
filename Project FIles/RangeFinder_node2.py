# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Example to receive addressed packed with ACK and send a response
# Author: Jerry Needell
#
import time
import board # type: ignore
import busio # type: ignore
import digitalio # type: ignore

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip.
# set GPIO pins as necessary - this example is for Raspberry Pi
CS = digitalio.DigitalInOut(board.RFM_CS)
RESET = digitalio.DigitalInOut(board.RFM_RST)

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Initialze RFM radio
from adafruit_rfm import rfm9x
radio = rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# set delay before transmitting ACK (seconds)
radio.ack_delay = 0.2
radio.enable_crc = True
radio.coding_rate = 5
# radio.signal_bandwidth = 62500000
radio.spreading_factor = 9
# set node addresses
radio.node = 2
radio.destination = 1
# initialize counter
counter = 0
ack_failed_counter = 0
radio.tx_power=23
import neoblink
neoblink.blink_neo_color(0, 255, 0)
# Wait to receive packets.
print("Waiting for packets...")
while True:
    # Look for a new packet: only accept if addresses to my_node
    packet = radio.receive(with_header=True)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        neoblink.blink_neo_color(255, 255, 255)
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw header):", [hex(x) for x in packet[0:4]])
        print("Received (raw payload): {0}".format(packet[4:]))
        print("RSSI: {0}".format(radio.last_rssi))
        # send response 2 sec after any packet received
        time.sleep(2)
        counter += 1
        # send a  mesage to destination_node from my_node
        if not radio.send(
            bytes("response from node {} {}".format(radio.node, counter), "UTF-8")
        ):
            ack_failed_counter += 1
            print(" No Ack: ", counter, ack_failed_counter)
