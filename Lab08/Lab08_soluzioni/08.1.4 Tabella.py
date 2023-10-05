# Esercizio 08.1.4
# Tabella

from pprint import pprint

n_righe = int(input('Numero di righe: '))
n_colonne = int(input('Numero di colonne: '))

# Punto I

tabella = []
for riga in range(n_righe):
    valori_riga = [0] * n_colonne
    tabella.append(valori_riga)

pprint(tabella)

# Punto II

for riga in range(len(tabella)):
    for colonna in range(len(tabella[riga])):
        tabella[riga][colonna] = 1

pprint(tabella)

# Punto III

for riga in range(len(tabella)):
    for colonna in range(len(tabella[riga])):
        if (riga + colonna) % 2 == 0:
            tabella[riga][colonna] = 1
        else:
            tabella[riga][colonna] = 0

pprint(tabella)

# Punto IV

for colonna in range(len(tabella[0])):
    tabella[0][colonna] = 0
    tabella[-1][colonna] = 0

pprint(tabella)

# Punto V

for riga in range(len(tabella)):
    tabella[riga][0] = 1
    tabella[riga][-1] = 1

pprint(tabella)


# Punto VI

somma = 0
for riga in range(len(tabella)):
    somma = somma + sum(tabella[riga])

print(somma)