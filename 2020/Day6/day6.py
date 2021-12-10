#!/usr/bin/env python3
import sys
import utils

class Group:
    def __init__(self):
        self.yes1 = set()
        self.yes2 = None

    def AddLine(self, line):
        if self.yes2 is None:
            self.yes2 = set(line)

        self.yes1 = self.yes1 | set(line)
        self.yes2 = self.yes2 & set(line)

    def GetCount1(self):
        return len(self.yes1)

    def GetCount2(self):
        return len(self.yes2)

def main():
    lines = utils.read_lines()

    groups = []
    current_group = None
    for line in lines:
        if current_group is None:
            current_group = Group()
        elif line == '':
            groups.append(current_group)
            current_group = None
            continue

        current_group.AddLine(line)

    if current_group is not None:
        groups.append(current_group)

    total1 = 0
    total2 = 0
    for group in groups:
        total1 += group.GetCount1()
        total2 += group.GetCount2()

    print('Part1: {}'.format(total1))
    print('Part2: {}'.format(total2))


main()
