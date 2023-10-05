# Esercizio 04.1.7
# Parole a pezzi

#  Display all substrings of a word, sorted by length.
#

# Read the word from the user.
word = input("Enter a word: ")

# Generate and display all substrings ordered by increasing length.
for length in range(1, len(word) + 1):
    for pos in range(0, len(word) - length + 1):  # all starting positions of substrings of length 'length'
        substring = ''
        for i in range(pos, pos + length):  # all characters of the substring of length 'length' starting at 'pos'
            substring = substring + word[i]
        print(substring)

# ** Alternative solution using the slicing operator ** #

# Generate and display all substrings ordered by increasing length.
for length in range(1, len(word) + 1):
    for pos in range(0, len(word) - length + 1):  # all starting positions of substrings of length 'length'
        print(word[pos: pos + length])
