
import time, board, busio, digitalio, adafruit_rfm9x


def interface_radio(FREQ, NODE, tx_power, ack_dellay, destination_node):
    CS = digitalio.DigitalInOut(board.RFM_CS)
    RESET = digitalio.DigitalInOut(board.RFM_RST)

    # Initialize SPI bus.
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    # Initialze RFM radio
    RFM = adafruit_rfm9x.RFM(spi, CS, RESET, FREQ)

    RFM.node = NODE
    RFM.ack_delay = ack_dellay
    RFM.destination = destination_node
    if tx_power == "full":
        RFM.tx_power = 23
    else:
        RFM.tx_power = tx_power
    RFM.send(bytes("startup message from node {}".format(RFM.node), "UTF-8"))
    import radioterminal
    rt = radioterminal
    radioterm = True
    # if board.BOOT == True:
    #     import neopx
    #     neopx.blink_neo_red()
    while radioterm == True:
        radioterm, typeSelect, data = rt.radioterm()
        if typeSelect == "b":
            counter, sent = Broadcast_send(RFM, data)
            if sent == False:
                import terminal
                if terminal.confirmation() == True:
                    counter, sent = Broadcast_send(RFM, data)
                elif terminal.confirmation() == False:
                    radioterm = True
        if typeSelect == "blink neo" or "ds":

            Broadcast_send(RFM, data)
    


    



def Broadcast_send(RFM, data):
    time_now = time.monotonic()
    transmit_interval = 5
    counter = 0
    while True:
        if time.monotonic() - time_now > transmit_interval:
            # reset timeer
            time_now = time.monotonic()
            counter += 1
            # send a  mesage to all nodes            
            if RFM.send(data, keeplisting=False, destination=255, node=1) == True:
                print(" message sent! counter= "+counter)
                sent = True
                return counter, sent
            else:
                print("message failed to send! counter= "+counter)
                sent = False
                return counter, sent


