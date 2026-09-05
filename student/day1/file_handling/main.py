student_name = input("Enter student name: ")
marks_python = float(input("Enter marks for Python:"))
marks_math = float(input("Enter marks for Mathematics:"))
marks_comm = float(input("Enter marks for Communication:"))

student = {
    "name": student_name,
    "python": marks_python,
    "mathematics": marks_math,
    "communication": marks_comm
}

print(student)