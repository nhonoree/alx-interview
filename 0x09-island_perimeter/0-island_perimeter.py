#!/usr/bin/python3
"""
This module contains a function that calculates the perimeter
of an island represented by a grid of 0s and 1s.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
        grid (list of list of int): 2D grid representation of the island.
        
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell contributes 4 sides by default
                perimeter += 4

                # Check for adjacent land above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # remove 1 from top and 1 from bottom

                # Check for adjacent land to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # remove 1 from left and 1 from right
    return perimeter
