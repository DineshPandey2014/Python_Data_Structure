"""
https://www.youtube.com/watch?v=EG1eTU0TONo&list=PLNxqWc8Uj2LTaaxs-8vzK0Ft47rMggFnN&index=7


"""
import copy


def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_util(board, row, n, result):
    if row == n:
        #result.append(["".join(["Q" if cell == 1 else "-" for cell in row]) for row in board])
        # Here we have a nested list. We need to use a deep copy method
        result.append(copy.deepcopy(board))
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, result)
            board[row][col] = 0  # Backtrack

if __name__ == "__main__":
    n = 4
    # Create a board of n * n
    # Here we take n = 4
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    board = [[0] * n for _ in range(n)]
    result = []
    solve_n_queens_util(board, 0, n, result)
    """
      [['-   Q   -  -', 
       ' -   -   -  Q', 
       ' Q   -   -  -', 
       ' -   -   Q  -'], 
       ['--Q-', 'Q---', '---Q', '-Q--']]
    """
    print(result)