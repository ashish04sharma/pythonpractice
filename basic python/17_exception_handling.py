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
