# Esercizio 07.1.4
# Massimi locali

# ESTENSIONE

"""
Find the two closest local maxima of a series of numbers
"""

numbers = []
data = input("Number: ")
while data != '':
    numbers.append(int(data))
    data = input("Number: ")

pos_local_max = []

for i in range(1, len(numbers) - 1):
    if numbers[i - 1] < numbers[i] > numbers[i + 1]:
        pos_local_max.append(i)

if len(pos_local_max) > 1:
    min_distance = pos_local_max[1] - pos_local_max[0]
    min_position = 1
    for i in range(2, len(pos_local_max)):
        if pos_local_max[i] - pos_local_max[i - 1] < min_distance:
            min_distance = pos_local_max[i] - pos_local_max[i - 1]
            min_position = i
    print("The closest local maxima are in positions: ", pos_local_max[min_position - 1], pos_local_max[min_position])
else:
    print("There are less than 2 local maxima")
