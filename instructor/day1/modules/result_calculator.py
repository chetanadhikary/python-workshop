def calculate_percentage(mark1,mark2,mark3):
    total = mark1 + mark2 + mark3
    return total/3

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >=70 :
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "F"
    