# Check for perfect numbers (sum of divisors equals the number)

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return n > 1 and total == n


print("Is 28 perfect?", is_perfect(28))
print("Is 12 perfect?", is_perfect(12))

perfect = []
for num in range(1, 1000):
    if is_perfect(num):
        perfect.append(num)
print("Perfect numbers below 1000:", perfect)
