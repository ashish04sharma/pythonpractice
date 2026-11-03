# Print multiplication table of a number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\nTables from 1 to 5:")
for row in range(1, 11):
    for col in range(1, 6):
        print(row * col, end="\t")
    print()

# Neatly aligned table using f-string width
print(f"\nTable of {num} (aligned):")
for i in range(1, 11):
    print(f"{num:>3} x {i:>2} = {num * i:>4}")

# Same table using a while loop, in reverse
print(f"\nTable of {num} in reverse:")
i = 10
while i >= 1:
    print(num, "x", i, "=", num * i)
    i -= 1
