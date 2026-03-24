
# This program siply acts as a interface to the rest of the program, 
# you can use it to edit the config or send all types of radio transmitions
# If you are using hardcoded values to transmit data only with no configuration
# the terminal is not technicly nessisary

from lib import filehandler as filehnd
NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth = filehnd.varinit()

def confirmation():         #function used for confirmation of commands when needed

    confirm = input("are you sure? y or n: ")
    if confirm == "y":
        return True
    elif confirm == "n":
        print("canceling...")
        return False
    else:
        print("answer not recognised returning to terminal...")
        return False
    
def PrintConfig(NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth):
    print("node; "+NODE)
    print("freq; "+FREQ)
    print("tx_power; "+tx_power)
    print("spread factor; "+spread_factor)
    print("coding rate; "+codeing_rate)
    print("signal bandwidth; "+signal_bandwidth)

def terminal(): # terminal logic
    prev_command_recognised = True
    Term_open = True
    reconfig = False

    while Term_open == True:

        prev_command_recognised = True
        userin = input("Terminal: ")

        if prev_command_recognised == False:
            userin = input("Comand not recognised try again: ")

        elif userin == "print config":
            PrintConfig(NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth)

        elif userin == "reload config": # if reconfiguation is requiered edit config.txt then use relod config
            print("reloading config...")
            NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth = filehnd.varinit()
            print("config relaoded!")
            return Term_open, reconfig
        
        elif userin == "radio":
            print("entering radio controll sub-menue... ")
            try:
                import radio
                import filehandler as filehnd
                NODE, FREQ, tx_power, spread_factor, coding_rate, signal_bandwidth = filehnd.varinit()
                ack_dellay = 0.2
                radio.interface_radio(FREQ, NODE, tx_power, ack_dellay, spread_factor, coding_rate, signal_bandwidth)
            except:
                print("could not import radio")
        elif userin == "clear":
            print("\n\n\n\n\n\n\n\n\n\n")
            return Term_open, reconfig
        
        elif userin == "exit":
            conf = confirmation()
            if conf == True:
                Term_open = False
                reconfig = False
                return Term_open, reconfig
            
            elif conf == False:
                Term_open = True
        elif userin == "print commands":
            print("accepted commands are; exit\nclear\nradio\nreload config\n")
            
        # input handleing for terminal
        elif prev_command_recognised == True:
            userin = input("Terminal: ")
        else:
            prev_command_recognised = False
        
            
