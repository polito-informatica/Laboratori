# Esercizio 07.1.1
# Somma a segni alterni

"""
Compute the alternating sum of a list of values.
"""


def main():
    # Read values from the user and store them in a list.
    values = []
    input_str = input("Enter values (blank line to quit): ")
    while input_str != "":
        values.append(float(input_str))
        input_str = input("Enter values (blank line to quit): ")

    # Display the alternating sum of the entered values.
    print("The alternating sum is", alternating_sum(values))

    # Shortcut: use the "sum" function over the slice composed of even-position
    # and odd-position elements, separately.
    print('Another way of computing the alternating sum:', sum(values[0::2]) - sum(values[1::2]))


def alternating_sum(data):
    """
    Compute the alternating sum of a list of values.

    :param data: the list of values to process
    :return: the alternating sum of the provided values
    """
    total = 0
    for i in range(len(data)):
        if i % 2 == 0:
            total = total + data[i]
        else:
            total = total - data[i]

    return total


# Call the main function.
main()
