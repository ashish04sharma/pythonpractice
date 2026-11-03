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

# Nested if
if num > 0:
    if num < 10:
        print("Single digit positive number")
    elif num < 100:
        print("Two digit positive number")
    else:
        print("Large positive number")

# Short if-else on one line
result = "divisible by 5" if num % 5 == 0 else "not divisible by 5"
print(num, "is", result)

# Chained comparison
if 1 <= num <= 100:
    print(num, "is between 1 and 100")

# Combining conditions with and
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
