"""
Here in this algo we are finding any path from top left cell to right bottom cell

"""
def anyPathBinaryMatrix(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()  # hold tuple row_index, col_index

    def dfs_any_path(row_index, col_index, path):
        if row_index == rows-1 and col_index == cols-1:
            path.append((row_index, col_index))
            visited.add(((row_index, col_index)))
            return True

        if (   row_index < 0
                or row_index >= rows
                or col_index < 0
                or col_index >= cols
                or grid[row_index][col_index] != 0
                or (row_index, col_index) in visited):
            return False

        path.append((row_index, col_index))
        visited.add(((row_index, col_index)))

        is_path_exist = (
        dfs_any_path(row_index, col_index + 1, path)  # Left
        or dfs_any_path(row_index, col_index - 1, path)  # right
        or dfs_any_path(row_index - 1, col_index, path)  # top
        or dfs_any_path(row_index + 1, col_index, path)  # bottom
        or dfs_any_path(row_index - 1, col_index + 1, path)  # Diganol top right
        or dfs_any_path(row_index + 1, col_index - 1, path)  # Diganol bottom left
        or dfs_any_path(row_index - 1, col_index - 1, path)  # Diganol top left
        or dfs_any_path(row_index + 1, col_index + 1, path)  # Diganol bottom right
        )
        # pop only when we get is_path_exist as False
        # Other wise don't pop
        # It means path don't exist
        if is_path_exist == False:
            path.pop()
        return is_path_exist

    path = []

    # Not here we don't need to run two for loop to traverse entire grid.
    # In quesiton it is asked about the path from top left cell to bottom right cell
    # So here we are starting from top node with index (0,0)
    dfs_any_path(0, 0, path)
    return path

if __name__ == "__main__":
    """
    [ [0, 1, 0],
      [0, 0, 1],
      [0, 0, 0]
    ]
    """
    grid = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
    result = anyPathBinaryMatrix(grid)
    print(result)