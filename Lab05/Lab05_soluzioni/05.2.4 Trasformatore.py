# Esercizio 05.2.4
# Trasformatore

#  Determine the turns ratio that maximizes power.

# Define constant variables.
R0 = 20  # Resistance of the generator, Ohm
VS = 40  # Source voltage, Volt
RS = 8  # Resistance of the load (speaker), Ohm
STEP = 0.01  # Step of turn ratio


#  Compute the power for all values from STEP up to 2.0, saving the maximum.

max_power = 0.0
max_turns = -1  # invalid value, as 'sentinel'

n = STEP
while n <= 2.0:
    # formula for computing the power given to the load (speaker)
    Ps = RS * ((n * VS) / (n * n * R0 + RS)) ** 2
    if Ps > max_power:
        max_power = Ps
        max_turns = n
    n = n + STEP

# Display the result.
print(f"The maximum power is {max_power:.2f} with a turns ratio of {max_turns:.2f}.")
