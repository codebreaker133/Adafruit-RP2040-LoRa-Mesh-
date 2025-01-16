import filehandeler

configfile = "config"

FH = filehandeler
UID = FH.filemod(configfile, mode="conf_edit", writedata="1234", arg="uid=")

print(UID)