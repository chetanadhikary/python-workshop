class Student:
    """Represent a student."""

    def __init__(self, name, age, python, mathematics, communication):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        total = self.python + self.mathematics + self.communication
        return total / 3

    def update_python_mark(self, mark):
        if 0 <= mark <= 100:
            self.python = mark
        else:
            print("Invalid Python mark.")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())


student = Student("Chetan", 41, 85, 78, 90)
student.update_python_mark(1870)
student.display()