# Esercizio 05.1.4
# Al cinema

#  Sell a limited number of cinema tickets.

# Define constant variables.
LIMIT = 100

# Count the number of buyers until all tickets are sold.
num_buyers = 0
tickets = LIMIT
while tickets > 0:
    print(f"There are currently {tickets} tickets remaining.")

    # Get the number of tickets that want to be purchased in the current
    # transaction, ensuring that the number of tickets is legal.
    current = int(input("How many tickets would you like to purchase? "))
    while current > 4 or current > tickets or current < 1:
        if current < 1:
            print("Warning: you must buy at least 1 ticket")
        elif current > 4:
            print("Warning: you must buy at most 4 tickets")
        else:
            print(f"Warning: we only have {tickets} tickets available")
        current = int(input("How many tickets would you like to purchase? "))

    tickets = tickets - current
    num_buyers = num_buyers + 1

# Display the number of buyers.
print(f"The total number of buyers was {num_buyers}")
