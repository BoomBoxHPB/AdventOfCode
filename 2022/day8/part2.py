from functools import reduce
import pathlib
from typing import List, Tuple
from operator import mul


def treeScore(value: int, trees: List[int]):
    if not trees:
        return 0
    
    score = 0
    for tree in trees:
        score += 1
        if tree >= value:
            break
    # print("Score: ", score)
    return score


def getTreeScore(grid: List[List[int]], col: int, row: int) -> int:
    value = grid[row][col]

    # print(col, row)
    # print(value)
    left = grid[row][:col]
    left.reverse()
    right = grid[row][col + 1 :]
    above = [gridRow[col] for gridRow in grid[:row]]
    above.reverse()
    below = [gridRow[col] for gridRow in grid[row + 1 :]]

    adjacents = [left, right, above, below]
    # print(adjacents)
    score = reduce(mul, [treeScore(value, l) for l in adjacents], 1)
    # print(score)
    return score


def run(inputPath: pathlib.Path):
    grid = [[int(v) for v in line.strip()] for line in inputPath.open().readlines()]
    # print(grid)

    gridHeight = len(grid)
    gridWidth = len(grid[0])

    indices: List[Tuple[int, int]] = []
    for col in range(gridWidth):
        for row in range(gridHeight):
            indices.append((col, row))
                
    # getTreeScore(grid, 2, 3)
    print(max(getTreeScore(grid, col, row) for col, row in indices))
