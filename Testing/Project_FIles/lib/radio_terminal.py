
def radioterm(radiot: bool):
     
    print("welcome to the direct radio interface")
    print("this interface is used to talk to the radio and isue it comands")

    """
    the variables in this part of the program are used as folows;

    userin; user input to be proseced and used for ether transmition to another node(s) or
    control the program outright
     
    typeSelect; this is ued to tell the program what type of transmition is ocuring
     
    data; the actual data that is to be sent over the radio 
    """

    radiot = True
    typeSelect = "none" 
    data = "none"        
    while radiot == True:
        userin = input("radio terminal: ")
        if userin == "broadcast":
            userin = input("what do you want to broadcast: ")
            typeSelect = "b" #broadcast mode
            data = bytes(userin,"utf-8")
            return radiot, typeSelect, data
        
        elif userin == "direct send":
            userin = input("what do you want to send: ")
            data = bytes(userin,"utf-8")
            typeSelect = "ds" #direct send mode
            return radiot, typeSelect, data

        elif userin == "blink neo":
            userin = input("what color: ")
            if userin == 'red':
                data = bytes("blink neo red","utf-8")
                typeSelect = "blink neo"
                radiot = True
                return radiot, typeSelect, data
            
        elif userin == "listen for trafic":
            data = "none"
            typeSelect = "listen"
            radiot = True
            return radiot, typeSelect, data

        elif userin == "exit":
            data = "none"
            typeSelect = "exit"
            import general_purpose_terminal as terminal
            if terminal.confirmation() == True:                
                radiot = False

            elif terminal.confirmation() == False:
                radiot = True

            else:
                print("terminal confirmation script error")
                radiot = False
        else:
            data = "error in radio terminal"
            typeSelect = "error inradio terminal"  
    print("exiting radio terminal") 
    typeSelect = "none" 
    data = "none"  
    radiot = False
    return radiot, typeSelect, data      

            

        

    