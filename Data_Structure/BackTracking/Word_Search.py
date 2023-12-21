"""
https://www.youtube.com/watch?v=pfiQ_PS1g8E

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

The time complexity of this algorithm is
�
(
�
⋅
�
⋅
3
�
)
O(n⋅m⋅3
L
 ), where L = word.length. Thinking of the solution space tree, each node can have 3 children (not 4, because we don't consider the square where we came from, thus each node has at most 3 children, except the first node). The maximum depth is L, so this gives us
3
�
3
L
  nodes. We also have
�
⋅
�
n⋅m squares that we can start from. This time complexity would occur in the worst-case scenario if we had a grid with only one letter, and the word was also only that one letter, plus a different letter at the end. For example, board = [["A", "A", "A"],["A", "A", "A"],["A", "A", "A"]], word = "AAAAAAAAZ". The space complexity is
�
(
�
)
O(L) due to the recursion call stack and seen if it is a set. If using a boolean array, the space complexity is instead
�
(
�
⋅
�
)
O(n⋅m).

As you can see from the examples we have solved, backtracking problems all follow a very similar format. The main difference between problems is how to represent the state of each "node". Try these practice problems before moving on to the quiz and the next chapter.
"""


def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    # So that we can not visit to same node
    path = set()

    def dfs(r, c, i):
        # If we found the word
        if i == len(word):
            return True

        # check for boundary condition means out out of board
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                word[i] != board[r][c] or (r, c) in path):
            return False

        # else found the matcing character add the index of character as tupple to set
        path.add((r, c))

        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))
        path.remove((r, c))
        return res

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    return False

if __name__ == "__main__":
    # Example usage:
    # Create an instance of the Solution class


    # Sample input
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "ABCCED"

    # Check if the word exists in the board
    result = exist(board, word)
    print(result)
