# file_object = open("file_name.txt", "mode")

file = open("sample.txt", "r")

if file:
    print("File opened successfully")


file.close() # file will be closed
