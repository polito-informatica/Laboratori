# Esercizio 02.2.1
# Carrello

#  Print the first 3 letters of a string, followed by ..., followed by the
#  last 3 letters of a string.


# Initialize the string.
string = "Mississippi"

# Or... read the string from the user
#string = input('Enter a string:')

# NOTE: The string should have more than 6 characters
# What happens if it is shorter than 6 characters?
# What happens if it is shorter than 3 characters?

beginning = string[0:3]
ending = string[-3:]

# using sep='' to suppress the space between arguments
print(beginning, '...', ending, sep='')

# using f-strings:
print(f'{beginning}...{ending}')

