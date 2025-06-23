
# This program siply acts as a interface to the rest of the program, 
# you can use it to edit the config or send all types of radio transmitions
# If you are using hardcoded values to transmit data only with no configuration
# the terminal is not technicly nessisary

def inptloop(prev_command_recognised): # terminal interfaceing loop 

    if prev_command_recognised == True:
        userin = input("Terminal: ")

    elif prev_command_recognised == False:
        userin = input("Comand not recognised try again: ")
    return userin

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

def terminal(): # terminal logic
    import neoblink as neo
    prev_command_recognised = True
    Term_open = True
    reconfig = False
    while Term_open == True:

        userin = inptloop(prev_command_recognised)
        prev_command_recognised = True

        if userin == "reload config":
            print("reloading config...")
            # RELOAD CONFIG
            print("config relaoded!")
            reconfig = True
            return reconfig, reconfig
        
        elif userin == "radio":
            print("entering radio controll sub-menue... ")
            import radio
            import configEditor
            conedit = configEditor
            NODE, FREQ, tx_power, spread_factor, coding_rate, signal_bandwidth = conedit.varinit()
            ack_dellay = 0.2
            radio.interface_radio(FREQ, NODE, tx_power, ack_dellay, spread_factor, coding_rate, signal_bandwidth)

        elif userin == "clear":
            print("\n\n\n\n\n\n\n\n\n\n")
            return reconfig, reconfig
        
        elif userin == "exit":
            conf = confirmation()
            if conf == True:
                Term_open = False
                return Term_open, reconfig
            
            elif conf == False:
                Term_open = True
        elif userin =="neo white":
            
            neo.blink_neo_color(255, 255, 255, 1)
        elif userin == "print commands":
            print("accepted commands are; exit\nclear\nradio\nreload config\nneo white\n")
        else:
            prev_command_recognised = False
            
