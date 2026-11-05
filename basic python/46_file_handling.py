# Write to a file, add to it, read it back and delete it

import os

filename = "notes.txt"

with open(filename, "w") as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(filename, "a") as file:
    file.write("Third line\n")

with open(filename, "r") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())

os.remove(filename)
print("File exists after delete:", os.path.exists(filename))
