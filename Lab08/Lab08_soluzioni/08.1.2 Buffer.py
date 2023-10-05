# Esercizio 08.1.2
# Buffer

# definisci dei dati di esempio
dati = [9.8, 3.7, 8.9, 3.7, 11.2, 24.8, 8.9, 10.4]

print(dati)

# METODO 1: sposto i dati uno ad uno

# salva il valore dell'ultimo elemento
ultimo = dati[-1]
# sposta ogni elemento dalla casella 'i' alla casella successiva 'i+1'
# devo iniziare dal "fondo" della lista per non sovrascrivere i dati prima di averli spostati
for i in range(len(dati) - 2, -1, -1):
    dati[i + 1] = dati[i]
# riempio la prima posizione con il dato che prima era in ultima
dati[0] = ultimo

print(dati)

# METODO 2: uso una porzione per spostare tutti i dati (tranne l'ultimo)
ultimo = dati[-1]
dati[1:] = dati[0:-1]
dati[0] = ultimo

print(dati)

# METODO 3: come quello precedente, ma usando una tupla per scambiare contemporaneamente i due blocchi
dati[0], dati[1:] = dati[-1], dati[:-1]

print(dati)

# METODO 4: inserisci "in testa" il dato estratto "in coda"
dati.insert(0, dati.pop())

print(dati)

