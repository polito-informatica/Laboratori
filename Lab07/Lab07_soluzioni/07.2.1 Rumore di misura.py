# Esercizio 07.2.1
# Rumore di misura

"""
Smooth out values in a list by averaging them with their neighbors.
"""


def main():
    values = [1, 2, 3, 5, 3, 1, 4]
    values_copy = list(values)

    # Display the original values.
    print("The original values are:", values)

    # Smooth the values and display the result.
    smooth(values)
    print("The smoothed values are:", values)

    smoothed_alternative = smooth_on_new_list(values_copy)
    print("The smoothed values are:", smoothed_alternative)


def smooth(data):
    """
    Smooth values in a list by averaging the value of each element with its neighbor(s).

    :param data: data the list of values to smooth
    :return: None (it modifies the list in-place)
    """
    if len(data) <= 1:
        return

    # Handle the first element in the list.
    old_left = data[0]
    data[0] = (data[0] + data[1]) / 2

    # Handle all values except for the first and last.
    for i in range(1, len(data) - 1):
        current = data[i]
        data[i] = (old_left + data[i] + data[i + 1]) / 3
        old_left = current

    # Handle the last element in the list.
    data[len(data) - 1] = (old_left + data[len(data) - 1]) / 2


def smooth_on_new_list(data):
    """
    This version creates a NEW list instead of modifying the current one, and returns it
    """
    result = []

    # element 0: average of elements 0 and 1
    result.append((data[0] + data[1]) / 2)

    # elements i = 1...len-1: average of 3 elements
    for i in range(1, len(data) - 1):
        value = (data[i - 1] + data[i] + data[i + 1]) / 3
        result.append(value)

    # last element: average of 2
    result.append((data[-2] + data[-1]) / 2)

    return result


# Call the main function.
main()
