# Store student marks in a dictionary and assign grades

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    return "F"


students = {}
count = int(input("How many students? "))

for i in range(count):
    name = input("Enter student name: ")
    marks = float(input("Enter marks for " + name + ": "))
    students[name] = marks

print("\nResults:")
for name, marks in students.items():
    print(name, "-", marks, "- Grade", get_grade(marks))

if students:
    average = sum(students.values()) / len(students)
    print("Class average:", round(average, 2))
