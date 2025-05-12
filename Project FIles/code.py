import configEditor as confedit
import neoblink as neo
import general_purpose_terminal as gpterm 

print("starting config")
NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth = confedit.varinit() #loading initial config values
def printconf(NODE, FREQ, tx_power, spread_factor, codeing_rate):
    print("node= "+NODE)
    print("freq= "+FREQ)
    print("tx_power= "+tx_power)
    print("spread factor ="+spread_factor)
    print("coding rate= "+codeing_rate)
    print("signal bandwidth= "+signal_bandwidth)
printconf(NODE, FREQ, tx_power)

Term_open = True
import board, digitalio #type: ignore
#builtins from adafruit for board control
neo.blink_neo_color(0, 255, 0, 0.5) # green blink to show values initalized properly

neo.blink_neo_color(255, 255, 255, 0.5) # bootup blinks LED white to show terminal startup
def terminit(Term_open): #defines terminal logic using outputs from main terminal lib
    reconfig = False
    while Term_open == True:
        Term_open, reconfig = gpterm.terminal() #call terminal 
        
        if reconfig == True:    # if reconfiguation is requiered edit config.txt then use the
                                # "reload config" command in terminal
            
            NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth = confedit.varinit()  # pulls variables from config file
            printconf(NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth) #prints values to terminal for debug
            
        
terminit(Term_open) # coment this line out if the terminal is not used,
                    # see terminal program for use cases
                    # if you disable terminnal make sure you add your own
                    # custom code for tansmition and reception.
                    # Please do not use MY libraries outside this code they
                    # were coded for this aplication only, and will not behave 
                    # without special care and formating and I will not provide support
                    # unless we have spoken in person about your use case
