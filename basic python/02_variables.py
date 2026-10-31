# Variables and data types

age = 20
height = 5.8
name = "Ashish"
is_student = True

print(name, "is", age, "years old")
print("Height:", height)
print("Student:", is_student)

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# Type conversion
num_text = "25"
num = int(num_text)
print("String to int:", num + 5)
print("Int to float:", float(age))
print("Float to int:", int(height))
print("Int to string:", str(age) + " years")

# Multiple assignment and swapping
x, y, z = 1, 2, 3
print("x, y, z:", x, y, z)
x, y = y, x
print("After swap x, y:", x, y)
