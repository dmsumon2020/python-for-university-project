# Store the number of borrowed books for seven weeks
borrowed_books = [23, 19, 31, 27, 22, 30, 25]

# Get the borrowing records for weeks 2 to 5
weeks_2_to_5 = borrowed_books[1:5]

# Change the value for week 1
borrowed_books[0] = 20

# Display the updated list
print("Updated weekly borrowing statistics:")
print(borrowed_books)

# Display the records for weeks 2 to 5
print("Borrowing records for weeks 2 to 5:")
print(weeks_2_to_5)