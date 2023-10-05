# Esercizio 03.2.5
# Ancora voti

# Read input from the user.
num = float(input("Enter a numeric grade: "))

# find the letter
closest_integer = round(num, 0)
if closest_integer == 4:
    letter = 'A'
elif closest_integer == 3:
    letter = 'B'
elif closest_integer == 2:
    letter = 'C'
elif closest_integer == 1:
    letter = 'D'
else:
    letter = 'F'

# aggiunta dei "+" o dei "-". Se il voto supera il valore intero per più di 0.15, allora sarà più vicino al 0.3 che a 0.0
# e quindi "merita" il "+". Analogamente sul lato negativo.
if letter != 'F':
    delta = num - closest_integer
    if delta >= 0.15:
        letter = letter + '+'
    elif delta <= -0.15:
        letter = letter + '-'

# Display the result.
print("The letter grade is %s." % letter)



# Nota: si potrebbe anche procedere per enumerazione diretta di tutti gli intervalli.
# La soluzione che segue non è particolarmente leggibile né manutenibile, nonostante
# calcoli correttamente il voto

# Convert to a letter grade.
if num >= 3.85:
    letter = "A"
elif num >= 3.5:
    letter = "A-"
elif num >= 3.15:
    letter = "B+"
elif num >= 2.85:
    letter = "B"
elif num >= 2.5:
    letter = "B-"
elif num >= 2.15:
    letter = "C+"
elif num >= 1.85:
    letter = "C"
elif num >= 1.5:
    letter = "C-"
elif num >= 1.15:
    letter = "D+"
elif num >= 0.85:
    letter = "D"
elif num >= 0.5:
    letter = "D-"
else:
    letter = "F"

# Display the result.
print("The letter grade is %s." % letter)
