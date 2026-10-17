# slide(start, stop, step)

# It starts the slice object at position 2, slice to position 4, and return the result:
var = ("P", "Y", "T", "H", "O", "N")
sl = slice(2, 4)
print (var[sl])

#It use the step parameter to return every second item:
var = ("P", "Y", "T", "H", "O", "N")
sl = slice(0, 6, 2)
print (var[sl])
