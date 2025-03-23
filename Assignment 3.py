# Input a Sentence
sentence = input("Enter a sentence of your choice: ")

# Output Sentence Details
total_chars = len(sentence)
print("Total characters:", total_chars)

words = sentence.split()
total_words = len(words)
print("Total words:", total_words)

first_word = words[0]
last_word = words[-1]
print("First word:", first_word)
print("Last word:", last_word)

# Indexing and Slicing
first_three_chars = sentence[:3]
print("First three characters:", first_three_chars)

last_three_chars = sentence[-3:]
print("Last three characters:", last_three_chars)

reversed_sentence = sentence[::-1]
print("Reversed sentence:", reversed_sentence)

# Modify the Sentence
uppercase_sentence = sentence.upper()
print("Uppercase sentence:", uppercase_sentence)

lowercase_sentence = sentence.lower()
print("Lowercase sentence:", lowercase_sentence)

hyphenated_sentence = sentence.replace(" ", "-")
print("Hyphenated sentence:", hyphenated_sentence)
