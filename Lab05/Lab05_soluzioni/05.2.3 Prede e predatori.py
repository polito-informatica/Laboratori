# Esercizio 05.2.3
# Prede e predatori

#  Model the relationships between predators and prey.

print('''\
Simulation of the Predator-Prey eco-system, according to the equations:
prey(n+1) = prey(n) × (1 + A – B × pred(n))
pred(n+1) = pred(n) × (1 – C + D × prey(n))
''')

# Read the simulation parameters from the user.
a = float(input("Enter the value for A (0.1 is a good choice): "))
b = float(input("Enter the value for B (0.01 is a good choice): "))
c = float(input("Enter the value for C (0.01 is a good choice): "))
d = float(input("Enter the value for D (0.00002 is a good choice): "))

prey = int(input("Enter the initial prey (1000 is a good choice): "))
pred = int(input("Enter the initial predators (20 is a good choice): "))

periods = int(input("Enter the number of periods: "))

# Run the simulation for the requested number of periods.
for period in range(1, periods + 1):
    new_prey = prey * (1 + a - b * pred)
    new_pred = pred * (1 - c + d * prey)

    if round(new_prey) != 0 and round(new_pred) != 0:
        print("After period", period, "there are", round(new_pred), "predators")
        print("After period", period, "there are", round(new_prey), "prey")
        print()

        # Update prey and predators with the newly computed values.
        prey = new_prey
        pred = new_pred

    else:
        print('The number of preys o predators has reached the zero. The program stopped.')
        break
