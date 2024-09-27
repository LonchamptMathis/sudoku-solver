import pulp
import numpy as np

def solve_sudoku(board):
    """
    Solve the given puzzle sudoku instance using Integer Programming if possible.

    :param board: A 9x9 2D list representing the Sudoku puzzle
    """
    # Define the problem
    prob = pulp.LpProblem("Sudoku_Problem", pulp.LpMaximize)

    # Define the decision variables
    x = pulp.LpVariable.dicts("x", (range(9), range(9), range(1, 10)), cat="Binary")

    # Objective: No need to maximize or minimize, so set it to 0
    prob += 0

    # Constraints
    # Each cell must have exactly one digit
    for i in range(9):
        for j in range(9):
            prob += pulp.lpSum([x[i][j][k] for k in range(1, 10)]) == 1

    # Each digit appears exactly once in each row
    for i in range(9):
        for k in range(1, 10):
            prob += pulp.lpSum([x[i][j][k] for j in range(9)]) == 1

    # Each digit appears exactly once in each column
    for j in range(9):
        for k in range(1, 10):
            prob += pulp.lpSum([x[i][j][k] for i in range(9)]) == 1

    # Each digit appears exactly once in each 3x3 subgrid
    for r in range(3):
        for c in range(3):
            for k in range(1, 10):
                prob += pulp.lpSum([x[i][j][k] for i in range(3 * r, 3 * (r + 1)) for j in range(3 * c, 3 * (c + 1))]) == 1

    # Pre-filled cells
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                prob += x[i][j][board[i][j]] == 1

    # Solve the problem
    prob.solve()

    # Extract the solution
    solution = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            for k in range(1, 10):
                if pulp.value(x[i][j][k]) == 1:
                    solution[i][j] = k
    solution = np.array(solution)

    return solution