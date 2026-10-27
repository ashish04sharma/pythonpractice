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
