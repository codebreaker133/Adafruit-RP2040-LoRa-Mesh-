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

def terminit(Term_open):
    reconfig = False
    while Term_open == True:
        Term_open, reconfig = term.terminal()
        if reconfig == True:
            
            NODE, FREQ, tx_power = conedit.varinit()
            printcon(NODE, FREQ, tx_power) 

terminit(Term_open) # coment this line out if the terminal is not used, see terminal program for use cases
