try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if the error happens
    print("You can't divide by zero!")