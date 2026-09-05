import json


students = [
    {
        "name": "Chetan",
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

with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("Student data saved successfully.")

with open("student.json", "r") as file:
    loaded_students = json.load(file)

print("\nStudent data:")
print(loaded_students)