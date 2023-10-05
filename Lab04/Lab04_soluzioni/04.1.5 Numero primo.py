# Esercizio 04.1.5
# Numero primo

# Determina se un numero inserito da tastiera è primo

n = int(input('Inserisci un numero: '))

# Algoritmo: per tutti i numeri interi i compresi tra 2 ed n-1, verifica se n è divisibile per i

# uso una variabile logica (flag) 'primo' per ricordarmi se ho incontrato almeno un valore divisibile
primo = True
for i in range(2, n):
    if n % i == 0:  # è divisibile
        primo = False

if primo:  # non ho incontrato nessun divisore
    print(f'Il numero {n} è primo')
else:
    print(f'Il numero {n} non è primo')
