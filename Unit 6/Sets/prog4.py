# The discard() Method
#This removes a specified item just like remove(), but if the item does not exist, Python will do nothing (no error is raised).

fruits = {"apple", "banana", "cherry"}
fruits.discard("orange")  # "orange" isn't in the set, but no error occurs

print(fruits)
# Output: {'apple', 'banana', 'cherry'}