import configEditor

conedit = configEditor
print("starting config")
NODE, FREQ, tx_power, spread_factor, codeing_rate = conedit.varinit() #loading initial config values
def printcon(NODE, FREQ, tx_power, spread_factor, codeing_rate):
    print("node= "+NODE)
    print("freq= "+FREQ)
    print("tx_power= "+tx_power)
    print("spread factor ="+spread_factor)
    print("coding rate= "+codeing_rate)
printcon(NODE, FREQ, tx_power)

import terminal
term = terminal
Term_open = True
import board, digitalio #type: ignore
#builtins from adafruit for board lvl control
import neoblink
neo = neoblink
neo.blink_neo_color(0, 255, 0, 0.5)

# boot_button = digitalio.digitalinout(board.button)
# boot_button.switch_to_input(pull=digitalio.Pull.UP)

neo.blink_neo_color(255, 255, 255, 0.5) # bootup blinks LED white to show startup
def terminit(Term_open): #defines terminal logic using outputs from main terminal lib
    reconfig = False
    while Term_open == True:
        Term_open, reconfig = term.terminal() #call terminal 
        
        if reconfig == True:    #if reconfiguation is requiered edit config.txt then use;
                                # "reload config in terminal"
            
            NODE, FREQ, tx_power = conedit.varinit() # pulls variables from config file
            printcon(NODE, FREQ, tx_power) #prints values to terminal for debug
            
        
        # if boot_button.value ==True:
        #     print("button pressed")
        #     neoblink.blink_neo_color(255,255,255)

terminit(Term_open) # coment this line out if the terminal is not used,
                    # see terminal program for use cases
                    # if you disable terminnal make sure you add your own
                    # custom code for tansmition and reception
                    # feel free to use the libraries in this repo
