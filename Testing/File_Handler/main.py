import file_handeler_testing as fh
filename= "Testing/File_Handler/config.txt" # pyright: ignore[reportInvalidStringEscapeSequence]
K1= fh.configread(filename,"key1")
print(K1)
print(fh.configread(filename, "key2"))
print(fh.configreadList(filename, "list1"))
print(fh.configread(filename, "key3"))
