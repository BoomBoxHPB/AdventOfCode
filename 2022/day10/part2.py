import pathlib
from typing import List

def run(inputPath: pathlib.Path):
    instructions = [s.strip().split() for s in inputPath.open().readlines()]
    cycleNum = 0
    regX = 1

    cycleVals = {}
    cycleVals[cycleNum] = regX

    for inst in instructions:
        if inst[0] == "noop":
            cycleNum += 1
            cycleVals[cycleNum] = regX
        elif inst[0] == "addx":
            cycleNum += 1
            cycleVals[cycleNum] = regX
            cycleNum += 1
            cycleVals[cycleNum] = regX
            regX += int(inst[1])
        
    cycleVals[cycleNum] = regX
    
    partialStr = ""
    rowSize = 40
    rowCount = 0
    for i in range(1, len(cycleVals)):
        pixel = i - (rowCount * rowSize)
        # print(cycleVals[i], range(pixel-2, pixel+1))
        if cycleVals[i] in range(pixel-2, pixel+1):
            # print("hit")
            partialStr += "#"
        else:
            partialStr += " "

        if i % 40 == 0:   
            print(partialStr)
            partialStr = ""
            rowCount += 1
            # break