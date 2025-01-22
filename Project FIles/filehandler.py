import re


def file_updater(filename, key, newvalue):
    with open(filename,"r")as file:
        content = file.read()

    # Find the key and replace its value
    print(f"Searching for '{key}' in file '{filename}'")
    pattern = r"" + re.escape(key) + r"\s*=\s*\"?(\w+)\"?"  # Match key with current value
    updated_content, replacements = re.subn(pattern, r"\1"+newvalue, content)
    
    if replacements == 0:
        print("key "+key+" not found in "+filename+".")
    else:
        # Write the updated content back to the file
        with open(filename, 'w') as file:
            file.write(updated_content)


def configread(filename,key):
    with open(filename,"r") as file:
        content = file.read()
        pattern = re.compile(key+r"=\s?\w*")
        values = re.search(pattern, content)
        # print(values.group(0))
        if values != None:
            results = re.sub(key+r"=\s?","",values.group(0)) # SYNTAX ERROR needs fixing
            return results            
        else:
            print(f"no values found for{key}")


def filemod(filename, mode, writedata, key):
    if mode == "readtxt":
        mode = "rt"
        file = open(filename , mode)
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
        file_updater(filename,key,writedata)
    
def createfile(filename):
    file = open(filename , "x")
    return file
