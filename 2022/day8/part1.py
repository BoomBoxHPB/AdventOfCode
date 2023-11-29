import pathlib
from typing import List, Optional, Tuple


def isVisible(grid: List[List[int]], col: int, row: int):
    value = grid[row][col]
    # print(value)
    left = grid[row][:col]
    right = grid[row][col + 1 :]
    above = [gridRow[col] for gridRow in grid[:row]]
    below = [gridRow[col] for gridRow in grid[row + 1 :]]

    adjacents = [left, right, above, below]
    # print(adjacents)
    return any([len(l) == 0 or max(l) < value for l in adjacents])


def run(inputPath: pathlib.Path):
    grid = [[int(v) for v in line.strip()] for line in inputPath.open().readlines()]
    # print(grid)

    gridHeight = len(grid)
    gridWidth = len(grid[0])

    totalVisible = 0
    for col in range(gridWidth):
        for row in range(gridHeight):
            if isVisible(grid, col, row):
                # print("visible")
                totalVisible += 1

    print(totalVisible)
