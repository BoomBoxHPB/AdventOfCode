import pathlib
from typing import List


def run(inputPath: pathlib.Path):
    lines = inputPath.open().readlines()

    lineBreakIndex = lines.index("\n")

    crates = lines[: lineBreakIndex - 1]
    # print(crates)

    numStacks = int(len(crates[0]) / 4)
    stacks: List[List[str]] = [[] for i in range(numStacks)]

    for crateLine in crates:
        items = [crateLine[(i * 4) + 1] for i in range(len(stacks))]
        for item, stack in zip(items, stacks):
            if item != " ":
                stack.append(item)

    print(stacks)

    instructions = lines[lineBreakIndex + 1 :]
    # print(instructions)

    for instruction in instructions:
        _, num, _, source, _, dest = instruction.strip().split()
        print(num, source, dest)
        num = int(num)
        source = int(source) - 1
        dest = int(dest) - 1

        for _ in range(num):
            value = stacks[source].pop(0)
            stacks[dest].insert(0, value)

        print(stacks)

    outcome = ''.join([stack[0] for stack in stacks])
    print(outcome)