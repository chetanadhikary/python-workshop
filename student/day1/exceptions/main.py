
student_name = input("Enter student name:")
marks_python = float(input("Enter marks for Python:"))
marks_math = float(input("Enter marks for Mathematics:"))
marks_comm = float(input("Enter marks for Communication:"))

total = (marks_python +
          marks_math +
            marks_comm)
percentage = total/3

percentage = 0

print("\n -- Result --")
print("Student:", student_name)
print("Percentage",percentage)
