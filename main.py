import checkfile

configfile = "config.txt"

cf = checkfile
UID = cf.filemod(configfile, mode="conf_edit", writedata="", arg="UID=")

print(UID)