# Tuples and sets

colors = ("red", "green", "blue")
print(colors)
print("Second color:", colors[1])
print("Count of red:", colors.count("red"))

nums = {1, 2, 3, 3, 4, 4, 5}
print("Set removes duplicates:", nums)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# Tuple unpacking
first, second, third = colors
print("Unpacked:", first, second, third)
print("Index of blue:", colors.index("blue"))

# Adding and removing in a set
nums.add(10)
nums.discard(1)
print("After add/discard:", nums)

print("Symmetric difference:", a ^ b)
print("{1, 2} is subset of a:", {1, 2}.issubset(a))

# Quick way to remove duplicates from a list
names = ["amit", "ravi", "amit", "neha", "ravi"]
print("Unique names:", sorted(set(names)))
