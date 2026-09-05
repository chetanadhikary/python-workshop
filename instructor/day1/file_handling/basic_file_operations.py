student_name = input("Enter student name: ")

with open("student.txt", "w") as file:
    file.write(student_name)

print("Student name saved successfully.")

with open("student.txt", "r") as file:
    name = file.read()

print("Student name:", name)