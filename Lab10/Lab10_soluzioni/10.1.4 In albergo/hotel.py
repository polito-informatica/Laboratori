# Esercizio 10.1.4
# In albergo

#  Display the sales file for a hotel, including error checking.

# Read the filename from the user.
filename = input("Enter the name of the file to display: ")

# Open the file.
try:
    in_f = open(filename, "r", encoding='utf-8')
except IOError:
    exit("That file couldn't be opened.")

# Read the lines, adding new categories as they are found and keep track
# of the totals.
categories = []
totals = []
for line in in_f:
    # Verify that the line has the required number of items.
    parts = line.rstrip().split(";")
    if len(parts) != 4:
        exit("There is an invalid line in the file.")

    # Verify that the amount is a valid number.
    try:
        amount = float(parts[2])
    except ValueError:
        exit("There is an invalid number in the file.")

    # If the category already exists then add to the total, otherwise add a
    # new category.
    if parts[1] in categories:
        index = categories.index(parts[1])
        totals[index] = totals[index] + amount
    else:
        categories.append(parts[1])
        totals.append(amount)

# Close the file.
in_f.close()

# Display the results.
print("Totals:")
for i in range(0, len(categories)):
    # print("  %s: %.2f" % (categories[i], totals[i]))
    print(f'  {categories[i]}: {totals[i]:.2f}')
