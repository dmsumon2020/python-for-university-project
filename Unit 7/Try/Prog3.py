try:
    # Trying to open a file that doesn't exist
    file = open("nonexistent.txt", "r")
except Exception as e:
    print(f"An unexpected error occurred: {e}")