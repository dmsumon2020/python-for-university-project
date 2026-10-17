# Open the file in write mode
f_1 = open("demo3.txt", "w")

f_1.write("Python tools can be classified into two categories, general-purpose tools, and functional tools. \n")

f_1.writelines("Python has full-fledged support for a vast variety of built-in object types. \n")

f_1.writelines("Python considers memory as the private heap. \n")

f_1.writelines("Python community support is quite active and responsive \n")

f_1.close()  # to change file access modes


# Again opening the file

f_1 = open("demo3.txt", "rb")

print("Position of pointer:", f_1.tell())
# Reading first line
l1 = f_1.readline()
print(l1)
print("Position of pointer:", f_1.tell())

# Reading second line
l2 = f_1.readline()
print(l2)
print("Position of pointer:", f_1.tell())

# Reading third line
l3 = f_1.readline()
print(l3)
print("Position of pointer:", f_1.tell())

# Reading fourth line
l4 = f_1.readline()
print(l4)
print("Position of pointer:", f_1.tell())


# changing the pointer's position
# moving pointer 15 positions back from end of the file
print("changed pointer position:", f_1.seek(-15, 2))
f_1.close()

