
# Prompts user for .txt file to be loaded.
filename = input("Enter file name: ")

# Opens and reads contents of file.
with open(filename, "r") as file:
    text = file.read().lower()

# Separates text into individual words.
words = text.split()

# Displays total word count.
print(f"Total # of words: {len(words)}")

# TLDR: count recurring words
# Uses word_counts{} dictionary to track each unique term/word and # of occurrences.
# The earlier .lower() is to prevent duplicates from case differences (i.e., you vs You).
word_counts = {}

for term in words:
    if term in grammatical or len(term) < 2:
        continue
    if term in word_counts:
        word_counts[term] += 1
    else:
        word_counts[term] = 1

# filter common filler words
# print most common terms