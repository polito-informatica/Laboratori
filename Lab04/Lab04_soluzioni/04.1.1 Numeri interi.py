# Esercizio 04.1.1
# Numeri interi

# inizializzazione delle variabili
somma = 0

n_min = 1000
n_max = -1000

conta_pari = 0
conta_dispari = 0

riga = input('Inserisci un numero: ')

# l'esecuzione prosegue fino a che non venga data in input una stringa vuota
while riga != '':
    n = int(riga)

    somma = somma + n
    print(f'Somma parziale: {somma}')

    if n > n_max:
        n_max = n
    print(f'Valore massimo: {n_max}')

    if n < n_min:
        n_min = n
    print(f'Valore minimo: {n_min}')

    if n % 2 == 0:
        conta_pari = conta_pari + 1
    else:
        conta_dispari = conta_dispari + 1

    print(f'Valori pari={conta_pari}, valori dispari={conta_dispari}')

    riga = input('Inserisci un numero: ')
