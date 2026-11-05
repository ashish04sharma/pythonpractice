# Count how many times each word appears in a sentence

sentence = "the quick brown fox jumps over the lazy dog and the fox runs"
counts = {}

for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1

print("Sentence:", sentence)
print("\nWord counts:")
for word, count in counts.items():
    print(word, "-", count)

most_common = max(counts, key=counts.get)
print("\nMost common word:", most_common)
