#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island defined in grid"""
    gridHeight = len(grid)
    assert (gridHeight > 0)
    gridWidth = len(grid[0])
    perimeter = 0

    assert 1 <= len(grid) <= 100, "Number of rows is out of range"
    assert all(1 <= len(row) <=
               100 for row in grid), "Number of columns is out of range"

    for i in range(gridHeight):
        for j in range(gridWidth):
            assert grid[i][j] in (
                0, 1), f"Invalid cell value at row {i}, col {j}"
            if grid[i][j] == 1:
                if j == 0:
                    perimeter += 1
                elif grid[i][j - 1] == 0:
                    perimeter += 1
                if j == gridWidth - 1:
                    perimeter += 1
                elif grid[i][j + 1] == 0:
                    perimeter += 1
                if i == 0:
                    perimeter += 1
                elif grid[i - 1][j] == 0:
                    perimeter += 1
                if i == gridHeight - 1:
                    perimeter += 1
                elif grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
