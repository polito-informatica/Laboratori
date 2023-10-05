# Esercizio 04.2.1
# Il gioco di NIM

#  Play a game of Nim with the user.

from random import randint
from math import log2

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.
pile = randint(10, 100)
turn = randint(0, 1)
strategy = randint(0, 1)

# While the game is still being played.
while pile > 0:
    if turn == COMPUTER:
        if pile == 1:
            # Take the last marble.
            take = 1
        elif strategy == DUMB:
            # Take a random, legal number of marbles from the pile.
            take = randint(1, pile // 2)
        elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:  # or: if log2(pile+1).isinteger():
            # The computer is smart, but can't make a smart move.
            # Take a random, legal number of marbles from the pile.
            take = randint(1, pile // 2)
        else:
            # The computer is smart and can make a smart move.
            # Take marbles so that the pile will be a power of 2, minus 1.
            take = pile - 2 ** int(log2(pile)) + 1

        pile = pile - take
        print("The computer took %d marbles, leaving %d." % (take, pile))
        print()
        turn = HUMAN

    elif turn == HUMAN:
        print("Your turn.   The pile currently has", pile, "marbles in it.")

        # Force the user to take a legal number of marbles.
        take = int(input("How many marbles will you take? "))
        while take < 1 or take > max(pile // 2, 1):
            print("That isn't a legal move.")
            take = int(input("How many marbles will you take? "))

        pile = pile - take
        print("Now the pile has", pile, "marbles in it.")
        print()
        turn = COMPUTER

# Display the winner.
if turn == COMPUTER:
    print("The computer won!")
else:
    print("You Won!")
