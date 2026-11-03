# Simple calculator using user input

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /, %, **): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
elif op == "%":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Remainder:", a % b)
elif op == "**":
    print("Result:", a ** b)
else:
    print("Invalid operation")


# Same calculator written as a function
def calculate(x, y, operator):
    if operator == "+":
        return x + y
    if operator == "-":
        return x - y
    if operator == "*":
        return x * y
    if operator == "/" and y != 0:
        return x / y
    return None


print("12 * 3 =", calculate(12, 3, "*"))
print("12 / 0 =", calculate(12, 0, "/"))
