# for and while loops

print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

print("Multiplication table of 7:")
for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)

print("Countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Done!")
