from student import Student
from student_manager import StudentManager


student1 = Student("Chetan", 41, 85, 78, 90)
student2 = Student("Rahul", 35, 72, 88, 81)

manager = StudentManager()

manager.add_student(student1)
manager.add_student(student2)

manager.view_students()

student = manager.find_student("Chetan")

if student:
    print("\nStudent found:")
    student.display()
else:
    print("Student not found.")

updated = manager.update_student("Chetan", 100, 92, 88)

if updated:
    print("\nStudent updated:")
    manager.find_student("Chetan").display()
else:
    print("Student not found.")

deleted = manager.delete_student("Rahul")

if deleted:
    print("\nStudent deleted.")
else:
    print("Student not found.")

print("\nRemaining students:")
manager.view_students()