# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Example to receive addressed packed with ACK and send a response
# Author: Jerry Needell
#
import time
import board # type: ignore
import busio # type: ignore
import digitalio # type: ignore
import adafruit_rfm9x # type: ignore

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
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# set delay before transmitting ACK (seconds)
rfm9x.ack_delay = 0.1
rfm9x.enable_crc = True
# rfm9x.coding_rate = 8
rfm9x.spreading_factor = 12
# set node addresses
rfm9x.node = 2
rfm9x.destination = 1
# initialize counter
counter = 0
ack_failed_counter = 0
rfm9x.tx_power=23
import neopx
neopx.blink_neo_color(0, 255, 0)
# Wait to receive packets.
print("Waiting for packets...")
while True:
    # Look for a new packet: only accept if addresses to my_node
    packet = rfm9x.receive(with_ack=True, with_header=True)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        import neopx
        neopx.blink_neo_color(255, 255, 255)
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw header):", [hex(x) for x in packet[0:4]])
        print("Received (raw payload): {0}".format(packet[4:]))
        print("RSSI: {0}".format(rfm9x.last_rssi))
        # send response 2 sec after any packet received
        time.sleep(2)
        counter += 1
        # send a  mesage to destination_node from my_node
        if not rfm9x.send_with_ack(
            bytes("response from node {} {}".format(rfm9x.node, counter), "UTF-8")
        ):
            ack_failed_counter += 1
            print(" No Ack: ", counter, ack_failed_counter)
