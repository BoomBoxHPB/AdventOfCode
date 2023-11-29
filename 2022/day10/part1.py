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
    
    print([(cycleVals[i] * i) for i in (20,60,100,140,180,220)])
    print(sum((cycleVals[i] * i) for i in (20,60,100,140,180,220)))