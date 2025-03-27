import configEditor

conedit = configEditor
print("starting config")
NODE, FREQ, tx_power = conedit.varinit() #loading initial config values
def printcon(NODE, FREQ, tx_power):
    print("node= "+NODE)
    print("freq= "+FREQ)
    print("tx_power= "+tx_power)
printcon(NODE, FREQ, tx_power)

import terminal
term = terminal
Term_open = True
<<<<<<< Updated upstream
import board, digitalio
# import displaydriver1327
import neoblink
neo = neoblink
neo.blink_neo_color(255, 255, 255)
# boot_button = digitalio.digitalinout(board.button)
# boot_button.switch_to_input(pull=digitalio.Pull.UP)
def terminit(Term_open):
=======
import board, digitalio #builtins from adafruit for board lvl control
# import displaydriver1327 #my custon display driver for 128x128 I2C OLED
import neopx
neo = neopx
neo.blink_neo_color(255, 255, 255) # bootup blinks LED white to show startup
def terminit(Term_open): #defines terminal logic using outputs from main terminal lib
>>>>>>> Stashed changes
    reconfig = False
    while Term_open == True:
        Term_open, reconfig = term.terminal() #call terminal 
        
        if reconfig == True:    #if reconfiguation is requiered edit config.txt then use;
                                # "reload config in terminal"
            
            NODE, FREQ, tx_power = conedit.varinit() # pulls variables from config file
            printcon(NODE, FREQ, tx_power) #prints values to terminal for debug
            
            # Dd = displaydriver1327
            # Dd.write_to_display("reconfigureing...")
<<<<<<< Updated upstream
        
        # if boot_button.value ==True:
        #     print("button pressed")
        #     import neoblink
        #     neoblink.blink_neo_color(255,255,255)
=======
>>>>>>> Stashed changes

terminit(Term_open) # coment this line out if the terminal is not used,
                    # see terminal program for use cases
                    # if you disable terminnal make sure you add your own
                    # custom code for tansmition and reception
                    #feal free to use the libraries in this repo
