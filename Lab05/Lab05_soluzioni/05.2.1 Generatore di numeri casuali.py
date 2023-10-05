# Esercizio 05.2.1
# Generatore di numeri casuali

#  Generate 100 random numbers using a seed value supplied by the user.

# Define constant variables.
A = 32310901
B = 1729
M = 2 ** 24

# Read the seed from the user.
r_old = int(input("Enter an integer: "))

# Compute and display 100 pseudo-random numbers.
for _ in range(100):
    r_new = (A * r_old + B) % M
    print(r_new)
    r_old = r_new
