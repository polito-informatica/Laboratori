# Esercizio 03.1.1
# Vero o Falso

from math import sqrt

# Confronto I
if 1 == 1:
    print("1 == 1? True")
else:
    print("1 == 1? False")

# Confronto II
if 1 == 1.0:
    print("1 == 1.0? True")
else:
    print("1 == 1.0? False")

# Confronto III
if 2.0 == sqrt(4.0):
    print("2.0 == sqrt(4.0)? True")
else:
    print("2.0 == sqrt(4.0)? False")

# Confronto IV
if '1' == 1:
    print("'1' == 1? True")
else:
    print("'1' == 1? False")

# Confronto V
if 'ciao' == 'Ciao':
    print("'ciao' == 'Ciao'? True")
else:
    print("'ciao' == 'Ciao'? False")



# FORMULAZIONE ALTERNATIVA: il risultato di un confronto (es. 1==1) è esso stesso un valore di tipo
# booleano, e quindi può essere memorizzato in una variabile, che assumerà il valore True oppure il valore False
# (che sono costanti predefinite in Python) e come tale può essere stampata

confronto_I = (1 == 1)
print("1 == 1?", confronto_I)

confronto_II = (1 == 1.0)
print("1 == 1.0?", confronto_II)

confronto_III = (2.0 == sqrt(4.0))
print("2.0 == sqrt(4.0)?", confronto_III)

confronto_IV = ('1' == 1)
print("'1' == 1?", confronto_IV)

confronto_V = ('ciao' == 'Ciao')
print("'ciao' == 'Ciao'?", confronto_V)
