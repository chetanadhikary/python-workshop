from modules.result_calculator import calculate_percentage,calculate_grade

student_name = input("Enter student name:")
marks_python = float(input("Enter marks for Python:"))
marks_math = float(input("Enter marks for Mathematics:"))
marks_comm = float(input("Enter marks for Communication:"))

percentage = calculate_percentage(mark1=marks_python,
                                  mark2=marks_math,
                                  mark3=marks_comm)
grade = calculate_grade(percentage=percentage)

print("\n -- Result --")
print("Student:", student_name)
print("Percentage",percentage)
print("Grade",grade)