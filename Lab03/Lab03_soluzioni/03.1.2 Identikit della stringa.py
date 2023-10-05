# Esercizio 03.1.2
# Identikit della stringa

# Read input from the user.
message = input("Enter a string: ")

# Check each property and display a message if that property is present.
if message.isalpha():
    print("The string contains only letters.")

elif message.isdigit():
    print("The string contains only digits.")

if message.isalpha() and message.isupper():  # v. nota
    print("All letters in the string are uppercase letters.")

elif message.isalpha() and message.islower():  # v. nota
    print("All letters in the string are lowercase letters.")

# Attenzione: quelle che seguono sono 'if' e non 'elif' perché non sono in
# esclusione rispetto alle possibilità precedenti

if message.isalnum():
    print("The string contains only letters and digits.")

if message[0].isupper():
    print("The string starts with an uppercase letter.")

if message.endswith("."):
    print("The string ends with a period.")

# NOTA: attenzione alle funzioni isupper/islower
# La documentazione dice:
# "Return True if all cased characters in the string are uppercase "
# "and there is at least one cased character, False otherwise"
# Quindi verifica "all CASED characters", quindi restituisce True
# se tutte le lettere sono maiuscole. I caratteri che non sono lettere
# (es. punteggiatura e spazi) non vengono controllati.
# Per questo bisogna verificare anche .isalpha(), per escludere dal
# nostro criterio dei caratteri che non siano alfabetici.
# La differenza è tra:
#   - tutti i caratteri alfabetici sono maiuscoli => .isupper()
#   - tutti i caratteri sono alfabetici maiuscoli => .isalpha() and .isupper()
