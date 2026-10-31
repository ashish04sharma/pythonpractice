# String operations

text = "Python is fun"

print(text.upper())
print(text.lower())
print(text.replace("fun", "awesome"))
print(text.split())
print("Length:", len(text))
print("First 6 letters:", text[:6])
print("Reversed:", text[::-1])

word = "madam"
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

# More useful methods
messy = "   hello world   "
print("Stripped:", messy.strip())
print("Title case:", messy.strip().title())
print("Count of 'o':", messy.count("o"))
print("Find 'world':", messy.find("world"))
print("Starts with 'Py':", text.startswith("Py"))

words = ["learn", "python", "daily"]
print("Joined:", " ".join(words))
print("Is digit '123':", "123".isdigit())
