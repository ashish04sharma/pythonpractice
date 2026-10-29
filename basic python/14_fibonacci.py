# Fibonacci series

n = int(input("How many terms? "))

a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print("10th Fibonacci number (recursion):", fib(10))
