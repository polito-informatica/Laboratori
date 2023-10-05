# Esercizio 02.2.5
# Immatricolazioni

matricola1 = 'S301888'
matricola2 = 'S800123'

# tutte le matricole da studente in Ateneo iniziano con la stessa lettera, per cui possiamo ricavarla da uno qualunque dei due codici di matricola

lettera = matricola1[0]

valore1 = int(matricola1[1:])
valore2 = int(matricola2[1:])

primaMatricola = min(valore1, valore2)
secondaMatricola = max(valore1, valore2)

print(lettera + str(primaMatricola), sep='')
print(lettera + str(secondaMatricola), sep='')

# SPUNTO 1: se considerassimo matricole con una lettera diversa, come ad esempio quelle di chi lavora al Politecnico, che iniziano con la "D", cosa accadrebbe?
# matricola2 = 'D300733'

# SPUNTO 2: se considerassimo matricole che, nella parte numerica, iniziano con uno o più "0", cosa accadrebbe?
# matricola2 = 'S000733'
