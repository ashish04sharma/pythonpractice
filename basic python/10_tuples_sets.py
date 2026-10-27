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
