import json


def save_students(students, filename):
    """Save student data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)


def load_students(filename):
    """Load student data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Invalid JSON data in: {filename}")
        return []



students = [
    {
        "name": "Harry",
        "python": 85,
        "mathematics": 78,
        "communication": 90
    },
    {
        "name": "Rahul",
        "python": 72,
        "mathematics": 88,
        "communication": 81
    }
]

filename = "students.json"

save_students(students, filename)
print("Student data saved successfully.")

loaded_students = load_students(filename)

print("\nLoaded student data:")
for student in loaded_students:
    print(student)