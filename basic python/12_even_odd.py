# Check whether a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()
