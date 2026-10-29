# Check whether a number is an Armstrong number
# e.g. 153 = 1^3 + 5^3 + 3^3

num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)
total = 0

for d in digits:
    total += int(d) ** power

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
