
try:
    from lib import filehandler as filehnd
    from lib import general_purpose_terminal as gpterm 
except:
    error = "failled to initialize critical module"
    print(error)
    raise Exception(error)
try:
    import neoblink as neo
except:
    error = "failed to initialize neoblink module, LED disabled"
    print(error)


print("loading current config...")
NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth = filehnd.varinit() #loading initial config values
print("the current config was loaded and is as follows,\n")
gpterm.PrintConfig(NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth) #prints values to terminal for debug
#builtins from adafruit for board control
print("system initialized... \n starting terminal...\n")
if error != "failed to initialize neoblink module, LED disabled":
    neo.blink_neo_color(0, 255, 0, 0.5) # green blink to show values initalized properly

def terminit(Term_open): #defines terminal logic using outputs from main terminal lib
    while Term_open == True:
        Term_open = gpterm.terminal() # type: ignore #opens terminal 

terminit(True) # coment this line out if the terminal is not used,
                    # see terminal program for use cases
                    # if you disable terminnal make sure you add your own
                    # custom code for tansmition and reception.
                    # Please do not use MY libraries outside this code they
                    # were coded for this aplication only, and will not behave 
                    # without special care and formating and I will not provide support
                    # unless we have spoken in person about your use case
