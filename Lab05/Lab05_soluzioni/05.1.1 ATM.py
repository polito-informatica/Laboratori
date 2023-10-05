# Esercizio 05.1.1
# ATM

#  Simulate a bank machine validating a user's PIN.

# Define constants.
CORRECT_PIN = "1234"

# Number of attempts
attempts = 3
# Boolean variable to represent whether the PIN is correct or not
pin_is_correct = False

while attempts > 0 and not pin_is_correct:
    pin = input("Enter your PIN: ")

    if pin == CORRECT_PIN:
        pin_is_correct = True
        print("Your PIN is correct")

    attempts = attempts - 1

if not pin_is_correct:
    print("Your bank card is blocked")

