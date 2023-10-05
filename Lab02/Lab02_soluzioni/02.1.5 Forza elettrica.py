# Esercizio 02.1.5
# Forza di Coulomb

from math import pi

# Define constants.
EPSILON = 8.854e-12

# Gather input from the user.
q1 = float(input("Enter the charge for particle 1 (C): "))
q2 = float(input("Enter the charge for particle 2 (C): "))
r = float(input("Enter the distance between (m): "))

# Compute the force.
f = (q1 * q2) / (4 * pi * EPSILON * r ** 2)

# Display the result.
print("The force is", f, "N")
