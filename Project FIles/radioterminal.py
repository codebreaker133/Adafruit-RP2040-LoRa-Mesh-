
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
            typeSelect = "b" #broadcast
            data = userin
            return radiot, typeSelect, data
        
        if userin == "direct send":
            userin = input("what do you want to send: ")
            data = userin
            typeSelect = "ds" #direct send
            return radiot, typeSelect, data

        if userin == "blink neo":
            userin = input("what color: ")
            if userin == 'red':
                data = bytes("blink neo red","utf-8")
                typeSelect = "blink neo"
                return radiot, typeSelect, data
            
        if userin == "listen for trafic":
            
        if userin == "exit":
            import terminal
            if terminal.confirmation() == True:
                radiot = False
            elif terminal.confirmation() == False:
                radiot = True

            

        

    