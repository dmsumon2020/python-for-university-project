# file.writelines(list_of_items)

file = open("Prog3.txt", "w")

lines = ["Rony \n", "Sony \n", "Jony \n", "Tony"]

file.writelines(lines)

file.close()


file = open("Prog3.txt", "r+")

texts = file.read()

print(texts)

file.close()