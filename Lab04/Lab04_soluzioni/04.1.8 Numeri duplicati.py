# Esercizio 04.1.8
# Numeri duplicati

precedente = None  # valore fasullo, che sia "sicuramente" diverso dal primo numero inserito
duplicati = False  # variabile logica (flag), mi dice se sono all'interno di una sequenza di 2 o più numeri uguali

riga = input('Numero: ')
while riga != '':
    num = int(riga)

    if num != precedente:
        # nel, caso normale, il nuovo numero è diverso dal precedente
        if duplicati:
            # il valore precedente era la fine di una sequenza di duplicati?
            print(f'Il valore {precedente} è duplicato')
            duplicati = False
    else:
        # ho appena inserito un duplicato, non posso ancora stamparlo perché potrebbero arrivarne altri
        duplicati = True

    # prima di leggere un nuovo numero, mi salvo quello precedente in modo da poterlo confrontare
    precedente = num

    riga = input('Numero: ')

# se la sequenza inserita termina con dei numeri duplicati, nel ciclo while non ne stampa il valore
if duplicati:
    print(f'Il valore {precedente} è duplicato')
