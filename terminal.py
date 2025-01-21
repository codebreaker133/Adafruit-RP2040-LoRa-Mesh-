
# This program siply acts as a interface to the rest of the program, 
# If you are using the main program to transmit data only this is not technicly nessicary

def inloop(prev_command_recognised): # terminal interfaceing program

    if prev_command_recognised == True:
        userin = input("Terminal: ")

    elif prev_command_recognised == False:
        userin = input("Comand not recognised try again: ")
    return userin

def confirmation():

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

    prev_command_recognised = True
    Term_open = True
    reconfig = False
    while Term_open == True:

        userin = inloop(prev_command_recognised)
        prev_command_recognised = True

        if userin == "reload config":
            print("reloading config...")
            # RELOAD CONFIG
            print("config relaoded!")
            reconfig = True
            return reconfig, reconfig
        
        elif userin == "host":
            print("entering host controll submenue... ")

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

        else:
            prev_command_recognised = False
            
