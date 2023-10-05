# Esercizio 10.1.3
# Ricerca dell'anello

#  Find occurrences of a word in several files.

# Target files
filenames = input('Insert the list of files to search (separate with ,): ')

# Extract the target word from the command line.
target = input('Insert the word to search: ')

# For each filename on the command line.
for filename in filenames.split(','):
    # Save the filename and open the file.
    in_f = open(filename.strip(), "r", encoding='utf-8')

    # Search each line in the file for the target.
    for line in in_f:
        if target.lower() in line.lower():  # 'in' is used to search for a substring
            print(f'{filename}: {line}', end='')  # end='' because 'line' already contains a \n

    # Close the file.
    in_f.close()
