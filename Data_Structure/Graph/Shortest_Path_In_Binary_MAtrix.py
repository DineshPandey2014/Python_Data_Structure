"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the
bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are
different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

"""


from collections import deque

def shortest_path_binary_matrix(matrix):
    if not matrix or not matrix[0] or matrix[0][0] == 1 or matrix[-1][-1] == 1:
        return -1  # No valid path
    rows, cols = len(matrix), len(matrix[0])

    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    visited = set((0,0))
    while queue:
        row, col, path_length = queue.popleft()

        if row == rows - 1 and col == cols - 1:
            return path_length

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == 0:
            #     queue.append((new_row, new_col, path_length + 1))
            #     matrix[new_row][new_col] = 1  # Mark the cell as visited

            # Check the cell is valid
            if (0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                queue.append((new_row, new_col, path_length + 1))
                visited.add((new_row, new_col))


    return -1  # No valid path found

if __name__ == "__main__":
    # Example usage:
    binary_matrix = [
        [0, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 0, 0]
    ]

    result = shortest_path_binary_matrix(binary_matrix)
    print("Shortest path length:", result)
