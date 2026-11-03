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

# get returns a default instead of an error
print("Phone:", student.get("phone", "not added"))

# pop removes a key and returns its value
city = student.pop("city")
print("Removed city:", city)
print("Keys:", list(student.keys()))
print("Has 'name':", "name" in student)

marks.update({"maths": 95, "biology": 88})
print("After update:", marks)
print("Top subject:", max(marks, key=marks.get))

# Dictionary inside a dictionary
classroom = {
    "ashish": {"age": 21, "grade": "A"},
    "rahul": {"age": 20, "grade": "B"},
}
for name, info in classroom.items():
    print(name, "-> age", info["age"], "grade", info["grade"])
