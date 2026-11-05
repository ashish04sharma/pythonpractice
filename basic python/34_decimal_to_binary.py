# Convert a decimal number to binary and back

def to_binary(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result


def to_decimal(binary):
    total = 0
    for digit in binary:
        total = total * 2 + int(digit)
    return total


number = 45
binary = to_binary(number)
print(number, "in binary:", binary)
print(binary, "in decimal:", to_decimal(binary))
print("Using built-in bin():", bin(number))
