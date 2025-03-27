import re # import python RegularExpresions (RegEx) module

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


def configread(filename, key):
    with open(filename,"r") as file: #read file contents
        content = file.read()
        pattern = re.compile(key+r"=\s?\w*") #compile search for value after key arg
        values = re.search(pattern, content) #used comiled search
        # print(values.group(0))
        if values != None:
            results = re.sub(key+r"=\s?","",values.group(0)) # if key exists read value
            return results            
        else:
            print(f"no values found for{key}")


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
