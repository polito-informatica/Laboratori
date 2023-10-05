# Esercizio 02.2.2
# Numero telefonico

# Display a phone number with nice formatting.

# Gather input from the user.
num = input("Enter a 10 digit phone number: ")

# Extract the parts of the number.
area_code = "(" + num[0:3] + ")"
formatted = area_code + " " + num[3:6] + "-" + num[6:10]

# Display the result.
print("The formatted number is:", formatted)
