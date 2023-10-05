# Esercizio 02.1.2
# Resistenze

# La legge di Kirchoff dice che:
# I1 = I2 + I3
# La legge di Ohm stabilisce che:
# V1 (caduta di tensione ai capi di R1) = R1 * I1
# V2 = R2 * I2
# V3 = R3 * I3
# Il collegamento in parallelo di R2 e R2 implica che:
# V2 = V3
# Il collegamento in serie di R1 con il resto del circuito implica che:
# V1 + V2 = E  (alternativamente: V1 + V3 = E)

# Per calcolare la resistenza totale dovrò calcolare I1, e poi R = E / I1

# Consideriamo il parallelo tra R2 e R3, con caduta di tensione V2.
# V2 = R2 * I2 e V2 = R3 * I3
# oppure I2 = V2/R2 e I3 = V2/R3

# La resistenza equivalente del parallelo tra R2 e R3 sarà
# R23 = V2 / (I2 + I3)
# sostituendo
# R23 = V2 / ( V2/R2 + V2/R3 ) = V2 / ( V2 * (1/R2+1/R3) )
# quindi (semplificando V2) R23 = 1 / (1/R2 + 1/R3)

# Considerando poi il collegamento di R1 "in serie", abbiamo che
# E = V1 + V2 = R1 * I1 + R23 * I1 (perché sarebbe R23 * (I2+I3), ma la corrente totale è I1)
# Ricavo I1 = E / (R1 + R23)
# Allora la resistenza totale sarà
# Rtot = E / I1 = R1 + R23


r1 = 100
r2 = 150
r3 = 300

# Per la lettura da tastiera, scommentare le righe seguenti:
# r1 = float(input('Valore di R1 (Ω): '))
# r2 = float(input('Valore di R2 (Ω): '))
# r3 = float(input('Valore di R3 (Ω): '))

# r23 è il parallelo tra r2 ed r3
r23 = 1 / (1 / r2 + 1 / r3)

# la resistenza equivalente è la serie tra r1 ed r23
r = r1 + r23

print('Resistenza totale', r, 'Ω')
