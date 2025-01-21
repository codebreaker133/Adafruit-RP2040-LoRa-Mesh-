import time, board, busio, digitalio, adafruit_rfm9x



def radio_setup(FREQ, NODE, tx_power, ack_dellay, destination_node):
    CS = digitalio.DigitalInOut(board.RFM_CS)
    RESET = digitalio.DigitalInOut(board.RFM_RST)

    # Initialize SPI bus.
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    # Initialze RFM radio
    RFM = adafruit_rfm9x.RFM(spi, CS, RESET, FREQ)
    RFM.node = NODE
    RFM.ack_delay = ack_dellay
    ack_failed_counter = 0
    counter = 0
    RFM.destination = destination_node
    RFM.send(bytes("startup message from node {}".format(RFM.node), "UTF-8"))
    return RFM



def Broadcast_send_contin(RFM):
    time_now = time.monotonic()
    transmit_interval = 10
    while True:
        # Look for a new packet: only accept if addresses to my_node
        if time.monotonic() - time_now > transmit_interval:
            # reset timeer
            time_now = time.monotonic()
            counter += 1
            # send a  mesage to destination_node from my_node
            if not RFM.send_with_ack(
                bytes("message from node node {} {}".format(RFM.node, counter), "UTF-8")
            ):
                ack_failed_counter += 1
                print(" No Ack: ", counter, ack_failed_counter)


