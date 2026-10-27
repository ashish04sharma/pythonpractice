# Defining and using functions

def greet(name):
    print("Hello,", name)


def add(a, b):
    return a + b


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


greet("Ashish")
print("Sum:", add(10, 20))
print("Factorial of 5:", factorial(5))
