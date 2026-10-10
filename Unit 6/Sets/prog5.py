# The pop() Method

# This removes a random item from the set since sets are unordered. 
# It also returns the item that was removed. If the set is empty, it raises a KeyError. 

fruits = {"apple", "banana", "cherry"}
removed_item = fruits.pop()

print(removed_item)
print(fruits)
