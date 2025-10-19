"""
Word Occurrences
Estimate: 15 minutes
Actual:
"""

word_occurrences = {}
text = input("Text: ")
for word in text.split():
    if word in word_occurrences:
        word_occurrences[word] += 1
    else:
        word_occurrences[word] = 1
print(word_occurrences)