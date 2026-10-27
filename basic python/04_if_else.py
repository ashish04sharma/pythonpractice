# Conditional statements

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
