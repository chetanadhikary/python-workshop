class Person:
    """Represent a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        print("Student:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.student_id)

    def display_student(self):
        self.display()


class Teacher(Person):
    """Represent a teacher."""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display()
        print("Subject:", self.subject)


student = Student("Chetan", 41, "S001")
teacher = Teacher("Anita", 35, "Python")

print("Student:")
student.display_student()

print("\nTeacher:")
teacher.display_teacher()