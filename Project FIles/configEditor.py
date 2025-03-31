
import filehandler
fm = filehandler

def varinit(): #returns initial values needed for startup of Radio Module

    filename = "config.txt"
    NODE = fm.configread(filename,"Node")
    FREQ = fm.configread(filename,"freq")
    tx_power = fm.configread(filename,"tx_power")
    spread_factor = fm.configread(filename,"spread_factor")
    codeing_rate = fm.configread(filename, "coding_rate")
    return NODE, FREQ, tx_power, spread_factor, codeing_rate