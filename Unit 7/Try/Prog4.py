try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully!")
    print(content)
finally:
    print("Execution complete.")