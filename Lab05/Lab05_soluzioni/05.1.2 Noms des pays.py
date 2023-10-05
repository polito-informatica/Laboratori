# Esercizio 05.1.2
# Noms des pays

#  Add the correct article ahead of a French country name.

# Read input from the user.
country = input("Enter a french country name: ")

# Determine the correct article.
if country == "Belize" or country == "Cambodge" or country == "Mexique" or \
        country == "Mozambique" or country == "Zaire" or country == "Zimbabwe":
    article = "le "
elif country == "Etats-Unis" or country == "Pays-Bas":
    article = "les "
elif country[0] in "AEIOU":
    article = "l'"
elif country[len(country) - 1] == "e":
    article = "la "
else:
    article = "le "

# Display the result.
print(f"{article}{country}")
