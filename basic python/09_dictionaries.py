# Dictionaries

student = {
    "name": "Ashish",
    "age": 20,
    "course": "Computer Science",
}

print(student)
print("Name:", student["name"])

student["age"] = 21
student["city"] = "Bangalore"
print("Updated:", student)

for key, value in student.items():
    print(key, ":", value)

marks = {"maths": 85, "physics": 78, "chemistry": 90}
print("Average marks:", sum(marks.values()) / len(marks))
