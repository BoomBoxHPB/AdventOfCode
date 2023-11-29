import pathlib
from typing import List


class Item:
    def __init__(self, monkey: int, level: int) -> None:
        self.monkey = monkey
        self.level = level

    def __repr__(self):
        return f"(monkey:{self.monkey}, level:{self.level})"


class MonkeyRules:
    def __init__(self, operation, test, monkeyTrue, monkeyFalse) -> None:
        self.operation = operation.strip().split()
        self.mod = test
        self.monkeyTrue = monkeyTrue
        self.monkeyFalse = monkeyFalse
        self.counter = 0

    def nextMonkey(self, item: Item) -> None:
        startLevel = item.level
        startMonkey = item.monkey
        level = self.applyOperation(item.level)
        level = level // 3
        if self.test(level):
            item.monkey = self.monkeyTrue
        else:
            item.monkey = self.monkeyFalse
        item.level = level
        
        # print(f"Monkey {startMonkey} throws item {startLevel} (now {item.level}) to {item.monkey}")

        self.counter += 1

    def applyOperation(self, level: int) -> int:
        if self.operation[0] == "old":
            left = level
        else:
            left = int(self.operation[0])

        if self.operation[2] == "old":
            right = level
        else:
            right = int(self.operation[2])
        
        if self.operation[1] == "*":
            return left * right
        else:
            return left + right

    def test(self, level: int) -> bool:
        return level % self.mod == 0

    def __repr__(self):
        return f"(op:{self.operation}, mod:{self.mod}, true:{self.monkeyTrue}, false:{self.monkeyFalse})"


def run(inputPath: pathlib.Path):
    items: List[Item] = []
    monkeys: List[MonkeyRules] = []

    with inputPath.open() as f:
        while True:
            firstLine = f.readline()
            if not firstLine:
                break
            monkeyNum = int(firstLine.split()[1].removesuffix(":"))
            levels = [int(i.strip()) for i in f.readline().split(":")[1].split(",")]
            operation = f.readline().split("= ")[1].strip()
            test = int(f.readline().split()[-1])
            monkeyTrue = int(f.readline().split()[-1])
            monkeyFalse = int(f.readline().split()[-1])
            f.readline()

            items += [Item(monkeyNum, i) for i in levels]
            monkeys.append(MonkeyRules(operation, test, monkeyTrue, monkeyFalse))

    print(items)
    print(monkeys)

    for _ in range(20):
        for i in range(len(monkeys)):
            for item in items:
                if item.monkey == i:
                    monkeys[item.monkey].nextMonkey(item)

        # print(items)
        # print(monkeys)

    print([m.counter for m in monkeys])