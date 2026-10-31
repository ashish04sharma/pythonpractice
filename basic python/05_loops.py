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

print("Even numbers up to 10:")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# break stops the loop, continue skips one round
print("Stop at 6, skip 3:")
for i in range(1, 10):
    if i == 3:
        continue
    if i == 6:
        break
    print(i)

print("Star pattern:")
for i in range(1, 5):
    print("*" * i)
