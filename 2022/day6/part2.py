import pathlib
from typing import List


def run(inputPath: pathlib.Path):
    data = inputPath.open().read().strip()

    messageLen = 14
    for i in range(messageLen, len(data)):
        if len(set(data[i - messageLen : i])) == messageLen:
            print(i)
            return
