"""
https://www.youtube.com/watch?v=HS7t2i9ldmE&list=PLtQWXpf5JNGJrA4oZNuF8pRfdxRq3XVm9&index=11

https://www.youtube.com/watch?v=CLvNe-8-6s8&t=6s

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume

all four edges of the grid are all surrounded by water.

"""


def numIslands(grid) -> int:
    # When grid is empty means None. Return number of island as 0
    if grid == None or len(grid) == 0:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    # Iterate each cell of grid. First find the first cell which has '1' as land.
    # increment the count of island by 1
    # Find all the neighbour cell recursive (top, bottom, left, right) cells which are land
    # mark them as water
    # final return number of island

    def changelandtowater(row, col, grid):
        # check valid boundary
        # Row less then 0
        # Row greater than grid.length means (row length)
        # column less than 0
        # columns greater than len(grid[0]) means (column length)
        # if position is at index
        if (row < 0 or row >= len(grid) or
                col < 0 or col >= len(grid[0]) or
                grid[row][col] == '0'):
            return

            # After this condition we found the position where we have land
            # change to water
        grid[row][col] = '0'

        # recursive search all the the neighbour cells

        changelandtowater(row + 1, col, grid)  # Bottom row
        changelandtowater(row - 1, col, grid)  # Top row
        changelandtowater(row, col + 1, grid)  # Left
        changelandtowater(row, col - 1, grid)  # Right

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                island_count = island_count + 1
                # increment the island count when we found the cell as 1 means land
                # Now we need to find all it's neighbour land recursive meand
                changelandtowater(row, col, grid)

    return island_count


if __name__ == "__main__":
    # Test Case 1: Basic example
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    # Expected output: 1
    print(numIslands(grid1))

    # Test Case 2: Another example with multiple islands
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    # Expected output: 3
    print(numIslands(grid2))

    # Test Case 3: Empty grid
    grid3 = []
    # Expected output: 0
    print(numIslands(grid3))

    # Test Case 4: Grid with no islands
    grid4 = [
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"]
    ]
    # Expected output: 0
    print(numIslands(grid4))
