# Esercizio 04.1.4
# Parole al contrario

#  Read a word from the user, and display its characters in reverse order.

# Read input from the user.
word = input("Enter a word: ")

# String length
word_len = len(word)

# Display the result.
reversed_word = word[word_len - 1::-1]  # with string slicing, negative step
# or simply
reversed_word = word[::-1]

print(f"{word} reversed is {reversed_word}")

print()

# Only capital letters, starting from the end

print('Only capital letters, in reverse order: ', end='')
for ch in reversed_word:
    if ch.isupper():
        print(ch, end='')
print()
