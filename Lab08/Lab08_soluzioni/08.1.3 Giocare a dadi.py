# Esercizio 08.1.3
# Giocare a dati

#  Find and mark the longest run in a sequence.

from random import randint

# Define constants.
NUM_TOSSES = 20

# Generate 20 random values.
values = []
for i in range(0, NUM_TOSSES):
    values.append(randint(1, 6))

# Record the longest run's length and its position.
longest_run = 1
longest_pos = 0

# For each value in the list.
for i in range(0, len(values)):
    # Determine the length of the run starting at the current element.
    current_run = 1
    pos = i + 1
    while pos < len(values) and values[pos] == values[i]:
        pos = pos + 1
        current_run = current_run + 1

    # Update the longest run if the current run is longer.
    if current_run > longest_run:
        longest_run = current_run
        longest_pos = i

# Print out the list, marking the longest run.
for i in range(0, len(values)):
    if i == longest_pos:
        print("(", end="")

    print(values[i], end="")

    if i == longest_pos + longest_run - 1:
        print(")", end="")

    print(end=" ")
