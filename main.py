import string

# Prompts user for .txt file to be loaded.
filename = input("Enter file name: ")

# Opens and reads contents of file.
# .lower() is to prevent duplicates from case differences (i.e., you vs You).
with open(filename, "r") as file:
    text = file.read().lower()

# Removes punctuation.
for punc in string.punctuation:
    text = text.replace(punc, "")

# Splits text of whitespace.
words = text.split()

print(f"Total # of words: {len(words)}")

# Uses word_counts{} dictionary to track each unique term/word and # of occurrences.
word_counts = {}
stop_words = {
    "an", "the",
    "and", "or", "but",
    "is", "am", "are", "was", "were",
    "be", "been", "being",
    "to", "of", "in", "on", "at", "for",
    "you", "he", "she", "it", "we", "they",
    "me", "my", "your", "our", "their",
    "this", "that", "these", "those",
    "with", "as", "by", "from",
    "have", "has", "had",
    "do", "does", "did",
    "not", "no", "yes"
}

# Filters out grammatical/filler words, and builds dictionary.
for term in words:
    if term in stop_words or len(term) < 2:
        continue
    if term in word_counts:
        word_counts[term] += 1
    else:
        word_counts[term] = 1

print(f"# of unique words: {len(word_counts)}")

# Filters for most common themes/words.
theme_words = {}

for term, count in word_counts.items():
    if count < 2:
        continue
    theme_words[term] = count

print(theme_words)