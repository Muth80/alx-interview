#!/usr/bin/python3
"""
island_perimeter

Finds the perimeter of an island given in a grid

Functions:
- island_perimeter(grid): returns the perimeter of the island described in grid:
"""

def island_perimeter(grid):
    """
    Finds the perimeter of an island given in a grid

    Args:
    - grid: list of list of integers where 0 represents water and 1 represents land

    Returns:
    - perimeter: integer representing the perimeter of the island
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0: # Top border
                    perimeter += 1
                if i == len(grid)-1 or grid[i+1][j] == 0: # Bottom border
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0: # Left border
                    perimeter += 1
                if j == len(grid[i])-1 or grid[i][j+1] == 0: # Right border
                    perimeter += 1

    return perimeter
