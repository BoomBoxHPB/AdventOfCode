#!/usr/bin/env python3.6
import sys
import utils

class Info:
    def __init__(self, line):
        parts = line.split()
        # print(parts)
        # Min/max
        (self.min, self.max) = [int(i) for i in parts[0].split('-')]
        self.char = parts[1].strip(':')
        self.string = parts[2]

    def isValidPart1(self):
        count = self.string.count(self.char)
        return (count >= self.min and count <= self.max)

    def isValidPart2(self):
        count = 0
        if self.string[self.min - 1] == self.char:
            count += 1
        if self.string[self.max - 1] == self.char:
            count += 1
        return (count == 1)

def create_struct(line):
    parts = line.split()
    print(parts)
    return parts

def main():
    infos = [Info(line) for line in utils.read_lines()]

    valid_count_part1 = 0
    valid_count_part2 = 0
    for info in infos:
        if info.isValidPart1():
            valid_count_part1 += 1
        if info.isValidPart2():
            valid_count_part2 += 1

    print("Part1: ", valid_count_part1)
    print("Part2: ", valid_count_part2)



main()
