# Search for a value by checking each item one by one

def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


fruits = ["apple", "mango", "banana", "orange"]
print("List:", fruits)

for fruit in ["banana", "grapes"]:
    index = linear_search(fruits, fruit)
    if index != -1:
        print(fruit, "found at index", index)
    else:
        print(fruit, "not found")
