# Esercizio 07.1.4
# Massimi locali

"""
Find the local maxima of a series of numbers (read in input, terminated with an empty line)
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

if len(pos_local_max) > 0:
    print("Local maxima are in positions: ", pos_local_max)
else:
    print("There are no local maxima")
