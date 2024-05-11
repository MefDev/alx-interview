#!/usr/bin/python3
"""Island perimeter module"""


def island_perimeter(grid: list) -> int:
    """Caluculate the perimeter of the island"""
    perimeter = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][column] == 1:
                    perimeter -= 2
                if column > 0 and grid[row][column - 1] == 1:
                    perimeter -= 2
    return perimeter
