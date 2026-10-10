grades = []

while True:
    entry = input("Enter a student's grade or type 'done': ")

    if entry.lower() == "done":
        break

    grades.append(float(entry))

print("Grades entered:", grades)