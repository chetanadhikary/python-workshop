# Day 1 - Python Fundamentals
def calculate_percentage(mark1,mark2,mark3):
    total = mark1 +mark2 + mark3
    return total/3


student_name = input("Enter student name:")
marks_python = float(input("Enter marks for Python:"))
marks_math = float(input("Enter marks for Mathematics:"))
marks_comm = float(input("Enter marks for Communication:"))


percentage = calculate_percentage(mark1=marks_python,
                                  mark2=marks_math,
                                  mark3=marks_comm)

print("\n -- Result --")
print("Student:", student_name)
print("Percentage",percentage)
