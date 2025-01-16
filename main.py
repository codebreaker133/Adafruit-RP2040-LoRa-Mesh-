import filehandler

configfile = "config"

FH = filehandler
UID = FH.filemod(configfile, mode="conf_edit", writedata="1234", arg="uid=")

print(UID)