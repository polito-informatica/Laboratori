# Esercizio 04.2.2
# Diagnostica per immagini

#  Model radioactive decay.
from math import e, log

# Define constant variables.
HALF_LIFE = 6
lam = log(2.0) / HALF_LIFE

# Since we are interested in the ratio a/a0, we can fix a0 to a conventional value of 1.0
a0 = 1.0

# For each of 24 hours.
for t in range(1, 25):
    amount = a0 * e ** (-lam * t)
    print(f'After {t} hours, the amount is {amount:.2f} times A0')
