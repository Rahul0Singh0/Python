def top_student(students):
    max_marks = 0
    topper = ""

    for name, marks in students.items():
        if marks > max_marks:
            max_marks = marks
            topper = name

    return topper

students = {
    "Rahul": 85,
    "Amit": 92,
    "Neha": 88
}

print(top_student(students))
