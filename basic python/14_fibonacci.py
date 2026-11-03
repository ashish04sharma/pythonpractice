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

# Store the series in a list
series = [0, 1]
while len(series) < 15:
    series.append(series[-1] + series[-2])
print("First 15 terms:", series)
print("Even terms:", [x for x in series if x % 2 == 0])
print("Sum of first 15 terms:", sum(series))

# Fibonacci numbers below 100
x, y = 0, 1
print("Fibonacci numbers below 100:")
while x < 100:
    print(x, end=" ")
    x, y = y, x + y
print()
