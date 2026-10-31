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
