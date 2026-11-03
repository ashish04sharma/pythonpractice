# Handling errors with try and except

try:
    num = int(input("Enter a number: "))
    print("100 divided by", num, "=", 100 / num)
except ValueError:
    print("That is not a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("No errors occurred")
finally:
    print("Program finished")

marks = [80, 90, 75]
try:
    print(marks[5])
except IndexError as e:
    print("Error:", e)

# KeyError with a dictionary
student = {"name": "Ashish"}
try:
    print(student["age"])
except KeyError:
    print("Key 'age' not found")


# raise lets us create our own error
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)

# Catch more than one error type together
for item in ["10", "abc", "0"]:
    try:
        print("100 /", item, "=", 100 / int(item))
    except (ValueError, ZeroDivisionError) as e:
        print("Problem with", repr(item), "->", e)
