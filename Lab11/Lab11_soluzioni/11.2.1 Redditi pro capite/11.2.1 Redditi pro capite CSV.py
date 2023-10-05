# Esercizio 11.2.1
# Redditi pro capite
# Versione con file CSV
import csv

#  Read a database of per capita income by country and allow the user to
#  query it.

# Load the data into a dictionary.
incomes = {}

inf = open("rawdata_2021.csv", "r", encoding='utf-8')
inf.readline() # skip 1st line
reader = csv.reader(inf)

for parts in reader:
    # Remove the dollar sign and comma.
    parts[2] = parts[2].replace("$", "")
    parts[2] = parts[2].replace(",", "")

    # Add the country to the dictionary.
    incomes[parts[0].upper()] = float(parts[2])

# Read queries from the user and respond to them.
country = input("Enter a country name (or type quit to quit): ").upper()
while country != "QUIT":
    if country in incomes:
        print("The per capita income is", incomes[country])
    else:
        print("That wasn't a recognized country.")
    print()

    # Read the next country from the user.
    country = input("Enter a country name (or type quit to quit): ").upper()
