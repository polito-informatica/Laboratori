# Esercizio 04.1.3
# Lati

#  Display a square and a diamond with a side length supplied by the user.
#

# Read the side length from the user.
side_length = int(input("Enter the side length: "))

# Display the square
for y in range(0, side_length):
    print('*' * side_length)
print()

# Display the diamond.
for y in range(1, side_length):
    print(" " * (side_length - y) + "*" * (y * 2 - 1))
for y in range(side_length, 0, -1):
    print(" " * (side_length - y) + "*" * (y * 2 - 1))

# Quale è la lunghezza minima in input per visualizzare le due forme?
