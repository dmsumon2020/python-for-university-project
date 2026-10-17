# Initialize the variable as a string
var = '27'
string = "Variable as string = %s" %(var)
print (string)

# Printing as raw data
print ("Variable as raw data = %r" %(var))

# Convert the variable to an integer
# and apply other formatting options
var = int(var)
string = "Variable as integer = %d" %(var)
print (string)
print ("Variable as float = %f" %(var))

print ("Variable as printing with special char = %c Ram" % (var))

print("Print variable as hexadecimal = %x" % (var))

print("Print variable as octal = %o" % (var))