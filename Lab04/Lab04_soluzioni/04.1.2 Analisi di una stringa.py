# Esercizio 04.1.2
# Analisi di una stringa

riga = input('Inserisci un testo: ')

# Visualizza le lettere maiuscole
stampa = ''
for ch in riga:
    if ch.isupper():    # oppure: if "A" <= ch <= "Z"
        stampa = stampa + ch
print(f'Solo lettere maiuscole: {stampa}')

# Visualizza le lettere in posizione pari
stampa = ''
for pos in range(1, len(riga), 2):
    stampa = stampa + riga[pos]
print(f'Lettere in posizione pari: {stampa}')

# Converti vocali in underscore
stampa = ''
for ch in riga:
    if ch.upper() in 'AEIOU':
        stampa = stampa + '_'
    else:
        stampa = stampa + ch
print(f'Vocali cancellate: {stampa}')

# Or using replace()
# stampa = riga
# for ch in "aeiouAEIOU":
#   stampa = stampa.replace(ch,"_")
# print(stampa)


# Numero di cifre numeriche
cifre = 0
for ch in riga:
    if ch.isnumeric():  # or: "0" <= ch <= "9"
        cifre = cifre + 1
print(f'Ci sono {cifre} cifre numeriche')

# Posizione delle vocali
print('Le vocali sono in posizione:')
for pos in range(len(riga)):
    if riga[pos].upper() in 'AEIOU':
        print(pos)
