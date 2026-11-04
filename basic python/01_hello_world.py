# Printing output and taking input

print("Hello, World!")

name = input("Enter your name: ")
print("Welcome,", name)

age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

# sep and end change how print joins and finishes a line
print("Python", "is", "fun", sep="-")
print("No new line here", end=" ")
print("<- same line")

# f-strings put variables straight into text
print(f"{name} is {age} years old")

# Escape characters
print("Line one\nLine two")
print("Tab\tseparated")
print("She said \"hi\"")

# Triple quotes keep line breaks as typed
print("""Roses are red,
Python is fun.""")

# format() is the older way to fill values into text
print("Name: {}, Age: {}".format(name, age))

# Repeat text with *
print("=" * 20)

# Raw string keeps the backslash as it is
print(r"C:\new\test")

# Printing a list without brackets using *
print(*[1, 2, 3], sep=", ")
