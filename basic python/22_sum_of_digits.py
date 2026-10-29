# Sum of digits of a number

num = int(input("Enter a number: "))
n = abs(num)
total = 0

while n > 0:
    total += n % 10
    n //= 10

print("Sum of digits of", num, "is", total)
