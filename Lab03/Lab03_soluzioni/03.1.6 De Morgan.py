# Esercizio 03.1.6
# De Morgan

x = int(input("Inserisci un numero intero: "))
print()

# caso I
expr1 = not (x > 0 and x < 100)
expr2 = x <= 0 or x >= 100
print('not (x > 0 and x < 100)', expr1)
print('x <= 0 or x >= 100', expr2)
print()

# caso II
expr1 = not (x > 0 or x < 100)
expr2 = x <= 0 and x >= 100
print('not (x > 0 or x < 100)', expr1)
print('x <= 0 and x >= 100', expr2)
print()

# caso III
expr1 = not (x > 0 or 100 < x)
expr2 = x <= 0 and 100 >= x
print('not (x > 0 or 100 < x)', expr1)
print('x <= 0 and 100 >= x', expr2)
print()

# caso IV
expr1 = not (x > 0 and x < 100 or x == -1)
# applicando De Morgan mi servono 2 passaggi, prima lo applico al 'or'
# not(x > 0 and x < 100) and x != -1
# e adesso lo applico al 'and' nella parentesi
# (x <=0 or x >=100) and x != -1
# attenzione, non posso togliere la parentesi, perché 'and' ha precedenza maggiore di 'or'
expr2 = (x <= 0 or x >= 100) and x != -1
print('not (x > 0 and x < 100 or x == -1)', expr1)
print('(x <= 0 or x >= 100) and x != -1', expr2)
