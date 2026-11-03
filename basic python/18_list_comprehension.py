# List comprehension examples

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n * n for n in numbers]
print("Squares:", squares)

evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

words = ["python", "java", "c", "javascript"]
upper_words = [w.upper() for w in words]
print("Uppercase:", upper_words)

lengths = {w: len(w) for w in words}
print("Word lengths:", lengths)

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("Labels:", labels)

# Flatten a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]
print("Flattened:", flat)

# Transpose a matrix
transposed = [[row[i] for row in matrix] for i in range(3)]
print("Transposed:", transposed)

# Set comprehension keeps only unique values
remainders = {n % 3 for n in numbers}
print("Remainders by 3:", remainders)

# Combine two lists with zip
names = ["amit", "neha", "ravi"]
scores = [82, 91, 77]
report = [f"{n}: {s}" for n, s in zip(names, scores)]
print("Report:", report)
