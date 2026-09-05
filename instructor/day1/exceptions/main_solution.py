def get_valid_mark(subject):
    """Get a valid numeric mark from the user."""
    while True:
        try:
            return float(input(f"Enter marks for {subject}:"))
        except ValueError:
            print("Invalid input. Please enter a number.")


student_name = input("Enter student name:")

marks_python = get_valid_mark("Python")
marks_math = get_valid_mark("Mathematics")
marks_comm = get_valid_mark("Communication")

total = marks_python + marks_math + marks_comm
percentage = total / 3

print("\n -- Result --")
print("Student:", student_name)
print("Percentage:", percentage)