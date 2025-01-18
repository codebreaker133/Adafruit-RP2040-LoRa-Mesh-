import re
def file_updater(filename, arg, newvalue):
    with open(filename,"r")as file:
        content = file.read()
    print(f"'{filename}' content:\n", repr(content)+"\n")

    # Find the arg and replace its value
    print(f"Searching for '{arg}' in file '{filename}'")
    pattern = rf"{re.escape(arg)}\s*=\s*\"?(\w+)\"?"  # Match arg with current value
    updated_content, replacements = re.subn(pattern, rf"\1{newvalue}", content)
    
    if replacements == 0:
        print(f"arg '{arg}' not found in '{filename}'.")
    else:
        # Write the updated content back to the file
        with open(filename, 'w') as file:
            file.write(updated_content)

file_updater('config',"uid=","host2")

def filemod(filename, mode, writedata, arg):
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
        file_updater(filename,arg,writedata)
    
def createfile(filename):
    file = open(filename , "x")
    return file
