# Factorial of a number using a loop and recursion

def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Using loop:", factorial_loop(num))
    print("Using recursion:", factorial_recursive(num))
