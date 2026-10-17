a = range(1, 30)
f2 = "f2.txt"



# Open file to write
f2 = open(f2, "w")

for num in a:
  f2.write(str(num) + " ")
f2.close()  # Close the file


# To read the contents of the file, open it

f2 = open("f2.txt", "r+")

# Select to read it

print(f2.read())