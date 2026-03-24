
import time, board, busio, digitalio #type: ignore
from adafruit_rfm import rfm9x #type: ignore


def interface_radio(FREQ, NODE, tx_power, ack_dellay, spread_factor, coding_rate, signal_bandwidth):
    CS = digitalio.DigitalInOut(board.RFM_CS) #set clock signal reset pin
    RESET = digitalio.DigitalInOut(board.RFM_RST) #set radio reset pin
    
    # Initialize SPI bus.
    SPI = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    # Initialze RFM radio
    RFM = rfm9x.RFM9x(SPI, CS, RESET, int(FREQ))
    RFM.enable_crc = True
    RFM.coding_rate = int(coding_rate) # accepted values are 5-8
    RFM.signal_bandwidth = int(signal_bandwidth)
    RFM.spreading_factor = int(spread_factor) # accepted values are 7-12 6 is accepted but requiers special configuration (not suported here)
    # set node addresses
    RFM.node = 1
    RFM.destination = 2

    RFM.node = int(NODE)
    RFM.ack_delay = int(ack_dellay)
    if tx_power == "full":
        RFM.tx_power = 23
    else:
        RFM.tx_power = tx_power
    RFM.send(
        bytes("Startup message from node 1", "UTF-8")
        )
    
    import radio_terminal as rt
    radioT = True
    sent = False
    typeSelect = "none" 
    data = "none"
    while radioterm == True:
        radioterm, typeSelect, data = rt.radioterm(radioT) 

        if typeSelect == "b":
            counter, sent = Broadcast_send(RFM, NODE, data)
            if sent == False:
                import general_purpose_terminal as terminal
                if terminal.confirmation() == True:
                    counter, sent = Broadcast_send(RFM, NODE, data)
                elif terminal.confirmation() == False:
                    radioT = True

        if typeSelect == "blink neo" or "ds":
            print("sending over radio")
            Broadcast_send(RFM, NODE, data)

        if typeSelect == "listen for trafic":
            paket = True
            while paket == False:
                listen_for_trafic(RFM, listen=True)
                
        else:
            break

            

    

def listen_for_trafic(RFM, listen):
    while listen == True:
        data = RFM.receive()
        print("listening for trafic from other nodes")
        if data is not None:
            print("data retreved: "+data.decode("utf-8"))
            return data
    



def Broadcast_send(RFM, NODE, data):
    time_now = time.monotonic()
    transmit_interval = 5
    counter = 0
    while True:
        if time.monotonic() - time_now > transmit_interval:
            # reset timeer
            time_now = time.monotonic()
            counter += 1
            # send a  mesage to all nodes            
            if RFM.send(data, keeplisting=False, destination=255, node=NODE) == True:
                print(" message sent! counter= " + str(counter))
                sent = True
                return counter, sent
            else:
                print("message failed to send! counter= " + str(counter))
                sent = False
                return counter, sent


