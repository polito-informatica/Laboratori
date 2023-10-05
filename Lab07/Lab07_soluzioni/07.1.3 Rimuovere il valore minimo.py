# Esercizio 07.1.3
# Rimuovere il valore minimo

#  Remove the minimum value from a list.

from random import randint


def main():
    # Create a list of random values.
    random_values = []
    for i in range(10):
        random_values.append(randint(0, 10))

    # Demonstrate that remove_min functions correctly.
    print("The original list is: ", random_values)
    random_values = remove_min(random_values)
    print("With the minimum removed: ", random_values)


def remove_min(data):
    """
    Remove the minimum value from a list
    :param data: the list of values to process
    :return: a new copy of the list with the minimum element removed
    """
    smallest = data[0]
    smallest_pos = 0

    for i in range(1, len(data)):
        if data[i] < smallest:
            smallest = data[i]
            smallest_pos = i

    return data[:smallest_pos] + data[smallest_pos + 1:]


# Call the main function.
main()
