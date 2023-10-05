# Esercizio 10.2.4
# Legami covalenti

#  Search a table of bonding information for a value supplied by the user.

# Open the file and read its data into a list.
in_f = open("bond_data.txt", "r")
lines = in_f.readlines()
in_f.close()

# Search the data until the user enters a blank line.
search = input("What do you want to look for (blank to quit)? ")
while search != "":
    # Find all lines that match the search value and display the other values.
    for line in lines:
        parts = line.split()
        if search.upper() in parts[0].upper():
            print("Bond Energy:", parts[1], "  Bond Length:", parts[2])
        if search in parts[1]:
            print("Bond Type:", parts[0], "  Bond Length:", parts[2])
        if search in parts[2]:
            print("Bond Type:", parts[0], "Bond Energy:", parts[1])

    # Read the next input from the user.
    print()
    search = input("What do you want to look for (blank to quit)? ")
