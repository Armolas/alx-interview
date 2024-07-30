#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """calculates the perimeter of an island"""
    rows = len(grid)
    cols = len(grid[0])

    i = 0
    perimeter = 0
    while i < rows:
        j = 0
        while j < cols:
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                if i == rows + 1 or grid[i + 1][j] == 0:
                    perimeter += 1
            j += 1
        i += 1
    return perimeter
