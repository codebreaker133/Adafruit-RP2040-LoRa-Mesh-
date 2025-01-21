import configEditor

conedit = configEditor
NODE, FREQ, tx_power = conedit.varinit()
def printcon(NODE, FREQ, tx_power):
    print("node= "+NODE)
    print("freq= "+FREQ)
    print("tx_power= "+tx_power)



import terminal
term = terminal
Term_open = True
while Term_open == True:
    Term_open, reconfig = term.terminal()
    if reconfig == True:
        NODE, FREQ, tx_power = conedit.varinit()
        printcon(NODE, FREQ, tx_power)
import radio
RFM = radio.radio_setup
radio.Broadcast_send_contin(RFM)