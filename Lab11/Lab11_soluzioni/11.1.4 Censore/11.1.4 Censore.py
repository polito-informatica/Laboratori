# Esercizio 11.1.4
# Censore

#  Implement a censor that replaces "bad" words with asterisks.

# Read the bad words into a set.
bad_file = open("bad_words.txt", "r", encoding='utf-8')
bad_words = set()
for word in bad_file:
    word = word.rstrip()
    bad_words.add(word)

# Close the bad words file.
bad_file.close()

# Read the input file and store it in a set.
input_name = input("Enter the input file name: ")
output_name = input("Enter the output file name: ")

# Open the files.
inf = open(input_name, "r", encoding='utf-8')
outf = open(output_name, "w", encoding='utf-8')

# Censor the input file, writing the result to the output file.
for line in inf:
    for bad_word in bad_words:
        # Check each position in the line.
        for pos in range(0, len(line) - len(bad_word)):
            # If we found the word at that position.
            if line[pos: pos + len(bad_word)].upper() == bad_word.upper():
                # Verify that it is actually a word, and not just part of another
                # word.
                if (pos == 0 or line[pos - 1] == " ") and \
                        (pos + len(bad_word) == len(line) - 1 or line[pos + len(bad_word)] in " .,;:?!"):
                    # Perform the replacement.
                    line = line[: pos] + "*" * len(bad_word) + line[pos + len(bad_word):]

    # Write the line to the output file.
    outf.write(line)

# Close the files.
inf.close()
outf.close()
