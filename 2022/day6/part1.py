import pathlib
from typing import List


def run(inputPath: pathlib.Path):
    data = inputPath.open().read().strip()

    for i in range(4, len(data)):
        if len(set(data[i - 4 : i])) == 4:
            print(i)
            return
