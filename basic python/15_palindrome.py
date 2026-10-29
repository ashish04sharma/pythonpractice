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
