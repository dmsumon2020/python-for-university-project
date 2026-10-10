# Initializing a dictionary
D1 = {"James": 50, "William": 30, "John": 25, "David": 60, "Sam": 20}
print(type(D1))

# Printing dictionary before sorting
print("The original dictionary is: ", D1)

# Sorting by value
D2 = dict(sorted(D1.items(), key=lambda x: x[1]))
print("After sorting by key: ", D2)
print(type(D2))