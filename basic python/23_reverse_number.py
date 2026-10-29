# Reverse the digits of a number

num = int(input("Enter a number: "))
n = abs(num)
reversed_num = 0

while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n //= 10

if num < 0:
    reversed_num = -reversed_num

print("Reversed number:", reversed_num)
