# Create a tuple containing borrower details
borrower = ("John Doe", "B1023", "2025-10-15")

print("Original borrower details:")
print(borrower)

# Attempt to modify an element in the tuple to demonstrate immutability
try:
    borrower[1] = "B2040"
except TypeError as error:
    print("Modification attempt failed:", error)

# Display tuple length and iterate through elements
print("Number of data fields:", len(borrower))

print("Borrower details:")
for item in borrower:
    print(item)