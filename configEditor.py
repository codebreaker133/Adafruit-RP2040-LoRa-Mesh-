
import filehandler
fm = filehandler

def varinit(): #returns initial values needed for startup of Radio Module

    filename = "config.txt"
    NODE = fm.configread(filename,"Node")
    FREQ = fm.configread(filename,"freq")
    tx_power = fm.configread(filename,"tx_power")
    return NODE, FREQ, tx_power