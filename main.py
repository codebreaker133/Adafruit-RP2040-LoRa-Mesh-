import checkfile

configfile = "config"

cf = checkfile
UID = cf.filemod(configfile, mode="conf_edit", writedata="1234", arg="uid=")

print(UID)