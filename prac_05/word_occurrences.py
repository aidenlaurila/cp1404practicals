"""
Word Occurrences
Estimate: 15 minutes
Actual: 21 minutes
"""

word_occurrences = {}
text = input("Text: ")
words = text.split()
for word in words:
    try:
        word_occurrences[word] += 1
    except KeyError:
        word_occurrences[word] = 1

max_length = max((len(word) for word in words))
for word in sorted(word_occurrences):
    print(f"{word:{max_length}} : {word_occurrences[word]}")