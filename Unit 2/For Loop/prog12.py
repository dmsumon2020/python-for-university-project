classes = [["Alice", "Ben"], ["Chloe", "David"]]

class_number = 1

for student_group in classes:
    print("Class", class_number)

    for student in student_group:
        print(student)

    class_number += 1