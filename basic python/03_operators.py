# Arithmetic, comparison and logical operators

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("a > b:", a > b)
print("a == b:", a == b)
print("a > 10 and b > 10:", a > 10 and b > 10)
print("a > 10 or b > 10:", a > 10 or b > 10)
print("not a > b:", not a > b)

# Assignment operators
c = 10
c += 5
print("c += 5:", c)
c *= 2
print("c *= 2:", c)
c -= 4
print("c -= 4:", c)

# Membership operators
nums = [1, 2, 3, 4]
print("3 in nums:", 3 in nums)
print("7 not in nums:", 7 not in nums)

# Identity operators check if two names point to the same object
p = [1, 2]
q = p
r = [1, 2]
print("q is p:", q is p)
print("r is p:", r is p)
print("r == p:", r == p)

# Operator precedence: ** before * before +
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
