import re # import python RegularExpresions (RegEx) module

def configread(filename, key):
    with open(filename,"r") as file: #open file in read mode
        content = file.read() #read contents 
        pattern = re.compile(key+r"=\s?\w*") #compile search for value after key arg
        values = re.search(pattern, content) #used compiled search
        if values != None:
            results = re.sub(key+r"=\s?","",values.group(0)) # if key exists read value
            return results            
        else:
            results = f"error no values found for {key}"
            print(f"no values found for {key}")
            return results

def configreadList(filename, key):
    with open(filename, "r") as file:
        content = file.read()
        pattern = re.compile(rf'^\s*{re.escape(key)}\s*=\s*((?:\d+\s*,\s*)*\d+)\s*$', re.MULTILINE)
        match = re.search(pattern, content)
        if match:
            num_list_str = match.group(1)
            # Split by comma, strip spaces, convert to int
            result = [int(num.strip()) for num in num_list_str.split(',')]
            return result
        



def filemod(filename, mode, writedata, key):
    if mode == "readtxt":
        mode = "rt"
        file = open(filename, mode)
        contents = file.read()
        return contents
    elif mode == "writetxt":
        mode = "wt"
        confirm = input("this will overwrite all data are you sure? y or n")
        if confirm == "y":
            file = open(filename, mode)
            file.write(str(writedata))
        elif confirm == "n":
            print("write averted")
        else:
            print("error ocurred")
    elif mode == "appendtxt":
        mode = "at"
        file = open(filename, mode)
        file.write(writedata)
    if mode == "conf_edit":
        file_updater(filename, key, writedata)
    
def createfile(filename):
    file = open(filename , "x")
    return file

def file_updater(filename, key, newvalue):
    with open(filename,"r")as file: #open file as read
        content = file.read() #read contents of file

    # Find the key and replace its value
    print(f"Searching for '{key}' in file '{filename}'")
    pattern = r"" + re.escape(key) + r"\s*=\s*\"?(\w+)\"?"  # Match key with current value using RegEx
    updated_content, replacements = re.subn(pattern, r"\1"+newvalue, content)
    
    if replacements == 0: #if no key(variable) is found do not write to file
        print("key "+key+" not found in "+filename+".")
    else:
        # Write the updated content back to the file
        with open(filename, 'w') as file:
            file.write(updated_content)


def varinit(): #returns initial values needed for startup of Radio Module

    filename = "config.txt"
    NODE = configread(filename,"Node")
    FREQ = configread(filename,"freq")
    tx_power = configread(filename,"tx_power")
    spread_factor = configread(filename,"spread_factor")
    codeing_rate = configread(filename, "coding_rate")
    signal_bandwidth = configread(filename, "signal_bandwidth")
    return NODE, FREQ, tx_power, spread_factor, codeing_rate, signal_bandwidth