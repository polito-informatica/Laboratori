# Esercizio 07.1.2
# Lista di numeri casuali

"""
Generate random integers and display them in different ways.
"""
from random import randint

# Define constants.
NUM_INTEGERS = 10
MAX_VALUE = 100

# Generate the random integers from 1 to MAX_VALUE
values = []
for i in range(0, NUM_INTEGERS):
    values.append(randint(1, MAX_VALUE))

#
# I.
#

# Display the elements at even index
print("Elements at even index: ", end="")
for i in range(0, len(values), 2):
    print(values[i], end=" ")
print()

# Alternative (using a slice of the list)
print("Elements at even index: ", end="")
for val in values[::2]:
    print(val, end=" ")
print()

#
# II.
#

# Display the even elements.

# Alternative 1: use a for..range loop
print("The even elements are: ", end="")
for i in range(len(values)):
    if values[i] % 2 == 0:
        print(values[i], end=" ")
print()

# Alternative 2: usa a for..in statement
print("The even elements are: ", end="")
for num in values:
    if num % 2 == 0:
        print(num, end=" ")
print()

#
# III.
#


# Display the elements in reverse order.
print("In reverse order:")
for i in range(len(values) - 1, -1, -1):
    print(values[i], end=" ")
print()

# Alternative (reversing the list with a slice)
print("In reverse order:")
for val in values[::-1]:
    print(val, end=" ")
print()

#
# IV.
#

# Display the first and last element.
print("First and last:", values[0], values[len(values) - 1])
print("First and last:", values[0], values[-1])  # shortcut: negative index
