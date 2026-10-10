grades = []

while True:
    entry = input("Enter a grade or type 'done' to stop: ")

    if entry.lower() == "done":
        print("Grade entry stopped.")
        break

    grade = float(entry)

    if grade < 0:
        print("Invalid grade. Negative grades are not allowed.")
        continue

    grades.append(grade)

print("Valid grades:", grades)
