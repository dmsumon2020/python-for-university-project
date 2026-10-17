fileName = "Prog5.txt"

file = open(fileName, "r+")


print(file.read(10))

file.close()