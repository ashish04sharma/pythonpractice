# Remove duplicate items from a list and keep the order

def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


numbers = [1, 3, 2, 3, 4, 1, 5, 2]
print("Original:", numbers)
print("Without duplicates:", remove_duplicates(numbers))
print("Using set (order not kept):", set(numbers))
