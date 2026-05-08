
# Prompts user for .txt file to be loaded.
filename = input("Enter file name: ")

# Opens and reads contents of file.
with open(filename, "r") as file:
    text = file.read()

# Separates text into individual words.
words = text.split()

# Displays total word count.
print(f"Total # of words: {len(words)}")

# count recurring words
# filter common filler words
# print most common terms