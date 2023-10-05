# Esercizio 03.1.3
# Stringhe e sottostringhe

lunga = input("Inserisci una sequenza 'lunga' di DNA: ")

# converto in maiuscolo per facilità di elaborazione
lunga = lunga.upper()

# dovrei verificare che la sequenza lunga contenga UNICAMENTE le 4 lettere ACTG...
# non lo sappiamo ancora fare perché servono i cicli

breve = input("Inserisci una sequenza 'breve' di DNA di 3 lettere: ")
breve = breve.upper()

if len(breve) != 3:
    print('Errore: la sequenza breve deve avere esattamente 3 lettere')
    exit()

# verifico se la sequenza breve è compresa in quella lunga

trovata = lunga.find(breve)
if trovata == -1:
    print('La sequenza breve non è presente')
else:
    print('La sequenza breve è presente a partire dalla posizione', trovata)

    # verifico quante volte è contenuta la sequenza (ovviamente da fare solo se è presente)
    quante = lunga.count(breve)
    print('La sequenza', breve, 'compare', quante, 'volte')
