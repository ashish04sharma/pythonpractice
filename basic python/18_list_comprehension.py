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
