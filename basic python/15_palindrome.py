# Check if a string or number is a palindrome

word = input("Enter a word: ").lower()

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

num = 12321
reverse = 0
temp = num
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10

if num == reverse:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")

# Ignore spaces and punctuation in a sentence
sentence = "Was it a car or a cat I saw?"
cleaned = ""
for ch in sentence:
    if ch.isalnum():
        cleaned += ch.lower()
print(sentence, "-> palindrome:", cleaned == cleaned[::-1])


def is_palindrome(value):
    text = str(value)
    return text == text[::-1]


print("Palindrome numbers from 100 to 200:", [n for n in range(100, 201) if is_palindrome(n)])
