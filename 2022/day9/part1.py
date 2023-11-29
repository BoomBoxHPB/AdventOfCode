import pathlib
from enum import Enum
from typing import Set, Tuple
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

    def move(self, direction: Direction):
        if direction == Direction.U:
            self.y += 1
        if direction == Direction.D:
            self.y -= 1
        if direction == Direction.L:
            self.x -= 1
        if direction == Direction.R:
            self.x += 1

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

        if abs(xDelta) + abs(yDelta) == 3:
            self.x += Position.roundUp(xDelta / 2)
            self.y += Position.roundUp(yDelta / 2)
        elif abs(xDelta) + abs(yDelta) == 2:
            self.x += Position.roundDown(xDelta / 2)
            self.y += Position.roundDown(yDelta / 2)


class Instruction:
    def __init__(self, input: str):
        pieces = input.strip().split()
        self.direction = Direction(pieces[0])
        self.count = int(pieces[1])

    def __repr__(self):
        return f"{self.direction} {self.count}"


def run(inputPath: pathlib.Path):
    instructions = [Instruction(s) for s in inputPath.open().readlines()]
    # print(instructions)

    head = Position()
    tail = Position()

    visited: Set[Position] = set()
    visited.add(tail.tuple())

    for instruction in instructions:
        for _ in range(instruction.count):
            head.move(instruction.direction)
            tail.moveTail(head)
            # print(head, tail)
            visited.add(tail.tuple())
            # print(list(visited))

    print(len(list(visited)))
