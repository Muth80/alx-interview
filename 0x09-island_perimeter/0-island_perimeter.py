#!/usr/bin/python3
"""
0-island_perimeter
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A rectangular grid with 0s representing water and
            1s representing land. The island is completely surrounded by water.

    Returns:
        int: The perimeter of the island.
    """
    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4 - (
                    (grid[i - 1][j] if i > 0 else 0) +
                    (grid[i + 1][j] if i < height - 1 else 0) +
                    (grid[i][j - 1] if j > 0 else 0) +
                    (grid[i][j + 1] if j < width - 1 else 0)
                )

    return perimeter
