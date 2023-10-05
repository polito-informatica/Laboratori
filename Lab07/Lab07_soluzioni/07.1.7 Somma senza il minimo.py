# Esercizio 07.1.7
# Somma senza il minimo

"""
Sum values without including the smallest.
"""

# Define constants.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    print("The sum without the smallest is", sum_without_smallest(ONE_TEN))


def sum_without_smallest(data):
    """
    Sum all elements in the list, excluding the smallest.

    :param data: the list of values to process
    :return: the sum of all of the values, excluding the smallest
    """
    smallest = min(data)
    total = sum(data)

    return total - smallest


# Call the main function.
main()
