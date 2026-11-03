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

# Separate even and odd numbers from a list
values = [3, 8, 15, 22, 7, 10, 41]
even_list = []
odd_list = []
for v in values:
    if v % 2 == 0:
        even_list.append(v)
    else:
        odd_list.append(v)
print("Even:", even_list, "Count:", len(even_list))
print("Odd:", odd_list, "Count:", len(odd_list))
print("Sum of even numbers:", sum(even_list))

# Another way: the last bit of an odd number is 1
print(num, "is", "odd" if num & 1 else "even", "(bitwise check)")
