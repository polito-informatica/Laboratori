# Esercizio 02.1.3
# Cifre

# Read a 5 digit integer and display it with one digit per row.

# OPTION 1: treat the number as a 5-character string

# Gather input from the user.
num = input("Enter a 5 digit integer: ")

# Display the result.
print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])

# OPTION 2: use Division and Modulo of powers of 10

num = int(input("Enter a 5 digit integer: "))

print((num // 10000) % 10)
print((num // 1000) % 10)
print((num // 100) % 10)
print((num // 10) % 10)
print(num % 10)
