# Calculate the power of a number using recursion

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


print("2 to the power 10:", power(2, 10))
print("5 to the power 3:", power(5, 3))
print("7 to the power 0:", power(7, 0))
print("Using ** operator:", 2 ** 10)
