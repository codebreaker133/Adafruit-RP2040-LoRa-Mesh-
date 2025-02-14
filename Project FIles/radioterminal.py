
def radioterm(radiot):
    radiot: bool
    print("welcome to the direct radio interface")
    print("this interface is used to talk to the radio and isue it comands")
    radiot = True
    while radiot == True:
        import radio
        radio.interface_radio()
        userin = input("radio terminal: ")
        if userin == "broadcast":
            userin = input("what do you want to broadcast: ")
            typeSelect = "b" #broadcast mode
            data = bytes(userin,"utf-8")
            return radiot, typeSelect, data
        
        if userin == "direct send":
            userin = input("what do you want to send: ")
            data = bytes(userin,"utf-8")
            typeSelect = "ds" #direct send mode
            return radiot, typeSelect, data

        if userin == "blink neo":
            userin = input("what color: ")
            if userin == 'red':
                data = bytes("blink neo red","utf-8")
                typeSelect = "blink neo"
                return radiot, typeSelect, data
            
        if userin == "listen for trafic":
            data = None
            return radiot, typeSelect, data
        
        if userin == "exit":
            import terminal
            if terminal.confirmation() == True:
                radiot = False
            elif terminal.confirmation() == False:
                radiot = True

            

        

    