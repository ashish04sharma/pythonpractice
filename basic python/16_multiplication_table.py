# Print multiplication table of a number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\nTables from 1 to 5:")
for row in range(1, 11):
    for col in range(1, 6):
        print(row * col, end="\t")
    print()
