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


# Default parameter value
def power(base, exp=2):
    return base ** exp


# Returning more than one value
def min_max(nums):
    return min(nums), max(nums)


# *args takes any number of arguments
def total(*nums):
    return sum(nums)


greet("Ashish")
print("Sum:", add(10, 20))
print("Factorial of 5:", factorial(5))
print("Square of 6:", power(6))
print("2 to the power 5:", power(2, 5))

low, high = min_max([4, 9, 1, 7])
print("Min:", low, "Max:", high)
print("Total:", total(1, 2, 3, 4, 5))

square = lambda x: x * x
print("Lambda square of 8:", square(8))
