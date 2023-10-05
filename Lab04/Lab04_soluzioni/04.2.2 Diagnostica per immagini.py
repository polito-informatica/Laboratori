# Esercizio 04.2.2
# Diagnostica per immagini

#  Model radioactive decay.
from math import e, log

# Define constant variables.
HALF_LIFE = 6
lam = log(2.0) / HALF_LIFE

# Read the initial amount from the user.
a0 = float(input("Enter the initial amount to Technetium-99: "))

# For each of 24 hours.
for t in range(1, 25):
    amount = a0 * e ** (-lam * t)
    print(f'After {t} hours, the amount is {amount:.2f}')
