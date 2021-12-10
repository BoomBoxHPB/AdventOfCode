#!/usr/bin/env python3
import sys
# import re
import copy
import itertools
import functools
import utils


def main():
    data = [int(line) for line in utils.read_lines()]
    data.sort()

    current = 0
    gaps = []

    for i in data:
        if current + 3 < i:
            break
        gaps.append(i - current)
        current = i

    gaps.append(3)
    current += 3

    ones = gaps.count(1)
    threes = gaps.count(3)
    print('Part1 {}'.format(ones * threes))

    goal = current
    p2total = 0

    @functools.lru_cache(maxsize=None)
    def IsValid(data1):
        cur = 0
        for i in data1:
            if cur + 3 < i:
                break
            cur = i

        cur += 3

        if cur == goal:
            return True


    for r in range(round((goal+2) / 3), len(data)+1):
        for stuff in itertools.combinations(data, r):
            if IsValid(stuff):
                p2total += 1

    print('Part2 {}'.format(p2total))

    # good_sets = []

    # @functools.lru_cache(maxsize=None)
    # def GetCount(data1):
    #     # if data1 in good_sets:
    #     #     print('found', data1)
    #     #     return 0

    #     total = 0

    #     cur = 0
    #     for i in data1:
    #         if cur + 3 < i:
    #             break
    #         cur = i

    #     cur += 3

    #     if cur == goal:
    #         total += 1
    #         # good_sets.append(data1)
    #         # print(len(data1), cur, goal)
    #         for d2 in itertools.combinations(data1, len(data1)-1):
    #             total += GetCount(d2)

    #     return total

    # print('Part2 {}'.format(GetCount(tuple(data))))


main()
