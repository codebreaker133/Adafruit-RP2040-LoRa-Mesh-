
import time, board, busio, digitalio, adafruit_rfm9x


def interface_radio(FREQ, NODE, tx_power, ack_dellay, destination_node):
    CS = digitalio.DigitalInOut(board.RFM_CS)
    RESET = digitalio.DigitalInOut(board.RFM_RST)
    
    # Initialize SPI bus.
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    # Initialze RFM radio
    RFM = adafruit_rfm9x.RFM9x(spi, CS, RESET, int(FREQ))

    RFM.node = int(NODE)
    RFM.ack_delay = int(ack_dellay)
    RFM.destination = int(destination_node)
    if tx_power == "full":
        RFM.tx_power = 23
    else:
        RFM.tx_power = tx_power
    RFM.send(
        bytes("Startup message from node 1", "UTF-8")
        )
    
    import radioterminal
    rt = radioterminal
    radioterm = True
    sent = False
    while radioterm == True:
        radioterm, typeSelect, data = rt.radioterm(radioterm)
        if typeSelect == "b":
            counter, sent = Broadcast_send(RFM, data)
            if sent == False:
                import terminal
                if terminal.confirmation() == True:
                    counter, sent = Broadcast_send(RFM, data)
                elif terminal.confirmation() == False:
                    radioterm = True
        if typeSelect == "blink neo" or "ds":
            print("sending over radio")
            Broadcast_send(RFM, data)
        if typeSelect == "listen for trafic":
            paket = True
            while paket == False:
                print("listening for trafic from other nodes...")
                time.sleep(3)
        else:
            break

            

    

def listen_for_trafic(RFM, listen):
    data = RFM.receive()
    while listen == True:
        if data is not None:
            return data
    



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


