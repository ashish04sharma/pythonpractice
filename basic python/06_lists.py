# Working with lists

fruits = ["apple", "banana", "mango"]
print(fruits)

fruits.append("orange")
fruits.insert(1, "grapes")
print("After adding:", fruits)

fruits.remove("banana")
print("After removing:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Total fruits:", len(fruits))

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Sorted:", numbers)
print("Max:", max(numbers), "Min:", min(numbers), "Sum:", sum(numbers))

# Slicing
print("First three:", numbers[:3])
print("Every second:", numbers[::2])

# pop removes and returns an item
last = numbers.pop()
print("Popped:", last, "Remaining:", numbers)

numbers.reverse()
print("Reversed:", numbers)
print("Index of 5:", numbers.index(5))

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
