import configEditor

conedit = configEditor
print("starting config")
NODE, FREQ, tx_power = conedit.varinit()
def printcon(NODE, FREQ, tx_power):
    print("node= "+NODE)
    print("freq= "+FREQ)
    print("tx_power= "+tx_power)
printcon(NODE, FREQ, tx_power)

import terminal
term = terminal
Term_open = True
import board, digitalio
# import displaydriver1327
import neopx
neo = neopx
neo.blink_neo_color(255, 255, 255)
# boot_button = digitalio.digitalinout(board.button)
# boot_button.switch_to_input(pull=digitalio.Pull.UP)
def terminit(Term_open):
    reconfig = False
    while Term_open == True:
        Term_open, reconfig = term.terminal()
        
        if reconfig == True:
            
            NODE, FREQ, tx_power = conedit.varinit()
            printcon(NODE, FREQ, tx_power) 
            
            # Dd = displaydriver1327
            # Dd.write_to_display("reconfigureing...")
        
        # if boot_button.value ==True:
        #     print("button pressed")
        #     import neopx
        #     neopx.blink_neo_color(255,255,255)


terminit(Term_open) # coment this line out if the terminal is not used, see terminal program for use cases
