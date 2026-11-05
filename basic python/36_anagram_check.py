# Check if two words are anagrams of each other

def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()
    return sorted(first) == sorted(second)


pairs = [("listen", "silent"), ("Dormitory", "dirty room"), ("hello", "world")]

for first, second in pairs:
    if is_anagram(first, second):
        print(first, "and", second, "are anagrams")
    else:
        print(first, "and", second, "are not anagrams")
