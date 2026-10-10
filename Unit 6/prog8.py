# Creating a dictionary
D1 = {
    101: "James",
    'age': 40,
    'city': "Delhi",
}
# Print the elements
print(D1)
# Add a new element
D1['Post'] = 'Manager'
print("Available Elements are:", D1)
# After adding new element, print all values
print("Before Deletion:", D1)
# deleting an element age
del D1['age']
# Values after deleted an element
print("After Deletion:", D1)