# Esercizio 05.2.2
# La passeggiata ebbra

#  Simulate a person walking who chooses a random direction at each intersection.

from random import randint

# Define constant variables.
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Walk 100 blocks, picking a random direction at each intersection.
x = 0
y = 0
for i in range(0, 100):
    direction = randint(0, 3)
    # Adjust the position according to the direction chosen.
    if direction == UP:
        y = y - 1
    elif direction == DOWN:
        y = y + 1
    elif direction == LEFT:
        x = x - 1
    elif direction == RIGHT:
        x = x + 1

# Compute the distance and display the result.
distance = abs(x) + abs(y)
print(f"The drunkard ended up at ({x},{y}).")
print(f"That's {distance} blocks from where he started.")
