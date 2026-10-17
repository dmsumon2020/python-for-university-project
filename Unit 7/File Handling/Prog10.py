import os

# Define old and new file names
old_filename = "zim.txt"
new_filename = "final_demo.txt"

try:
  # Renaming the file
  os.rename(old_filename, new_filename)
  print(f"File successfully renamed to '{new_filename}'.")

except FileNotFoundError:
  print("The file you are trying to rename was not found!")

except PermissionError:
  print(
      "The file is currently open in another program, so it cannot be"
      " renamed."
  )