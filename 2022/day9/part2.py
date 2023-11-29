import pathlib
from enum import Enum
from typing import Set, Tuple, List
import math


class Direction(Enum):
    U = "U"
    D = "D"
    L = "L"
    R = "R"


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = set()
        self.markVisited()
        self.tail = None


    def addTail(self, tail):
        self.tail = tail

    def move(self, direction: Direction):
        if direction == Direction.U:
            self.y += 1
        if direction == Direction.D:
            self.y -= 1
        if direction == Direction.L:
            self.x -= 1
        if direction == Direction.R:
            self.x += 1
        
        self.markVisited()
        if self.tail:
            self.tail.moveTail(self)

    def markVisited(self):
        self.visited.add((self.x, self.y))


    def __repl__(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)

    @staticmethod
    def roundUp(val: int) -> int:
        if val > 0:
            return math.ceil(val)

        return math.floor(val)

    @staticmethod
    def roundDown(val: int) -> int:
        if val > 0:
            return math.floor(val)

        return math.ceil(val)

    def moveTail(self, head):
        xDelta = head.x - self.x
        yDelta = head.y - self.y

        moved = False

        totalDelta = abs(xDelta) + abs(yDelta)
        if abs(xDelta) == 3 or abs(yDelta) == 3:
            print("WOOOOO")
        if totalDelta == 3 or totalDelta == 4:
            self.x += Position.roundUp(xDelta / 2)
            self.y += Position.roundUp(yDelta / 2)
            moved = True
        elif totalDelta == 2:
            self.x += Position.roundDown(xDelta / 2)
            self.y += Position.roundDown(yDelta / 2)
            moved = True
        # print(f"totalDelta = {totalDelta} ({xDelta},{yDelta}) self={self}")
        
        self.markVisited()
        if moved and self.tail:
            # print("moved")
            self.tail.moveTail(self)


class Instruction:
    def __init__(self, input: str):
        pieces = input.strip().split()
        self.direction = Direction(pieces[0])
        self.count = int(pieces[1])

    def __repr__(self):
        return f"{self.direction} {self.count}"


def run(inputPath: pathlib.Path):
    instructions = [Instruction(s) for s in inputPath.open().readlines()]
    print(instructions)

    positions: List[Position] = [Position()]
    for _ in range(9):
        newPosition = Position()
        positions[-1].addTail(newPosition)
        positions.append(newPosition)

    for instruction in instructions:
        for _ in range(instruction.count):
            positions[0].move(instruction.direction)
            # print(positions[6])

    print(len(list(positions[-1].visited)))
