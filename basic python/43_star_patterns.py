# Print star patterns using nested loops

rows = 5

print("Right triangle:")
for i in range(1, rows + 1):
    print("*" * i)

print("\nInverted triangle:")
for i in range(rows, 0, -1):
    print("*" * i)

print("\nPyramid:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
