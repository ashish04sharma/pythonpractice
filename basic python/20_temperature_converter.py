# Convert temperature between Celsius and Fahrenheit

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    print(c, "C =", round(celsius_to_fahrenheit(c), 2), "F")
elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f, "F =", round(fahrenheit_to_celsius(f), 2), "C")
else:
    print("Invalid choice")
