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

# None means no value yet
result = None
print("Result:", result, type(result))

# isinstance checks the type of a value
print("age is int:", isinstance(age, int))
print("name is str:", isinstance(name, str))

# Capital names are used for values that should not change
PI = 3.14159
print("Area of circle with r=2:", PI * 2 ** 2)

# Complex numbers have a real and an imaginary part
c = 3 + 4j
print("Complex:", c, "Real:", c.real, "Imaginary:", c.imag)

# Empty and zero values become False
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool(5):", bool(5))

# Same value can be given to many names
a = b = 100
print("a and b:", a, b)
print("Same object:", id(a) == id(b))
