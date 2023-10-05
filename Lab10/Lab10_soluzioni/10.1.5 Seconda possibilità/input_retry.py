# Esercizio 10.1.5
# Seconda possibilità

#  Read numbers from the user, with error checking, and report the sum.

# Keep reading values from the user until they enter two consecutive
# non-numeric values.


def safe_input():
    """
    Read a floating-point value from the user (or an empty line to conclude the list of values).
    In case of an invalid input, re-try the operation.
    In case of two errors, quit the program.

    :return: the number entered by the user, or None if the user entered an empty line
    """
    line = input("Enter a number (empty line to finish): ")
    if line == '':
        return None
    try:
        number = float(line)
        return number
    except ValueError:
        # offer a second attempt
        line = input("Wrong input. Retry. Enter a number (empty line to finish): ")
        if line == '':
            return None
        try:
            number = float(line)
            return number
        except ValueError:
            exit("Too many consecutive errors")


def main():
    total = 0

    value = safe_input()
    while value is not None:
        total = total + value
        value = safe_input()

    print(f'The total is: {total}')


main()
