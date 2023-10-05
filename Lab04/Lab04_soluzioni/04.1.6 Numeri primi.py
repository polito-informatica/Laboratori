# Esercizio 04.1.6
# Numeri primi

limite = int(input('Fino a quale valore vuoi arrivare? '))

for n in range(2,limite+1):
    # verifico se n è primo
    # uso il codice dell'esercizio precedente
    primo = True
    for i in range(2, n):
        if n % i == 0: 
            primo = False
    if primo:
        print(n)
