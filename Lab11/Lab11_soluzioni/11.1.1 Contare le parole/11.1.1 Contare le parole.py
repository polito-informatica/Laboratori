# Esercizio 11.1.1
# Contare le parole

#  Count how many times each word occurs in a file.

# Read the file name from the user and open the file.
filename = input("Enter the name of a file: ")
inf = open(filename, "r", encoding='utf-8')

# Create a new empty dictionary.
counts = {}

# Count the words in the file.
for line in inf:
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

# Close the file.
inf.close()

# Display the counts.
for word in sorted(counts):
    print(f"{word}: {counts[word]}")
