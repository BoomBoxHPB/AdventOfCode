#!/usr/bin/env python3
import sys
import utils

class Data:
    def __init__(self, lines):
        self.data = [line for line in lines]
        self.width = len(self.data[0])
        self.height = len(self.data)
        # print(self.width)
        # print(self.height)

    def TreeCount(self, down_right):
        cursor = [0, 0]
        count = 0
        while cursor[0] < self.height:
            if self.data[cursor[0]][cursor[1] % self.width] == '#':
                count += 1
            cursor = [sum(x) for x in zip(cursor, down_right)]
            # print(cursor)

        return count


def main():
    data = Data(utils.read_lines())

    print("Part1: ", data.TreeCount([1,3]))

    part2_list = [
        [1,1],
        [1,3],
        [1,5],
        [1,7],
        [2,1]
        ]

    part2_counts = [data.TreeCount(x) for x in part2_list]
    p2_count = 1
    for cnt in part2_counts:
        p2_count = p2_count * cnt

    print("Part2: ", p2_count)

main()
