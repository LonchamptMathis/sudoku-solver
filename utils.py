def display_sudoku(board):
    """
    Display the Sudoku board in a friendly format with grid lines.
    
    :param board: A 9x9 2D list representing the Sudoku puzzle
    """
    # Check board's size
    if board.shape != (9, 9):
        raise ValueError("The provided board does not match the shape of the sudoku")

    # Constructs graphical board
    print("-" * 25)
    for i in range(9):
        row = ""
        for j in range(9):
            if j % 3 == 0:
                row += "| "
            if board[i][j] == 0:
                row += ". "
            else:
                row += str(board[i][j]) + " "
        row += "|"
        print(row)
        if (i + 1) % 3 == 0:
            print("-" * 25)
