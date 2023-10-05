# Esercizio 08.2.2
# Quadrati magici

# Determine if the numbers form a magic square.


# Read the values from the user into a 2D board.
def input_board():
    """
    Reads a 4x4 matrix of values
    :return: a 4x4 table (list of lists)
    """
    board = []  # table
    for r in range(0, 4):  # rows
        row = []
        for c in range(0, 4):  # columns
            val = input(f"Enter a value (position {r + 1},{c + 1}): ")
            row.append(int(val))  # fills the list for the row
        board.append(row)
    return board


def display_board(board):
    """
    Displays the board
    :param board: board to be displayed
    """
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            print(f'{board[row][col]:3}', end=" ")
        print()


def check_magic(board):
    """
    Check if the numbers in the board satisfies the "magic square" conditions
    :param board: board to be checked
    :return: <code>True</code>  if it is a magic square, <code>False</code> otherwise
    """
    # Determine the target total by summing the first row.
    target = sum(board[0])

    # Assume it is a magic square.  Change is_magic_square to False if we find
    # evidence that it is not.
    is_magic_square = True

    # Check that all of the numbers are present.
    for i in range(1, 17):
        if (i not in board[0] and i not in board[1] and
                i not in board[2] and i not in board[3]):
            is_magic_square = False

    # Check the rows.
    for i in range(1, len(board)):
        if sum(board[i]) != target:
            is_magic_square = False

    # Check the columns.
    for j in range(0, 3):
        if board[0][j] + board[1][j] + board[2][j] + board[3][j] != target:
            is_magic_square = False

    # Check the diagonals.
    if board[0][0] + board[1][1] + board[2][2] + board[3][3] != target:
        is_magic_square = False
    if board[0][3] + board[1][2] + board[2][1] + board[3][0] != target:
        is_magic_square = False

    # Alternative way to check the diagonals using loops
    sum_diag = 0
    for i in range(len(board)):
        sum_diag = sum_diag + board[i][i]
    if sum_diag != target:
        is_magic_square = False

    sum_diag = 0
    for i in range(len(board)):
        sum_diag = sum_diag + board[i][len(board) - 1 - i]
    if sum_diag != target:
        is_magic_square = False

    return is_magic_square


def main():
    board = input_board()
    display_board(board)
    is_magic_square = check_magic(board)
    # Display the result.
    if is_magic_square:
        print("It is a magic square.")
    else:
        print("It is not a magic square.")


# run the program
main()
