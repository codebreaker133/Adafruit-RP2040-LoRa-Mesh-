import board # type: ignore
import busio # type: ignore
import digitalio # type: ignore
import adafruit_rfm 

# radio config
RADIO_FREQ_MHZ = 915.0
CS = digitalio.DigitalInOut(board.RFM_CS) #clock signal pin
RESET = digitalio.DigitalInOut(board.RFM_RST) #reset pin
SPIbus = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO) #data bus for radio

radio = adafruit_rfm.rfm9x.RFM9X(SPIbus, CS, RESET, RADIO_FREQ_MHZ) #radio initalised
# radio online, starting paramiter configuration
radio.crc = True
radio.bandwidth = 7800 #mesured in Hz
radio.coding_rate = 8 # 5-7
radio.spread_factor =12 # 7-12, six is valid but needs extra configuration to work
radio.tx_power = 23 #13-23dB
radio.receive_timeout = 2.0 #timeout before tx stops listening, set to 2 when lower bitrates set
# end of peram configuration starting transmition
import neoblink #type: ignore
print("radio transmiting...")
msg = input("what would you like to transmit?")
msgBITE = bytearray(msg, "UTF-8")
print("your message is "+len(msgBITE)+" bites long")
radio.send(msgBITE)
