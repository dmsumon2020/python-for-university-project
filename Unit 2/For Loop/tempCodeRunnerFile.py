classes = [["Alice", "Ben"], ["Chloe", "David"]]

for class_number, student_group in enumerate(classes, start=1):
    print("Class", class_number)

    for student in student_group:
        print(student)
