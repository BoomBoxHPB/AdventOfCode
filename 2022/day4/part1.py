import pathlib
from typing import Set


def setFromRange(rangeStr: str) -> Set[int]:
    lower, upper = (int(v) for v in rangeStr.split("-"))
    return set(range(lower, upper + 1))


def run(inputPath: pathlib.Path):
    fullyContains = 0
    with inputPath.open("r") as file:
        pairs = [line.strip().split(",") for line in file.readlines()]
        print(pairs)

        for range1, range2 in pairs:
            range1 = setFromRange(range1)
            range2 = setFromRange(range2)

            # print(range1, range2)
            if range1.issuperset(range2) or range2.issuperset(range1):
                fullyContains += 1
    
    print(fullyContains)
